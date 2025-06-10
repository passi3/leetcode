import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    recent_reviews = (
        performance_reviews
        .sort_values(['employee_id', 'review_date'])
        .groupby('employee_id')
        .tail(3)
    )

    def check_increase(df):
        if len(df) < 3:
            return None
        ratings = df['rating'].values
        if ratings[0] < ratings[1] < ratings[2]:
            return ratings[2] - ratings[0]
        return None

    improvement = (
        recent_reviews
        .groupby('employee_id')
        .apply(check_increase)
        .dropna()
        .reset_index(name='improvement_score')
    )

    result = (
        improvement
        .merge(employees, on='employee_id')
        .sort_values(['improvement_score', 'name'], ascending=[False, True])
        [['employee_id', 'name', 'improvement_score']]
    )

    return result