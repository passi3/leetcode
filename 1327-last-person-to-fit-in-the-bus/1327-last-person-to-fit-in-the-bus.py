import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values('turn')
    queue['total_weight'] = queue['weight'].cumsum()
    return queue[queue['total_weight']<=1000].tail(1)[['person_name']]