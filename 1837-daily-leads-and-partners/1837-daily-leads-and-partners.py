import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result1 = daily_sales.groupby(['date_id', 'make_name'])['lead_id'].nunique().reset_index(name='unique_leads')
    result2 = daily_sales.groupby(['date_id', 'make_name'])['partner_id'].nunique().reset_index(name='unique_partners')
    return result1.merge(result2, on=['date_id', 'make_name'], how='inner')