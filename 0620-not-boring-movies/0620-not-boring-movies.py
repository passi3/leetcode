import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[(cinema['description']!='boring') & (cinema['id']%2==1)].sort_values(by='rating', ascending=False)
    return cinema