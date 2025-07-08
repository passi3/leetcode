import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    covid_tests["test_date"] = pd.to_datetime(covid_tests["test_date"])
    positive = covid_tests[covid_tests["result"]=="Positive"]
    first_positive = positive.groupby("patient_id")["test_date"].min().reset_index()
    first_positive.columns = ["patient_id", "first_positive"]

    negative = covid_tests[covid_tests["result"]=="Negative"]

    merged = first_positive.merge(negative, on="patient_id")
    true_positive = merged[merged["test_date"] > merged["first_positive"]]

    first_negative = true_positive.groupby("patient_id")["test_date"].min().reset_index()
    first_negative.columns = ["patient_id", "first_negative"]

    result = first_positive.merge(first_negative, on="patient_id")
    result["recovery_time"] = (result["first_negative"] - result["first_positive"]).dt.days
    result = patients.merge(result[["patient_id", "recovery_time"]], on="patient_id")
    return result.sort_values(by=["recovery_time", "patient_name"], ascending=[True, True])