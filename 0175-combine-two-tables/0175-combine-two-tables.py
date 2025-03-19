import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person[['personId','firstName', 'lastName']], address[['personId','city', 'state']], how='left', on='personId')
    return result.drop(columns=['personId'])