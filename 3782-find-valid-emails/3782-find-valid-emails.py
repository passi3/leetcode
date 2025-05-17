import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
    valid_users = users[users['email'].str.match(pattern)]
    return valid_users.sort_values('user_id').reset_index(drop=True)