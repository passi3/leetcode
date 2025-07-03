import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    user = movie_rating.groupby("user_id").size().reset_index(name="count")
    user = user.merge(users).sort_values(["count", "name"], ascending=[False, True])
    user = user["name"].iloc[0]
    
    movie = movie_rating[(movie_rating["created_at"].dt.year==2020) & (movie_rating["created_at"].dt.month==2)]
    movie = movie.groupby("movie_id")["rating"].mean().reset_index(name="rating")
    movie = movie.merge(movies).sort_values(["rating", "title"], ascending=[False, True])
    movie = movie["title"].iloc[0]
    
    return pd.DataFrame({"results": [user, movie]})