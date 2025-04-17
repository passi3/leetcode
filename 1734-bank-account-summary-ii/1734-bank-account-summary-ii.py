import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    sum_amount = transactions.groupby('account')['amount'].sum().reset_index(name='balance')
    users = users.merge(sum_amount, on='account')
    return users[users['balance']>10000][['name', 'balance']]