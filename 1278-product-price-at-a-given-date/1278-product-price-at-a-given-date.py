import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    filtered = (
        products[products["change_date"] <= "2019-08-16"]
        .sort_values("change_date", ascending=False)
        .drop_duplicates("product_id")
    )

    result = (
        pd.DataFrame({"product_id": products["product_id"].unique()})
        .merge(filtered[["product_id", "new_price"]], on="product_id", how="left")
        .rename(columns={"new_price": "price"})
        .fillna(10)
    )

    return result