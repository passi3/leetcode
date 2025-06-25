import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby("departmentId")["salary"].max().reset_index()
    result = employee.merge(max_salary, on="departmentId", suffixes=("", "_max"))
    result = result[result["salary"]==result["salary_max"]]
    result = result.merge(department, left_on="departmentId", right_on="id")
    return result[["name_y", "name_x", "salary"]].rename(columns={
        "name_y": "Department",
        "name_x": "Employee",
        "salary": "Salary"
    })