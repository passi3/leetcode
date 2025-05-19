import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    managers = employees.groupby('reports_to')['age'].agg(
        reports_count='count',
        average_age='mean'
    ).reset_index(names='employee_id')
    managers['average_age'] = (managers['average_age'] + 0.5).astype(int)
    employees = employees.merge(managers, on='employee_id').drop(columns=['reports_to', 'age'])
    return employees.sort_values(by='employee_id')