import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#checking for outliers in the dataset using boxplots
import pandas as pd

def iqr_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] < lower) | (df[column] > upper)]

# Outliers for age
age_outliers = iqr_outliers(df, "age")

# Outliers for bmi
bmi_outliers = iqr_outliers(df, "bmi")

age_outliers, bmi_outliers

df[["age", "bmi"]].describe()


def boxplot_with_outliers(df, column):
    plt.figure(figsize=(6, 5))

    # Draw boxplot
    sns.boxplot(y=df[column], color="lightblue")

    # Calculate IQR boundaries
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df[column] < lower) | (df[column] > upper)]

    # Overlay outlier points
    sns.scatterplot(
        y=outliers[column],
        x=[0] * len(outliers),
        color="red",
        s=60,
        label="Outliers"
    )

    # Label each outlier
    for i, value in outliers[column].items():
        plt.text(
            0.02, value,
            f"{value}",
            fontsize=9,
            color="black",
            va="center"
        )

    plt.title(f"Boxplot with Outliers Labeled: {column}")
    plt.ylabel(column)
    plt.legend()
    plt.show()

# Run for both columns
boxplot_with_outliers(df, "bmi")
boxplot_with_outliers(df, "age")

#no outliers were found in the age column, so will now bucket up age into groups for better analysis
# Create Age Groups for easier demographic bar charts

bins_age =[17, 35, 50, 65, 100]
labels_age =['18-35', '36-50', '51-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=bins_age, labels=labels_age)

#bmi outliers were found, but since bmi is a key health indicator, we will keep them in the dataset for analysis and not remove them. We will also bucket up bmi into groups for better analysis.
# Create BMI Groups for easier demographic bar charts(WHO Standard)
bins_bmi =[0, 18.5, 24.9, 29.9, 100]
labels_bmi =['Underweight', 'Normal Weight', 'Overweight', 'Obese']
df['bmi_category'] = pd.cut(df['bmi'], bins=bins_bmi, labels=labels_bmi)
print(df.head())

# Save the transformed dataset
output_file = 'healthcare_dataset_transformed.csv'
df.to_csv(output_file, index=False)
print(f"File saved to {output_file}")
print(df.head())

