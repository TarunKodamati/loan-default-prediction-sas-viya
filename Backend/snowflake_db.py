import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        role=os.getenv("SNOWFLAKE_ROLE"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    return conn

def save_application(data, prediction, probability):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO LOAN_APPLICATIONS (
                LOAN_AMNT, TERM, INT_RATE, PURPOSE, SUB_GRADE,
                ANNUAL_INC, EMP_LENGTH, HOME_OWNERSHIP, VERIFICATION_STATUS,
                FICO_SCORE, DTI, DELINQ_2YRS, INQ_LAST_6MTHS,
                OPEN_ACC, TOTAL_ACC, MORT_ACC, REVOL_BAL, REVOL_UTIL,
                NUM_REV_TL_BAL_GT_0, TOT_HI_CRED_LIM, ISSUE_MONTH,
                ISSUE_YEAR, MTHS_SINCE_RECENT_BC, BC_OPEN_TO_BUY,
                PREDICTION, PROBABILITY
            ) VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s
            )
        """, (
            data.get("loan_amnt"), data.get("term"), data.get("int_rate"),
            data.get("purpose"), data.get("sub_grade"), data.get("annual_inc"),
            data.get("emp_length"), data.get("home_ownership"),
            data.get("verification_status"), data.get("fico_score"),
            data.get("dti"), data.get("delinq_2yrs"), data.get("inq_last_6mths"),
            data.get("open_acc"), data.get("total_acc"), data.get("mort_acc"),
            data.get("revol_bal"), data.get("revol_util"),
            data.get("num_rev_tl_bal_gt_0"), data.get("tot_hi_cred_lim"),
            data.get("issue_month"), data.get("issue_year"),
            data.get("mths_since_recent_bc"), data.get("bc_open_to_buy"),
            prediction, probability
        ))
        conn.commit()
        print("Application saved to Snowflake")
    except Exception as e:
        print(f"Snowflake error: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()

def get_all_applications():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM LOAN_APPLICATIONS ORDER BY SUBMITTED_AT DESC")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    finally:
        cursor.close()
        conn.close()