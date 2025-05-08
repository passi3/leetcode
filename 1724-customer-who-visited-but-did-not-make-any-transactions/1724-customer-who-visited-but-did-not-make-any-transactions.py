import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    visits = visits[~visits['visit_id'].isin(transactions['visit_id'])]
    visits = visits.groupby('customer_id').size().reset_index(name='count_no_trans')
    return visits