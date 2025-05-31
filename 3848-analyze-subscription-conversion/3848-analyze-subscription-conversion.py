import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)
    def findMean(activity, avg):
        return (user_activity[user_activity.activity_type == activity]
                .groupby('user_id').mean('activity_duration')
                .apply(round2).reset_index()
                .rename(columns={'activity_duration':avg}))
    return pd.merge(findMean('free_trial', 'trial_avg_duration'),
                    findMean('paid', 'paid_avg_duration'), on='user_id')