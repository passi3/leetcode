import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby(by='customer_number').count().reset_index()
    max_order = orders['order_number'].max()
    return orders[orders['order_number']==max_order][['customer_number']]