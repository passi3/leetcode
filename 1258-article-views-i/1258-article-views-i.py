import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']].drop_duplicates(['author_id'])['author_id'].reset_index()
    views = views.rename(columns={'author_id': 'id'}).sort_values(by='id')
    return views[['id']]