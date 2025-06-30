import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_year_df = sales.groupby("product_id")["year"].min().reset_index()
    first_year_df.rename(columns={"year": "first_year"}, inplace=True)
    sales = sales.merge(first_year_df, on="product_id")
    result = sales[sales["year"] == sales["first_year"]][["product_id", "first_year", "quantity", "price"]]

    return result