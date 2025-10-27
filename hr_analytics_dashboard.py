
"""
HR Analytics Dashboard - Enhancing Employee Performance and Retention
Author: [Your Name]
Date: Mar 2024
Description:
    This script simulates the backend logic for building an HR analytics dashboard in Power BI.
    It processes employee data, calculates key KPIs, and exports clean datasets for Power BI integration.
"""

import pandas as pd
import numpy as np

# -----------------------------
# 1. Load and Preview Data
# -----------------------------
# Replace 'employee_data.csv' with your actual dataset
df = pd.read_csv('employee_data.csv')
print("Initial Data Preview:")
print(df.head())

# -----------------------------
# 2. Clean and Preprocess Data
# -----------------------------
# Handle missing values
df.fillna({
    'Age': df['Age'].median(),
    'Department': 'Unknown',
    'PerformanceScore': df['PerformanceScore'].mean()
}, inplace=True)

# Convert dates
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['LastEvaluationDate'] = pd.to_datetime(df['LastEvaluationDate'])

# -----------------------------
# 3. Feature Engineering
# -----------------------------
df['TenureMonths'] = (pd.Timestamp.now() - df['JoinDate']).dt.days // 30
df['RecentEvaluationGap'] = (pd.Timestamp.now() - df['LastEvaluationDate']).dt.days

# -----------------------------
# 4. Key Metrics & KPIs
# -----------------------------
# Performance buckets
df['PerformanceCategory'] = pd.cut(df['PerformanceScore'], 
                                   bins=[0, 2.5, 3.5, 5],
                                   labels=['Low', 'Average', 'High'])

# Engagement Index (dummy formula)
df['EngagementIndex'] = (df['SatisfactionScore'] * 0.6 + df['WorkLifeBalance'] * 0.4)

# Attrition Flag (1 = Left, 0 = Still working)
df['AttritionFlag'] = df['AttritionStatus'].apply(lambda x: 1 if x == 'Yes' else 0)

# -----------------------------
# 5. Export for Power BI
# -----------------------------
# Save clean and engineered data
df.to_csv('processed_hr_data.csv', index=False)
print("\nProcessed data saved as 'processed_hr_data.csv' for Power BI usage.")

# -----------------------------
# 6. Suggested Power BI Visuals (README Guide)
# -----------------------------
print("""
Suggested Power BI Visualizations:
-----------------------------------
1. KPI Cards:
   - Average Satisfaction Score
   - Total Employees
   - Attrition Rate
   - Average Performance Score

2. Bar Charts:
   - Performance Category vs Department
   - Attrition by Tenure

3. Line Graphs:
   - Engagement Index over time

4. Scatter Plot:
   - Performance Score vs Satisfaction Score

5. Slicers:
   - Department, Job Role, Gender, Performance Category
""")
