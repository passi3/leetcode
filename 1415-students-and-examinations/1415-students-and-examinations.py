import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)
    examinations = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    students = students.merge(examinations, on=['student_id', 'subject_name'], how='left').sort_values(by=['student_id', 'subject_name'])
    students['attended_exams'] = students['attended_exams'].fillna(0)
    return students