import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    confirmations = confirmations.groupby("user_id")['action'].agg(
        confirmed = lambda x: (x=="confirmed").sum(),
        total = "count"
    ).reset_index()
    confirmations["confirmation_rate"] = round(confirmations["confirmed"] / confirmations["total"], 2)
    signups = signups.merge(confirmations, on="user_id", how="left").fillna(0)
    return signups[["user_id", "confirmation_rate"]]