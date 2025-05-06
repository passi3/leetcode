import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    department = department.pivot(values='revenue', index='id', columns='month')
    department = department.reindex(columns = months).rename(columns={m: f"{m}_Revenue" for m in months}).reset_index()
    return department