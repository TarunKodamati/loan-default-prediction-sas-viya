## Key Variables

The following variables were identified as important predictors in the model based on analysis performed in SAS Viya Model Studio. These features had a strong influence on loan default prediction.

### Credit Risk Indicators
dti – Debt to income ratio, indicating borrower’s financial burden  
fico_score – Credit score representing borrower’s creditworthiness  
sub_grade – Risk grade assigned by the lender  

### Loan Characteristics
loan_amnt – Total loan amount requested  
term – Duration of the loan  
int_rate – Interest rate applied to the loan  

### Credit Behavior
delinq_2yrs – Number of delinquencies in the past two years  
inq_last_6mths – Number of recent credit inquiries  
revol_util – Credit utilization ratio  

### Financial Strength
annual_inc – Borrower’s annual income  
tot_cur_bal – Total current balance across all accounts  
avg_cur_bal – Average account balance  

### Account Activity
open_acc – Number of open accounts  
total_acc – Total number of credit accounts  
acc_open_past_24mths – Accounts opened in the last 24 months  

## Summary
These variables were selected based on their contribution to model performance and their relevance in explaining borrower risk. They help in identifying patterns associated with loan defaults and improve the model’s predictive accuracy.

<img width="1757" height="848" alt="image" src="https://github.com/user-attachments/assets/537bdc25-3363-4fd6-bb26-469d95811c1f" />
