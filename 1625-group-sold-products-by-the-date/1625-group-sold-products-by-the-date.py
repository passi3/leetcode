import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(['sell_date', 'product']).sort_values(by=['sell_date', 'product'], ascending=True)
    num_sold = activities.groupby('sell_date').size().reset_index(name='num_sold')
    products = activities.groupby('sell_date')['product'].agg(','.join).reset_index(name='products')
    result = num_sold.merge(products, on='sell_date')
    return result