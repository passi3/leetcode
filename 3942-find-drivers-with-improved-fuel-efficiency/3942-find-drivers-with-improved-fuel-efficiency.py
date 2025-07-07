import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
	trips['trip_date'] = pd.to_datetime(trips['trip_date'])
	def calc_half(x, half):
		if half == 0:
			x = x[trips['trip_date'].dt.month <= 6]
		else:
			x = x[trips['trip_date'].dt.month > 6]
		return (x / trips['fuel_consumed']).mean()
	df = trips.groupby(by='driver_id', as_index=False).agg(
		first_half_avg=('distance_km', lambda x: calc_half(x, 0)), 
		second_half_avg=('distance_km', lambda x: calc_half(x, 1)),
	)
	df['efficiency_improvement'] = df['second_half_avg'] - df['first_half_avg']
	df = df[df['efficiency_improvement'] > 0]
	df['first_half_avg'] = df['first_half_avg'].round(2)
	df['second_half_avg'] = df['second_half_avg'].round(2)
	df['efficiency_improvement'] = df['efficiency_improvement'].round(2)
	df = drivers.merge(df, on='driver_id')
	return df.sort_values(by=['efficiency_improvement', 'driver_name'], ascending=[False, True])