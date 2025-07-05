import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False).tolist()

    if N > 0 and N <= len(salaries):
        nth_salary = salaries[N - 1]
    else:
        nth_salary = None

    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary]})