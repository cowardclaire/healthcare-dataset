import pandas as pd

#importing the dataset and previewing the first few rows
df = pd.read_csv('data.csv')
print(df.head())

#checking for missing values in the dataset
df.isnull().sum()   
print(df.isnull().sum())

#checking the data types of each column and the overall structure of the dataset
df.info()

#remove health_risk column as it is not needed for the analysis
df.drop('health_risk_score', axis=1, inplace=True)    
print(df.head())

# Map binary 0/1 to No/Yes for readable visual legends
binary_cols = ['smoking', 'alcohol', 'fatigue', 'chest_pain', 'dizziness', 'heart_disease', 'diabetes', 'stroke']
for col in binary_cols:
    df[col] = df[col].map({0: 'No', 1: 'Yes'})

# Map exercise level ordinal values
df['exercise_level'] = df['exercise_level'].map({0: 'Low', 1: 'Moderate', 2: 'High'})

# Create Age Groups for easier demographic bar charts
bins_age = [17, 35, 50, 65, 100]
labels_age = ['18-35', '36-50', '51-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=bins_age, labels=labels_age)

# Create BMI Categories (WHO Standard)
bins_bmi = [0, 18.5, 24.9, 29.9, 100]
labels_bmi = ['Underweight', 'Normal Weight', 'Overweight', 'Obese']
df['bmi_category'] = pd.cut(df['bmi'], bins=bins_bmi, labels=labels_bmi)
print(df.head())

