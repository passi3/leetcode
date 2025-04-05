import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer[(customer['referee_id']!=2)|(customer['referee_id'].isnull())].reset_index()
    return customer[['name']]