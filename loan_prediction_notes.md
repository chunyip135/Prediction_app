# Predict whether loan is given or not

## a. EDA
1. missing values in both train & test data but around 1% to 8% of the data
2. Created heatmap
    * ApplicantIncome & LoanAmount is positive correlated with 0.57
3. most of the data in train have loan approved (70%)
    * think of imbalanced class problem exists
4. 80% of applicant are male
    * prpoertion of having loan approved are approx the same (65-69%)
5. married applicant have slightly higher approving rate with 71% compared to 61%

6. Married and Male have the highest approving rate

7. Applicant that are graduated have a slightly higher approving rate

8. Self-employed applicants have higher income

9. Total income for Male is higher 

10. Loan status approved have lower income than not approved

11. Applicant that are approved have lower LoanAmount 
    * As the Total income increases, the Loan Amount also increases
    * People with higher income tend have larger borrowings

12. Most of the loans are 1-year term

13. Most of the applicants have credit history
    * applicants with credit history tends to have higher approving rate (79%)

14. Try different Machine Learning algorithms
    * applyign feature engineering by taking the log for total income 
    * the RF, LR, LR, SGD, LinearSVC, SVC
    * Final chosen model are RF, XG, LR with accuracy of 83.9%
        - chosen columns are log(total income), EMI, Gender, Married, Dependents, Education, Self-employed, Credit history & Property area




    
