import requests
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings()

SAS_VIYA_URL = "https://vfl-026.engage.sas.com/microanalyticScore/modules/lr_step__pipeline_2_/steps/score"
SAS_VIYA_TOKEN = os.getenv("eyJqa3UiOiJodHRwczovL2xvY2FsaG9zdC9TQVNMb2dvbi90b2tlbl9rZXlzIiwia2lkIjoibGVnYWN5LXRva2VuLWtlWSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2YTEyNWUzMy03NzRjLTQyMDktYWI3ZC1lOGQzMTdiY2U5MmQiLCJzZXNzaW9uX3NpZyI6IjQ5OGQxZGNiLTE2OGUtNDFmOS1iN2E4LWM1MjNlYTEzZDgzNCIsInVzZXJfbmFtZSI6InRrb2RhbWF0aUB1Y28uZWR1Iiwib3JpZ2luIjoiZXh0ZXJuYWxfb2F1dGgiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0L1NBU0xvZ29uL29hdXRoL3Rva2VuIiwiYXV0aG9yaXRpZXMiOlsiVlNDb2RlR2VuQUkiLCJEYXRhUXVhbGl0eS5EYXRhUXVhbGl0eU1vbml0b3JpbmdBZG1pbmlzdHJhdG9ycyIsIkRhdGFCdWlsZGVycyIsIkJhdGNoU2VydmljZUFjY291bnRVc2VycyIsIkFwcGxpY2F0aW9uQWRtaW5pc3RyYXRvcnMiLCJMYXVuY2hlclN1cGVyVXNlcnMiLCJFc3JpVXNlcnMiLCJEYXRhQWdlbnRBZG1pbmlzdHJhdG9ycyIsIkRhdGFBZ2VudFBvd2VyVXNlcnMiLCJTQ0lNIiwiU0FTU2NvcmVVc2VycyIsIkdsb3NzYXJ5Lkdsb3NzYXJ5QWRtaW5pc3RyYXRvcnMiLCJDYXRhbG9nLlN1YmplY3RNYXR0ZXJFeHBlcnRzIiwiQ29tcHV0ZVNlcnZpY2VBY2NvdW50VXNlcnMiLCJDQVNIb3N0QWNjb3VudFJlcXVpcmVkIl0sImNsaWVudF9pZCI6ImpodWJ1c２VyIiwiYXVkIjpbImpodWJ1c２VyIiwib3BlbmlkIl0sImV4dF9pZCI6IjAwdW9ybmdjZW5wN08xendaMnA3IiwicmVtb3RlX2lwIjoiMTcyLjU5LjEyNS4xMTciLCJ6aWQiOiJ1YWEiLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwidXNlcl9pZCI6IjZhMTI1ZTMzLTc3NGMtNDIwOS1hYjdkLWU4ZDMxN2JjZTkyZCIsImF6cCI6ImpodWJ1c２VyIiwic2NvcGUiOlsib3BlbmlkIl0sImF1dGhfdGltZSI6MTc3NDY2NzI1OCwiZXhwIjoxNzc1OTYzMjU4LCJpYXQiOjE3NzQ2NjcyNTgsImp0aSI6IjlmMmMzZTRmMTQ2ZDQzM2NhYjA0ZDFlN2I4Y２RhMTVlIiwiZW1haWwiOiJ0a29kYW1hdGlAdWNvLmVkdSIsInJldl9zaWciOiIxYzU5ZDM２UiIsImNpZCI6ImpodWJ1c２VyIn0.tu8Md0xnPCLb-6RpO5YJg5bDd-₂sqoqm3swwpRljriPAyU5Yx11ohFSiveEXtfXXOImqlvt1Vzw8jyKUSNYBcZogE0v3zoXif7quZfeIgAoF6GgqF9cCaieD-FMmblOujT0ixbAmme631Y8bf9Of80X0h5KD₂AsBcq4fxvcWrf₁NBCc5₂zIZSQflnIen-z8owLHfCMY3PUd6SVCE5QxEDnAS73ml₂1Ev8cfQHqKRXCekbqEd7Dqb6MlhhSZPWhbx3gRfoy3z6zBUueBWUnVLOVNtdorXVRhNGtgXeVoJY7BMzfvUnAabEMAoleVxVhp5p-0AskVFbm33xRNR9aoww")


