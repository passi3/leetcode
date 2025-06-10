import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    hash_table = {}
    target_employees = performance_reviews.groupby('employee_id')['rating'].count().loc[lambda x: x>=3].index
    performance_reviews = performance_reviews[performance_reviews['employee_id'].isin(target_employees)].sort_values(['employee_id', 'review_date'])
    for target_employee in target_employees:
        ratings = performance_reviews[performance_reviews['employee_id'] == target_employee]['rating'].tolist()
        if ratings[-3] < ratings[-2] < ratings[-1]:
            hash_table[target_employee] = ratings[-1] - ratings[-3]
    
    result = pd.DataFrame(list(hash_table.items()), columns=['employee_id', 'improvement_score'])
    result = result.merge(employees, on='employee_id', how='left').sort_values(['improvement_score', 'name'], ascending=[0, 1])
    return result[['employee_id', 'name', 'improvement_score']]