import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id']).sum('total_time').reset_index()
    result = result.rename(columns={'event_day': 'day'})
    return result[['day', 'emp_id', 'total_time']]