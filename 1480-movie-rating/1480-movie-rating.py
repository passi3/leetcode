import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    grouped_user_rating = movie_rating.groupby("user_id")["rating"].size().reset_index(name="reviews")
    users = users.merge(grouped_user_rating, on="user_id", how="left")
    movie_rating = movie_rating[(movie_rating["created_at"].dt.year==2020) & (movie_rating["created_at"].dt.month==2)]
    grouped_movie_rating = movie_rating.groupby("movie_id")["rating"].mean().reset_index(name="avg_rating")
    movies = movies.merge(grouped_movie_rating, on="movie_id", how="left")
    most_rating_movie = movies.sort_values(["avg_rating", "title"], ascending=[False, True]).iloc[0]["title"]
    most_reviewer = users.sort_values(["reviews", "name"], ascending=[False, True]).iloc[0]["name"]
    return pd.DataFrame({
        "results": [most_reviewer, most_rating_movie]
    })