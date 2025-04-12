import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars='product_id', value_vars=['store1', 'store2', 'store3'], value_name='price')
    products = products.dropna(subset=['price']).reset_index(drop=True)
    products = products.rename(columns={'variable': 'store'})
    return products