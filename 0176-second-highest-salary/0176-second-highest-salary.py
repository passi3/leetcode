import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee["salary"].drop_duplicates().sort_values(ascending=0)
    secondSalary = employee.iloc[1] if len(employee) >=2 else None
    return pd.DataFrame({"SecondHighestSalary": [secondSalary]})