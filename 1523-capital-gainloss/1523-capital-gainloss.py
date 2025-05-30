import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks = stocks.groupby('stock_name').apply(lambda x: np.where(x['operation'] == 'Buy', -x['price'], x['price']).sum()).reset_index(name='capital_gain_loss')
    return stocks