import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders["order_date"].dt.year==2019].groupby("buyer_id").size().reset_index(name="orders_in_2019")
    result = users[["user_id", "join_date"]].merge(
        orders, how="left", left_on="user_id", right_on="buyer_id"
        ).fillna(0)
    return result[["user_id", "join_date", "orders_in_2019"]].rename(
        columns={"user_id": "buyer_id"}
    )