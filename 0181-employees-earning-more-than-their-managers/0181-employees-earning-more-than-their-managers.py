import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, employee, 
            left_on="managerId", right_on="id",
            suffixes=("", "_manager"),
            how="inner"
            )
    result = merged[merged["salary"] > merged["salary_manager"]]
    result = result[["name"]].rename(columns={"name": "Employee"})

    return result