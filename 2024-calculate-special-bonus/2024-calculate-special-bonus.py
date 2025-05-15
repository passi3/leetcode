import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(employees['employee_id']%2 == 1) & (~employees['name'].str.startswith('M'))]['salary']
    return employees[['employee_id', 'bonus']].fillna(0).sort_values(by='employee_id')