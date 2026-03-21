# LendingClub Dataset Description

## Overview
- This project uses the LendingClub loan dataset from 2017 to 2018, which contains comprehensive information about borrowers, loan characteristics, and credit history. The dataset includes both financial and behavioral attributes such as income, employment details, loan terms, credit utilization, and repayment patterns.

- The primary objective of this dataset is to support the development of a predictive model that can identify whether a borrower is likely to default on a loan. By analyzing historical lending data, the dataset captures patterns and relationships between borrower characteristics and loan outcomes.

- The data represents real-world lending scenarios and includes a wide range of variables related to credit risk assessment. These variables help in understanding borrower reliability, financial stability, and repayment capacity. The dataset also contains information about past delinquencies, credit inquiries, account balances, and utilization ratios, which are critical indicators in credit risk modeling.

- This dataset is well suited for classification problems in the financial domain, particularly for predicting loan default risk. It enables the application of machine learning and statistical techniques to identify high-risk borrowers and improve decision-making processes in lending institutions.

- Overall, the dataset provides a strong foundation for building data-driven solutions that can help financial organizations reduce default rates, manage risk more effectively, and optimize their lending strategies.

---

## Dataset Description

| Column                         | Description                                           | Role                    | Level    |
|--------------------------------|-------------------------------------------------------|-------------------------|----------|
| id                             | Unique loan identifier for each borrower              | Reject                  | Nominal  |
| loan_amnt                      | Total amount of loan requested by borrower            | Input                   | Interval |
| term                           | Length of loan (36 months or 60 months)               | Input                   | Nominal  |
| int_rate                       | Interest rate assigned to the loan                    | Input                   | Interval |
| installment                    | Monthly payment amount borrower must pay              | Input                   | Interval |
| sub_grade                      | Risk grade assigned to borrower by lender             | Input                   | Nominal  |
| emp_length                     | Borrower employment length                            | Input                   | Nominal  |
| home_ownership                 | Home ownership status (rent, own, mortgage)           | Input                   | Nominal  |
| annual_inc                     | Annual income reported by borrower                    | Input                   | Interval |
| verification_status            | Whether income was verified                           | Input                   | Nominal  |
| loan_status                    | Status of the loan (paid, default etc.)               | Target                  | Nominal  |
| purpose                        | Purpose of loan (car, credit card, etc.)              | Input                   | Nominal  |
| addr_state                     | Borrower's state                                      | Input                   | Nominal  |
| dti                            | Debt-to-income ratio                                  | Input                   | Interval |
| delinq_2yrs                    | Number of delinquencies in last 2 years               | Input                   | Interval |
| inq_last_6mths                 | Credit inquiries in last 6 months                     | Input                   | Interval |
| mths_since_last_delinq         | Months since last delinquency                         | Reject                  | Interval |
| mths_since_last_record         | Months since last public record                       | Reject                  | Interval |
| open_acc                       | Number of open credit accounts                        | Input                   | Interval |
| pub_rec                        | Number of derogatory public records                   | Input                   | Interval |
| revol_bal                      | Total revolving credit balance                        | Input                   | Interval |
| revol_util                     | Revolving credit utilization percentage               | Input                   | Interval |
| total_acc                      | Total number of credit accounts                       | Input                   | Interval |
| initial_list_status            | Initial listing status of loan                        | Input                   | Nominal  |
| out_prncp                      | Remaining principal balance                           | Reject                  | Interval |
| total_pymnt                    | Total payment received so far                         | Reject                  | Interval |
| total_rec_prncp                | Principal received to date                            | Reject                  | Interval |
| total_rec_int                  | Interest received to date                             | Reject                  | Interval |
| total_rec_late_fee             | Late fees received                                    | Reject                  | Interval |
| recoveries                     | Amount recovered after charge-off                     | Reject                  | Interval |
| collection_recovery_fee        | Collection fees after recovery                        | Reject                  | Interval |
| last_pymnt_amnt                | Last payment amount                                   | Reject                  | Interval |
| collections_12_mths_ex_med     | Collections in last 12 months                         | Input                   | Interval |
| mths_since_last_major_derog    | Months since last major derogatory mark               | Reject                  | Interval |
| application_type               | Individual or joint application                       | Input                   | Nominal  |
| acc_now_delinq                 | Number of accounts currently delinquent               | Input                   | Interval |
| tot_coll_amt                   | Total collection amount owed                          | Input                   | Interval |
| tot_cur_bal                    | Total current balance across accounts                 | Input                   | Interval |
| open_acc_6m                    | Accounts opened in last 6 months                      | Input                   | Interval |
| open_act_il                    | Active installment accounts                           | Input                   | Interval |
| open_il_12m                    | Installment accounts opened in last 12 months         | Input                   | Interval |
| open_il_24m                    | Installment accounts opened in last 24 months         | Input                   | Interval |
| mths_since_rcnt_il             | Months since recent installment account               | Input                   | Interval |
| total_bal_il                   | Total installment balance                             | Input                   | Interval |
| il_util                        | Installment utilization ratio                         | Input                   | Interval |
| open_rv_12m                    | Revolving accounts opened in 12 months                | Input                   | Interval |
| open_rv_24m                    | Revolving accounts opened in 24 months                | Input                   | Interval |
| max_bal_bc                     | Maximum balance on bankcard                           | Input                   | Interval |
| all_util                       | Balance to credit limit ratio                         | Input                   | Interval |
| total_rev_hi_lim               | Total revolving credit limit                          | Input                   | Interval |
| inq_fi                         | Financial inquiries count                             | Input                   | Interval |
| total_cu_tl                    | Total credit union trades                             | Input                   | Interval |
| inq_last_12m                   | Credit inquiries in last 12 months                    | Input                   | Interval |
| acc_open_past_24mths           | Accounts opened in last 24 months                     | Input                   | Interval |
| avg_cur_bal                    | Average current account balance                       | Input                   | Interval |
| bc_open_to_buy                 | Available credit on bankcards                         | Input                   | Interval |
| bc_util                        | Bankcard utilization ratio                            | Input                   | Interval |
| chargeoff_within_12_mths       | Charge-offs in last 12 months                         | Input                   | Interval |
| delinq_amnt                    | Amount currently delinquent                           | Input                   | Interval |
| mo_sin_old_il_acct             | Months since oldest installment account               | Input                   | Interval |
| mo_sin_old_rev_tl_op           | Months since oldest revolving account                 | Input                   | Interval |
| mo_sin_rcnt_rev_tl_op          | Months since recent revolving account                 | Input                   | Interval |
| mo_sin_rcnt_tl                 | Months since any recent account                       | Input                   | Interval |
| mort_acc                       | Number of mortgage accounts                           | Input                   | Interval |
| mths_since_recent_bc           | Months since recent bankcard account                  | Input                   | Interval |
| mths_since_recent_bc_dlq       | Months since recent bankcard delinquency              | Reject                  | Interval |
| mths_since_recent_inq          | Months since recent inquiry                           | Input                   | Interval |
| mths_since_recent_revol_delinq | Months since recent revolving delinquency             | Reject                  | Interval |
| num_accts_ever_120_pd          | Accounts ever 120 days past due                       | Input                   | Interval |
| num_actv_bc_tl                 | Active bankcard accounts                              | Input                   | Interval |
| num_actv_rev_tl                | Active revolving accounts                             | Input                   | Interval |
| num_bc_sats                    | Bankcard accounts with satisfactory status            | Input                   | Interval |
| num_bc_tl                      | Total bankcard accounts                               | Input                   | Interval |
| num_il_tl                      | Total installment accounts                            | Input                   | Interval |
| num_op_rev_tl                  | Open revolving accounts                               | Input                   | Interval |
| num_rev_accts                  | Total revolving accounts                              | Input                   | Interval |
| num_rev_tl_bal_gt_0            | Revolving accounts with balance                       | Input                   | Interval |
| num_sats                       | Total satisfactory accounts                           | Input                   | Interval |
| num_tl_120dpd_2m               | Accounts 120+ days past due in 2 months               | Input                   | Interval |
| num_tl_30dpd                   | Accounts 30+ days delinquent                          | Input                   | Interval |
| num_tl_90g_dpd_24m             | Accounts 90+ days delinquent in 24 months             | Input                   | Interval |
| num_tl_op_past_12m             | Accounts opened past 12 months                        | Input                   | Interval |
| pct_tl_nvr_dlq                 | Percent of accounts never delinquent                  | Input                   | Interval |
| percent_bc_gt_75               | Bankcard utilization above 75%                        | Input                   | Interval |
| pub_rec_bankruptcies           | Number of bankruptcies                                | Input                   | Interval |
| tax_liens                      | Number of tax liens                                   | Input                   | Interval |
| tot_hi_cred_lim                | Total high credit limit                               | Input                   | Interval |
| total_bal_ex_mort              | Total balance excluding mortgage                      | Input                   | Interval |
| total_bc_limit                 | Total bankcard credit limit                           | Input                   | Interval |
| total_il_high_credit_limit     | Installment high credit limit                         | Input                   | Interval |
| disbursement_method            | Method loan was disbursed                             | Input                   | Nominal  |
| debt_settlement_flag           | Whether borrower settled debt                         | Reject                  | Binary   |
| issue_year                     | Year loan issued                                      | Input                   | Interval |
| issue_month                    | Month loan issued                                     | Input                   | Nominal  |
| fico_score                     | Borrower FICO credit score                            | Input                   | Interval |
| last_fico_score                | Most recent FICO score                                | Input                   | Interval |
| earliest_cr_line_year          | Year credit history started                           | Input                   | Interval |
| earliest_cr_line_month         | Month credit history started                          | Input                   | Nominal  |
| credit_history_years           | Length of credit history                              | Input                   | Interval |
