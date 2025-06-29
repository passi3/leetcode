import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores[scores.duplicated(subset=["student_id", "subject"], keep=False)].sort_values(
        ["student_id", "subject", "exam_date"]
    )
    result = scores.groupby(["student_id", "subject"])["score"].agg(
        first_score = lambda x: x.iloc[0],
        latest_score = lambda x: x.iloc[-1]
    ).reset_index()
    result = result[result["first_score"] < result["latest_score"]]
    return result