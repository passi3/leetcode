import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'].dt.year==2020) & (orders['order_date'].dt.month==2)].groupby('product_id').sum('unit').reset_index()
    orders = orders[orders['unit']>=100].merge(products, on='product_id')
    return orders[['product_name', 'unit']]