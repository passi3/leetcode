import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['season'] = sales['sale_date'].apply(get_season)
    sales['total_price'] = sales['quantity'] * sales['price']
    sales = sales.merge(products[['product_id', 'category']], on='product_id', how='left')
    sales = sales.groupby(['season', 'category']).agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('total_price', 'sum')
    ).reset_index()
    sales = sales.sort_values(['season', 'total_quantity', 'total_revenue'], ascending=[1, 0, 0]).drop_duplicates(['season'])
    return sales

def get_season(x):
    if x.month in [3, 4, 5]:
        return 'Spring'
    elif x.month in [6, 7, 8]:
        return 'Summer'
    elif x.month in [9, 10, 11]:
        return 'Fall'
    elif x.month in [12, 1, 2]:
        return 'Winter'
    else:
        raise ValueError('invalid date')