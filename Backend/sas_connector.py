import requests
import urllib3
import os
from dotenv import load_dotenv
load_dotenv()
urllib3.disable_warnings()

SAS_VIYA_URL = os.getenv("https://vfl-026.engage.sas.com/microanalyticScore/modules/lr_step__pipeline_2_/steps/score")
SAS_USER = "tkodamati"
SAS_PASS = os.getenv("Sraa37342@123")
SAS_BASE = "https://vfl-026.engage.sas.com"

def get_session():
    
    session = requests.Session()
    session.verify = False
    
    # Step 1: Get login page
    session.get(f"{SAS_BASE}/SASLogon/login")
    
    # Step 2: Login with credentials
    login_data = {
        "username": SAS_USER,
        "password": SAS_PASS,
        "lt": "",
        "execution": "e1s1",
        "_eventId": "submit"
    }
    
    response = session.post(
        f"{SAS_BASE}/SASLogon/login",
        data=login_data,
        allow_redirects=True
    )
    
    print(f"Login status: {response.status_code}")
    return session

def score_application(data):
    try:
        session = get_session()
        
        payload = {
            "inputs": [
                {"name": "loan_amnt", "value": data.get("loan_amnt", 0)},
                {"name": "int_rate", "value": data.get("int_rate", 0)},
                {"name": "dti", "value": data.get("dti", 0)},
                {"name": "fico_score", "value": data.get("fico_score", 0)},
                {"name": "annual_inc", "value": data.get("annual_inc", 0)},
                {"name": "emp_length", "value": data.get("emp_length", "")},
                {"name": "home_ownership", "value": data.get("home_ownership", "")},
                {"name": "verification_status", "value": data.get("verification_status", "")},
                {"name": "Purpose", "value": data.get("purpose", "")},
                {"name": "sub_grade", "value": data.get("sub_grade", "")},
                {"name": "term", "value": data.get("term", "")},
                {"name": "inq_last_6mths", "value": data.get("inq_last_6mths", 0)},
                {"name": "open_acc", "value": data.get("open_acc", 0)},
                {"name": "total_acc", "value": data.get("total_acc", 0)},
                {"name": "mort_acc", "value": data.get("mort_acc", 0)},
                {"name": "revol_bal", "value": data.get("revol_bal", 0)},
                {"name": "revol_util", "value": data.get("revol_util", 0)},
                {"name": "num_rev_tl_bal_gt_0", "value": data.get("num_rev_tl_bal_gt_0", 0)},
                {"name": "tot_hi_cred_lim", "value": data.get("tot_hi_cred_lim", 0)},
                {"name": "delinq_2yrs", "value": data.get("delinq_2yrs", 0)},
                {"name": "issue_month", "value": data.get("issue_month", 1)},
                {"name": "issue_year", "value": data.get("issue_year", 2024)},
                {"name": "mths_since_recent_bc", "value": data.get("mths_since_recent_bc", 0)},
                {"name": "bc_open_to_buy", "value": data.get("bc_open_to_buy", 0)}
            ]
        }

        response = session.post(
            SAS_VIYA_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"SAS Response: {response.status_code}")
        print(f"SAS Result: {response.text}")
        
        result = response.json()
        outputs = {o["name"]: o["value"] for o in result.get("outputs", [])}
        i_loan_status = str(outputs.get("I_loan_status", "0")).strip()
        p_loan_status1 = float(outputs.get("P_loan_status1", 0.22))
        approved = i_loan_status == "1"
        
        return {
            "approved": approved,
            "probability": round(p_loan_status1, 4),
            "prediction": "Approved" if approved else "Not Approved",
            "source": "SAS Viya Real Model "
        }

    except Exception as e:
        print(f"SAS error: {e} — using demo scoring")
        return demo_scoring(data)


def demo_scoring(data):
    import math
    score = 0
    fico = data.get("fico_score", 0)
    rate = data.get("int_rate", 0)
    dti = data.get("dti", 0)

    if fico >= 750: score += 30
    elif fico >= 700: score += 20
    elif fico >= 650: score += 10
    else: score -= 15

    if rate < 8: score += 20
    elif rate < 15: score += 10
    elif rate > 22: score -= 20

    if dti < 15: score += 15
    elif dti < 25: score += 5
    else: score -= 10

    if data.get("term") == "36 months": score += 10
    if data.get("delinq_2yrs", 0) == 0: score += 10
    if data.get("inq_last_6mths", 0) == 0: score += 5

    prob = 1 / (1 + math.exp(-score * 0.08))
    approved = prob >= 0.5

    return {
        "approved": approved,
        "probability": round(prob, 4),
        "prediction": "Approved" if approved else "Not Approved",
        "source": "Demo Scoring"
    }