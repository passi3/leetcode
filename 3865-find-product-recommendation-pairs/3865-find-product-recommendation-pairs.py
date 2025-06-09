import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    product_purchases = product_purchases.merge(product_purchases, on='user_id')
    product_purchases = product_purchases[product_purchases['product_id_x'] < product_purchases['product_id_y']]
    product_pair = product_purchases.groupby(['product_id_x', 'product_id_y'])['user_id'].nunique().reset_index(name='customer_count')
    product_pair = product_pair[product_pair['customer_count']>=3]
    product_info1 = product_info.rename(columns={'product_id': 'product_id_x', 'category': 'product1_category'})
    product_info2 = product_info.rename(columns={'product_id': 'product_id_y', 'category': 'product2_category'})

    product_pair = product_pair.merge(product_info1[['product_id_x', 'product1_category']], on='product_id_x', how='left')\
    .merge(product_info2[['product_id_y', 'product2_category']], on='product_id_y', how='left')

    product_pair = product_pair.sort_values(['customer_count', 'product_id_x', 'product_id_y'], ascending=[0, 1, 1])

    product_pair = product_pair.rename(columns={
        'product_id_x': 'product1_id',
        'product_id_y': 'product2_id'
    })

    return product_pair[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']]