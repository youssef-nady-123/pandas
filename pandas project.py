import pandas as pd
import numpy as np

# =============================
# Step 1: Load Data
# =============================
df = pd.read_csv('pandas_practice_dataset.csv')

# =============================
# Step 2: Data Cleaning
# =============================

# Fill missing salary with mean
if 'salary' in df.columns:
    df['salary'].fillna(df['salary'].mean(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Strip spaces from names and uppercase departments
df['name'] = df['name'].str.strip()
df['department'] = df['department'].str.upper()

# =============================
# Step 3: Data Transformation
# =============================

# Add bonus column (10% of salary)
df['bonus'] = df['salary'] * 0.10

# Add salary after bonus column
df['salary_after_bonus'] = df['salary'] + df['bonus']

# Rank employees by salary
df['salary_rank'] = df['salary'].rank(ascending=False)

# Filter: IT employees with salary > average salary
average_salary = df['salary'].mean()
it_high_salary = df[(df['department'] == 'IT') & (df['salary'] > average_salary)]

# =============================
# Step 4: Aggregation & Grouping
# =============================

# Average salary per department
avg_salary_dep = df.groupby('department')['salary'].mean()

# Count employees per department
count_emp_dep = df.groupby('department')['id'].count()

# Multi-aggregation: average and max salary per department
multi_agg_dep = df.groupby('department')['salary'].agg(['mean','max'])

# =============================
# Step 5: Pivot Table
# =============================

pivot_salary_dep = pd.pivot_table(df, values='salary', index='department', aggfunc='mean')

# =============================
# Step 6: Merge with extra info
# =============================
extra_info = pd.DataFrame({
    'id':[1,2,3,4,5],
    'extra_bonus':[100,200,150,120,180]
})
df = pd.merge(df, extra_info, on='id', how='left')

# =============================
# Step 7: Outlier Removal
# =============================
df = df[df['salary'] < 9000]  # remove extreme salaries

# =============================
# Step 8: Working with Dates (example)
# =============================
df['join_date'] = pd.date_range(start='2020-01-01', periods=len(df), freq='M')
df['join_year'] = df['join_date'].dt.year
df['join_month'] = df['join_date'].dt.month

# =============================
# Step 9: Save Cleaned & Transformed Data
# =============================
df.to_csv('cleaned_transformed_data.csv', index=False)

# =============================
# =============================
# Print Summary Outputs
# =============================
print("--- Average Salary per Department ---")
print(avg_salary_dep)
print("\n--- Employee Count per Department ---")
print(count_emp_dep)
print("\n--- Multi-Aggregation (Mean & Max Salary) ---")
print(multi_agg_dep)
print("\n--- IT Employees with Salary > Average ---")
print(it_high_salary)
print("\n--- Pivot Table (Average Salary by Department) ---")
print(pivot_salary_dep)
print("\n--- Top 5 Employees After Cleaning & Transformation ---")
print(df.head())
