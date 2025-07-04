import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    login_df = activity.groupby("player_id")["event_date"].min().reset_index(name="first_login")
    logged_dates = activity.groupby("player_id")["event_date"].apply(set).reset_index()
    login_df = login_df.merge(logged_dates, on="player_id", how="left")
    login_df["next_date"] = login_df["first_login"] + pd.Timedelta(days=1)
    login_df["log_conse_first_login"] = login_df.apply(lambda x: x["next_date"] in x["event_date"], axis=1)
    return pd.DataFrame({
        "fraction": [round(login_df["log_conse_first_login"].mean(), 2)]
    })
    