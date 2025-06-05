import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.groupby('transaction_date')['amount'].agg(
        odd_sum = lambda x: x[x%2==1].sum(),
        even_sum = lambda x: x[x%2==0].sum()
    ).reset_index()
    return transactions.sort_values('transaction_date')