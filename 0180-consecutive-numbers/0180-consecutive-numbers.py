import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values("id")
    logs["prev"] = logs["num"].shift()
    logs["next"] = logs["num"].shift(-1)
    logs["consecutive"] = (logs["prev"] == logs["num"]) & (logs["num"] == logs["next"])
    result = logs[logs["consecutive"]][["num"]].drop_duplicates()
    result.columns = ["ConsecutiveNums"]
    return result