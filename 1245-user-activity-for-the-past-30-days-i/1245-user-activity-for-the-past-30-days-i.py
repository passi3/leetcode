import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('activity_date')['user_id'].nunique().reset_index(name='active_users').rename(columns={'activity_date': 'day'})
    activity = activity[(activity['day'] >= '2019-06-28') & (activity['day'] <= '2019-07-27')]
    return activity