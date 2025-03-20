import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person[person.duplicated(['email'], keep=False)]
    return result[['email']].drop_duplicates()