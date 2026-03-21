# Data Preprocessing

## Overview
Before building the predictive model, the dataset was cleaned and transformed to ensure data quality and improve model performance. The preprocessing steps were performed using SAS Viya Model Studio.

## Log Transformation
Several numerical variables in the dataset exhibited highly skewed distributions, which is common in financial data. Variables such as annual income, revolving balance, and total balances often have extreme values that can negatively impact model performance.
To address this, log transformation was applied to selected variables. This transformation compresses large values and reduces skewness, resulting in a more normalized distribution. By stabilizing variance and reducing the influence of outliers, log transformation helps machine learning models learn patterns more effectively and improves overall model stability.

<img width="1775" height="769" alt="image" src="https://github.com/user-attachments/assets/aab4ff82-3d81-453b-930c-251dc35089a3" />

## One Hot Encoding
The dataset includes multiple categorical variables such as home ownership, loan purpose, verification status, and application type. Since most machine learning algorithms require numerical input, these categorical variables were transformed using one hot encoding.
One hot encoding creates separate binary columns for each category within a variable. For example, a variable like home ownership is converted into multiple columns representing rent, own, and mortgage. This approach ensures that no artificial ordering is introduced between categories and allows the model to treat each category independently.

<img width="1770" height="355" alt="image" src="https://github.com/user-attachments/assets/708a5009-4e55-4af4-ab70-4e82f1a3347f" />

## Handling Missing Values
Missing values were analyzed across all variables.  
- Variables with a high percentage of missing values were removed  
- For numerical variables, missing values were imputed using appropriate statistical methods  
- For categorical variables, missing values were handled by assigning a separate category or using imputation techniques
<img width="1783" height="589" alt="image" src="https://github.com/user-attachments/assets/2b276161-58e6-42d5-8120-7b5ac0790b8d" />


## Data Leakage Removal
Certain variables were removed because they contained information that would not be available at the time of prediction.  
- Variables such as total payments, recoveries, and remaining principal were excluded  
- This step ensured that the model does not learn from future information  

## Data Partitioning
The dataset was split into training and validation sets.  
- Training data was used to build the model  
- Validation data was used to evaluate model performance  

## Summary
These preprocessing steps ensured that the dataset was clean, consistent, and suitable for predictive modeling. Proper data preparation helped improve model accuracy and reliability.
