import pandas as pd
import joblib

predict_df = pd.read_csv('employee_data.csv')
predict_df = predict_df[predict_df['Attrition'].isna()].copy()

predict_df['Education'] = predict_df['Education'].astype(str)
predict_df['EnvironmentSatisfaction'] = predict_df['EnvironmentSatisfaction'].astype(str)
predict_df['JobInvolvement'] = predict_df['JobInvolvement'].astype(str)
predict_df['JobLevel'] = predict_df['JobLevel'].astype(str)
predict_df['JobSatisfaction'] = predict_df['JobSatisfaction'].astype(str)
predict_df['PerformanceRating'] = predict_df['PerformanceRating'].astype(str)
predict_df['RelationshipSatisfaction'] = predict_df['RelationshipSatisfaction'].astype(str)
predict_df['StockOptionLevel'] = predict_df['StockOptionLevel'].astype(str)
predict_df['WorkLifeBalance'] = predict_df['WorkLifeBalance'].astype(str)

predict_df = predict_df.drop(columns=['EmployeeCount', 'Over18', 'StandardHours', 'Attrition'])

anomaly_predict_df = predict_df[(predict_df['TotalWorkingYears'] > 0) & (predict_df['NumCompaniesWorked'] == 0) & (predict_df['YearsAtCompany'] < predict_df['TotalWorkingYears'])]
print('Anomaly Data Amount:', len(anomaly_predict_df))
predict_df = predict_df.drop(anomaly_predict_df.index)
print('Remaining Data Amount', len(predict_df))

predict_df['SatisfactionScore'] = (predict_df['EnvironmentSatisfaction'].astype(int) + predict_df['JobSatisfaction'].astype(int) + predict_df['RelationshipSatisfaction'].astype(int)) / 3
predict_df['PromotionGap'] = predict_df['YearsAtCompany'] - predict_df['YearsSinceLastPromotion']
predict_df['YearsInRoleRatio'] = predict_df['YearsInCurrentRole'] / predict_df['YearsAtCompany']
predict_df['YearsInRoleRatio'] = predict_df['YearsInRoleRatio'].fillna(0)

bins = [17, 30, 36, 44, 70]
labels = ['Young', 'Mid-Age', 'Senior', 'Old']
predict_df['AgeGroup'] = pd.cut(predict_df['Age'], bins=bins, labels=labels)

bins = [0, 2906, 5010, 9082, float('inf')]
labels = ['Low', 'Lower-Mid', 'Upper-Mid', 'High']
predict_df['MonthlyIncomeGroup'] = pd.cut(predict_df['MonthlyIncome'], bins=bins, labels=labels)

selected_cols = [
    'YearsInRoleRatio', 'YearsAtCompany', 'PromotionGap', 
    'YearsWithCurrManager', 'SatisfactionScore', 'YearsInCurrentRole', 
    'MonthlyIncome', 'Age', 'TotalWorkingYears', 
    'BusinessTravel', 'EnvironmentSatisfaction', 'JobInvolvement', 
    'JobLevel', 'JobRole', 'MaritalStatus', 
    'OverTime', 'StockOptionLevel', 'WorkLifeBalance', 
    'AgeGroup', 'MonthlyIncomeGroup',
]

predict_df = predict_df[selected_cols]

predict_df['AgeGroup'] = predict_df['AgeGroup'].map({
    'Young': 0,
    'Mid-Age': 1,
    'Senior': 2,
    'Old': 3,
})
predict_df['AgeGroup'] = predict_df['AgeGroup'].astype(int)

predict_df['MonthlyIncomeGroup'] = predict_df['MonthlyIncomeGroup'].map({
    'Low': 0,
    'Lower-Mid': 1,
    'Upper-Mid': 2,
    'High': 3,
})
predict_df['MonthlyIncomeGroup'] = predict_df['MonthlyIncomeGroup'].astype(int)

predict_df = pd.get_dummies(
    predict_df,
    columns=['BusinessTravel', 'JobRole', 'MaritalStatus', 'OverTime'],
    dtype=int,
)
print(predict_df.shape)

scaler_saved = joblib.load('scaler.pkl')
X_predict_scaled = scaler_saved.transform(predict_df)

lr_model = joblib.load('lr_model.pkl')
lr_y_pred = lr_model.predict(X_predict_scaled)

predict_df['Attrition'] = lr_y_pred
print(predict_df.sample(5))