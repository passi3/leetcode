import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(salaries, how='outer', on='employee_id')
    return employees[(employees['name'].isnull()) | (employees['salary'].isnull())][['employee_id']].sort_values(by='employee_id', ascending=True)