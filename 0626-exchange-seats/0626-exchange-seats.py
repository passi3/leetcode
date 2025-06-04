import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)
    if n <= 1:
        return seat

    seat = seat.sort_values('id')
    odd_seat = seat[seat['id']%2 == 1]
    even_seat = seat[seat['id']%2 == 0]

    odd_seat['id'] = odd_seat['id'] + 1
    even_seat['id'] = even_seat['id'] - 1

    if n%2 == 1:
        odd_seat['id'].values[-1] = n
    
    new_seat = pd.concat([odd_seat, even_seat], axis=0, ignore_index=True)
    return new_seat.sort_values('id')
         