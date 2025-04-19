import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[logins['time_stamp'].dt.year == 2020].sort_values(['user_id', 'time_stamp'], ascending=[1, 0]).drop_duplicates('user_id', keep='first')
    logins = logins.rename(columns={'time_stamp': 'last_stamp'})
    return logins