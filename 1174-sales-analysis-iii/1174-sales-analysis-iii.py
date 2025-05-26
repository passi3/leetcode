import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.groupby('product_id')['sale_date'].agg(['min', 'max']).query('"2019-01-01"<=min<=max<="2019-03-31"').reset_index()
    return product[product['product_id'].isin(sales['product_id'])][['product_id', 'product_name']]