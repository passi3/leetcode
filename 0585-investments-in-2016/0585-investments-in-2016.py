import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    case1 = insurance["tiv_2015"].duplicated(keep=False)
    case2 = insurance.duplicated(subset=["lat", "lon"], keep=False)
    insurance = insurance[case1 & ~case2]
    result = round(insurance["tiv_2016"].sum(), 2)
    return pd.DataFrame({
        "tiv_2016": [result]
    })