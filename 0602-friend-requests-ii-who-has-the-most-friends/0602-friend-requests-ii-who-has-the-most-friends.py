import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # print(dir(pd.DataFrame))
    # print(help(pd.DataFrame.melt))
    result = request_accepted.melt(value_vars=["requester_id", "accepter_id"]).rename(columns={"value": "id"})
    result = result.groupby("id").size().reset_index(name="num")
    return result[result["num"] == result["num"].max()]