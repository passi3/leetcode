import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    rides = rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    users = users.merge(rides, left_on='id', right_on='user_id', how='left').fillna(0)
    return users[['name', 'travelled_distance']].sort_values(['travelled_distance', 'name'], ascending=[0, 1])