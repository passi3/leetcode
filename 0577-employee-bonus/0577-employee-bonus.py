import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(bonus, on='empId', how='left')
    employee = employee[(employee['bonus'] < 1000)|(employee['bonus'].isnull())]
    return employee[['name', 'bonus']]