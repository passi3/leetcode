import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product = product.merge(sales[['product_id', 'year', 'price']], on='product_id')
    return product[['product_name', 'year', 'price']]