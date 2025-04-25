import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    dep_count = employee.groupby('employee_id').size().reset_index(name='count')
    employee = employee.merge(dep_count, on='employee_id')
    employee = employee[(employee['primary_flag']=='Y') | (employee['count']==1)]
    return employee[['employee_id', 'department_id']]