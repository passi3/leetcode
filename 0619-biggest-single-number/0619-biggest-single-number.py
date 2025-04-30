import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = (
        my_numbers
        .value_counts()
        .reset_index(name='count')
        .query('count == 1')
        .max(numeric_only=True)
        .to_frame().T[['num']]
    )

    return result if not result['num'].isna().any() else pd.DataFrame({'num': [None]})