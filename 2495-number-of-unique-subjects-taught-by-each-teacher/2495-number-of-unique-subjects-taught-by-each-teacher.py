import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.drop_duplicates(subset=['teacher_id', 'subject_id'])
    teacher = teacher.groupby('teacher_id').size().reset_index(name='cnt')
    return teacher[['teacher_id', 'cnt']]