def score_application(data):
    """
    Sends loan application data to SAS Viya MAS endpoint
    and returns prediction result.
    """
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SAS_VIYA_TOKEN}"
        }

        payload = {
            "inputs": [
                # Core loan details
                {"name": "loan_amnt",                   "value": float(data.get("loan_amnt", 0))},
                {"name": "int_rate",                    "value": float(data.get("int_rate", 0))},
                {"name": "dti",                         "value": float(data.get("dti", 0))},
                {"name": "term",                        "value": str(data.get("term", "36 months"))},
                {"name": "Purpose",                     "value": str(data.get("purpose", "Other"))},
                {"name": "sub_grade",                   "value": str(data.get("sub_grade", "B3"))},
                {"name": "disbursement_method",         "value": "Cash"},
                {"name": "application_type",            "value": "Individual"},
                {"name": "initial_list_status",         "value": "w"},

                # Personal info
                {"name": "annual_inc",                  "value": float(data.get("annual_inc", 0))},
                {"name": "emp_length",                  "value": str(data.get("emp_length", "1 year"))},
                {"name": "home_ownership",              "value": str(data.get("home_ownership", "RENT"))},
                {"name": "verification_status",         "value": str(data.get("verification_status", "Not Verified"))},

                # Credit score & history
                {"name": "fico_score",                  "value": float(data.get("fico_score", 0))},
                {"name": "credit_history_years",        "value": float(data.get("credit_history_years", 5))},
                {"name": "inq_last_6mths",              "value": float(data.get("inq_last_6mths", 0))},
                {"name": "delinq_2yrs",                 "value": float(data.get("delinq_2yrs", 0))},
                {"name": "delinq_amnt",                 "value": float(data.get("delinq_amnt", 0))},
                {"name": "acc_now_delinq",              "value": float(data.get("acc_now_delinq", 0))},
                {"name": "pub_rec",                     "value": float(data.get("pub_rec", 0))},
                {"name": "tax_liens",                   "value": float(data.get("tax_liens", 0))},
                {"name": "collections_12_mths_ex_med",  "value": float(data.get("collections_12_mths_ex_med", 0))},

                # Accounts
                {"name": "open_acc",                    "value": float(data.get("open_acc", 0))},
                {"name": "total_acc",                   "value": float(data.get("total_acc", 0))},
                {"name": "mort_acc",                    "value": float(data.get("mort_acc", 0))},
                {"name": "num_rev_tl_bal_gt_0",         "value": float(data.get("num_rev_tl_bal_gt_0", 0))},

                # Revolving
                {"name": "revol_bal",                   "value": float(data.get("revol_bal", 0))},
                {"name": "revol_util",                  "value": float(data.get("revol_util", 0))},
                {"name": "bc_util",                     "value": float(data.get("revol_util", 0))},
                {"name": "bc_open_to_buy",              "value": float(data.get("bc_open_to_buy", 5000))},
                {"name": "max_bal_bc",                  "value": float(data.get("max_bal_bc", 5000))},
                {"name": "percent_bc_gt_75",            "value": float(data.get("percent_bc_gt_75", 25))},

                # Balances & limits
                {"name": "tot_hi_cred_lim",             "value": float(data.get("tot_hi_cred_lim", 50000))},
                {"name": "total_rev_hi_lim",            "value": float(data.get("tot_hi_cred_lim", 50000))},
                {"name": "avg_cur_bal",                 "value": float(data.get("avg_cur_bal", 8000))},
                {"name": "total_bal_il",                "value": float(data.get("total_bal_il", 10000))},
                {"name": "total_bal_ex_mort",           "value": float(data.get("total_bal_ex_mort", 15000))},
                {"name": "tot_coll_amt",                "value": float(data.get("tot_coll_amt", 0))},
                {"name": "total_il_high_credit_limit",  "value": float(data.get("total_il_high_credit_limit", 20000))},
                {"name": "total_cu_tl",                 "value": float(data.get("total_cu_tl", 5))},
                {"name": "il_util",                     "value": float(data.get("il_util", 50))},

                # Months since
                {"name": "mths_since_recent_bc",        "value": float(data.get("mths_since_recent_bc", 6))},
                {"name": "mo_sin_rcnt_tl",              "value": float(data.get("mo_sin_rcnt_tl", 6))},
                {"name": "mo_sin_rcnt_rev_tl_op",       "value": float(data.get("mo_sin_rcnt_rev_tl_op", 6))},
                {"name": "mo_sin_old_rev_tl_op",        "value": float(data.get("mo_sin_old_rev_tl_op", 60))},
                {"name": "mo_sin_old_il_acct",          "value": float(data.get("mo_sin_old_il_acct", 60))},
                {"name": "mths_since_rcnt_il",          "value": float(data.get("mths_since_rcnt_il", 12))},

                # Delinquency counts
                {"name": "num_tl_90g_dpd_24m",          "value": float(data.get("num_tl_90g_dpd_24m", 0))},
                {"name": "num_tl_30dpd",                "value": float(data.get("num_tl_30dpd", 0))},
                {"name": "num_tl_120dpd_2m",            "value": float(data.get("num_tl_120dpd_2m", 0))},

                # Issue date
                {"name": "issue_month",                 "value": int(data.get("issue_month", 3))},
                {"name": "issue_year",                  "value": int(data.get("issue_year", 2024))},
            ]
        }

        print(f"Sending to SAS Viya: {SAS_VIYA_URL}")
        response = requests.post(
            SAS_VIYA_URL,
            json=payload,
            headers=headers,
            verify=False
        )

        print(f"SAS Viya Status: {response.status_code}")
        print(f"SAS Viya Response: {response.text[:300]}")

        if response.status_code == 200:
            result = response.json()
            outputs = {o["name"]: o["value"] for o in result.get("outputs", [])}
            i_loan_status = str(outputs.get("I_loan_status", "0")).strip()
            p_loan_status1 = float(outputs.get("P_loan_status1", 0.22))
            approved = i_loan_status == "1"

            return {
                "approved": approved,
                "probability": round(p_loan_status1, 4),
                "prediction": "Approved" if approved else "Not Approved",
                "source": "SAS Viya Real Model"
            }
        else:
            print(f"SAS Viya error {response.status_code} - using demo scoring")
            return demo_scoring(data)

    except Exception as e:
        print(f"SAS error: {e} - using demo scoring")
        return demo_scoring(data)


def demo_scoring(data):
    """Demo scoring - used when SAS Viya not connected"""
    import math
    score = 0
    fico = data.get("fico_score", 0)
    rate = data.get("int_rate", 0)
    dti  = data.get("dti", 0)

    if fico >= 750:   score += 30
    elif fico >= 700: score += 20
    elif fico >= 650: score += 10
    else:             score -= 15

    if rate < 8:    score += 20
    elif rate < 15: score += 10
    elif rate > 22: score -= 20

    if dti < 15:   score += 15
    elif dti < 25: score += 5
    else:          score -= 10

    if data.get("term") == "36 months":     score += 10
    if data.get("delinq_2yrs", 0) == 0:    score += 10
    if data.get("inq_last_6mths", 0) == 0: score += 5

    prob = 1 / (1 + math.exp(-score * 0.08))
    approved = prob >= 0.5

    return {
        "approved": approved,
        "probability": round(prob, 4),
        "prediction": "Approved" if approved else "Not Approved",
        "source": "Demo Scoring"
    }
