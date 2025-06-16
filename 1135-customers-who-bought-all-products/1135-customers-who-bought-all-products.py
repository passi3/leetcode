import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    target_product = set(product['product_key'])
    customer = customer.groupby('customer_id')['product_key'].agg(set).reset_index()
    customer = customer[customer['product_key'].apply(lambda x: target_product.issubset(x))]
    return customer[['customer_id']]