import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    units_sold = units_sold.merge(prices, how='left', on='product_id')
    units_sold = units_sold[
        (units_sold['purchase_date'] >= units_sold['start_date']) & 
        (units_sold['purchase_date'] <= units_sold['end_date'])
        ]
    units_sold['sum_price'] = units_sold['units'] * units_sold['price']
    units_sold = units_sold.groupby('product_id').agg(
        total_units = ('units', 'sum'),
        total_price = ('sum_price', 'sum')
    ).reset_index()
    units_sold['average_price'] = (units_sold['total_price'] / units_sold['total_units']).round(2)
    prices = prices[['product_id']].drop_duplicates()
    return prices.merge(units_sold[['product_id', 'average_price']], on='product_id', how='left').fillna(0)