import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['previous'] = weather['recordDate'] - pd.Timedelta(days=1)
    weather = weather.merge(
        weather[['recordDate', 'temperature']],
        left_on='previous',
        right_on='recordDate',
        suffixes=('', '_previous')
    )
    result = weather[weather['temperature'] > weather['temperature_previous']]
    return result[['id']]