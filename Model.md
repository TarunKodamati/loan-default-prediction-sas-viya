# Model Performance

## Overview
The performance of multiple models was evaluated using SAS Viya Model Studio. Among all the models tested, logistic regression was selected as the final model based on its overall performance and consistency across evaluation metrics.

## Model Metrics

The logistic regression model demonstrated strong and stable performance on both training and validation datasets.

- Accuracy: approximately 78 percent on both training and validation data  
- F1 Score: approximately 0.17 at cutoff 0.5  
- KS Statistic cutoff around 0.22 indicating good class separation  

The similar performance between training and validation datasets indicates that the model generalizes well and does not suffer from overfitting.
<img width="1760" height="162" alt="image" src="https://github.com/user-attachments/assets/08db33be-bb9c-4d25-88d9-43773ba72b86" />


## ROC Curve Analysis

The ROC curve shows the trade-off between sensitivity and specificity across different thresholds.

- The curve is significantly above the diagonal line, indicating strong predictive power  
- The model is able to distinguish between default and non-default borrowers effectively  

<img width="1417" height="798" alt="image" src="https://github.com/user-attachments/assets/e4435f70-0165-4c19-b59d-d8d9b92887ef" />

## Confusion Matrix Analysis

At the default cutoff of 0.5:

- True Positives: 5246
- True Negatives: 18543
- False Positives: 9618
- False Negatives: 2617

## Lift Analysis

Lift and cumulative lift charts were used to evaluate the model’s ability to identify high-risk borrowers.

- The model shows strong lift in the top deciles  
- Higher lift values indicate that the model effectively ranks high-risk borrowers at the top  
- This is useful for prioritizing loan approvals and risk management
<img width="889" height="455" alt="image" src="https://github.com/user-attachments/assets/c9aa630c-4d81-4eaf-863c-5de31dc8affe" />

<img width="897" height="465" alt="image" src="https://github.com/user-attachments/assets/0b1013f2-645b-41b3-a8e8-fe4b869d3c8a" />


## Key Insights from Model

Based on partial dependence plots and model behavior:

- Higher interest rates are associated with increased probability of default  
- Higher debt-to-income ratio leads to higher default risk  
- Longer loan terms show slightly lower predicted risk compared to shorter-term loans  
- Lower available credit is associated with higher default probability  


## Summary

The logistic regression model provided a balanced and interpretable solution with strong predictive performance. The model achieved consistent accuracy, demonstrated good class separation through ROC analysis, and provided meaningful business insights. This makes it suitable for identifying high-risk borrowers and supporting data-driven lending decisions.
