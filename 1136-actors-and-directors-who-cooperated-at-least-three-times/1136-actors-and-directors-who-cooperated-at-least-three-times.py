import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperated')
    return actor_director[actor_director['cooperated']>=3][['actor_id', 'director_id']]