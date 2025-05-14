import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    n_users = users['user_id'].nunique()
    register = register.groupby('contest_id').size().reset_index(name='cnt')
    register['percentage'] = (100 * register['cnt'] / n_users).round(2)
    return register[['contest_id', 'percentage']].sort_values(['percentage', 'contest_id'], ascending=[0, 1])