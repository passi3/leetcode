import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    salary_filter_df = employees[employees['salary']<30000].dropna()
    manager_filter_df = salary_filter_df[~salary_filter_df['manager_id'].isin(employees['employee_id'])]
    return manager_filter_df[['employee_id']].sort_values(by='employee_id')