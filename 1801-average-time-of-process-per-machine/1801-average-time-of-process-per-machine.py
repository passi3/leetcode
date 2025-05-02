import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_time = activity[activity['activity_type'] == 'start'].rename(columns={'timestamp': 'start_time'})
    end_time = activity[activity['activity_type'] == 'end'].rename(columns={'timestamp': 'end_time'})
    merged_df = start_time[['machine_id', 'process_id', 'start_time']].merge(end_time[['machine_id', 'process_id', 'end_time']], on=['machine_id', 'process_id'])
    merged_df['process_time'] = merged_df['end_time'] - merged_df['start_time']
    merged_df = merged_df.groupby(['machine_id'])['process_time'].mean().round(3).reset_index(name='processing_time')
    return merged_df