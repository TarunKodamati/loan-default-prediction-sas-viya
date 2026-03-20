# Loan Default Prediction using SAS Viya Model Studio

##  Project Overview

This project focuses on predicting whether a borrower will default on a loan using historical LendingClub data. The goal is to help financial institutions identify high-risk borrowers and make better lending decisions.

---

##  Objective

To build a predictive model that classifies borrowers into:

- **1 → Default**
- **0 → Non-default**

---

##  Tools & Technologies

- SAS Viya Model Studio  
- Python (for preprocessing)  
- LendingClub Dataset  

---

##  Dataset Information

- Source: LendingClub  
- Time Period: 2017–2018  
- Dataset contains borrower financial and credit-related features  

### Key Variables

- dti → Debt-to-Income ratio  
- revol_util → Credit utilization  
- fico_score → Credit score  
- annual_inc → Annual income  
- delinq_2yrs → Past delinquencies  

---

##  Data Preprocessing

- Removed data leakage variables (e.g., total_pymnt, recoveries)  
- Handled missing values  
- Log transformation for skewed variables  
- Converted categorical variables into Nominal/Class variables  
- Selected important features for modeling  

---

##  Model Development

- Built using SAS Viya Model Studio pipeline  
- Data split:
  - Train: 70%  
  - Validation: 30%  

### Models evaluated:

- Logistic Regression  
- Decision Tree  
- Random Forest  

---

##  Model Performance

- Evaluated using:
  - ROC Curve  
  - AUC (Area Under Curve)  
  - Confusion Matrix  

 The model shows strong ability to distinguish between default and non-default borrowers.

---

##  Key Insights

- Higher DTI → higher default risk  
- Higher credit utilization → financial stress  
- Past delinquencies strongly impact default  
- Lower FICO score → higher probability of default  

---

##  Conclusion

The model effectively predicts borrower risk and provides valuable insights for better lending decisions.
