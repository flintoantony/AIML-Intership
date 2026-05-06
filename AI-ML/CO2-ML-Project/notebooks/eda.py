import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('C:/Users/Antony/internship/AI/CO2-ML-Project/data/CO2_emission.csv')

# Display first rows
print(df.head())

# Dataset info
print(df.info())

# Statistical summary
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate values
print("\nDuplicates:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# ---------------- VISUALIZATIONS ---------------- #

# 1 Histogram
df.hist(figsize=(15,10))
plt.tight_layout()
plt.savefig('images/histogram.png')   
plt.show()

# 2 Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.savefig('images/heatmap.png')   
plt.show()

# 3 CO2 emission by vehicle class
plt.figure(figsize=(12,6))
sns.boxplot(x='Vehicle_Class', y='CO2_Emissions', data=df)
plt.xticks(rotation=90)
plt.savefig('images/boxplot.png') 
plt.show()

# 4 Engine size vs CO2 emission
plt.figure(figsize=(8,6))
sns.scatterplot(x='Engine_Size', y='CO2_Emissions', data=df)
plt.savefig('images/scatter.png') 
plt.show()

print("EDA Completed Successfully")