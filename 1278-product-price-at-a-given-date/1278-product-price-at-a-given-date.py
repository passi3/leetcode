import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    product_ids = products["product_id"].unique()
    products = products.sort_values("change_date", ascending=False)
    products = products[products["change_date"] <= "2019-08-16"].drop_duplicates("product_id")
    result = pd.DataFrame({
        "product_id": product_ids,
    })
    result = result.merge(products[["product_id", "new_price"]], on="product_id", how="left").rename(columns={"new_price": "price"}).fillna(10)
    return result