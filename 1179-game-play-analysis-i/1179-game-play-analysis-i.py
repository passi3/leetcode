import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(['player_id', 'event_date'], inplace=True)
    activity = activity.groupby('player_id').first().reset_index()
    activity = activity.rename({'event_date': 'first_login'}, axis=1)
    return activity[['player_id', 'first_login']]