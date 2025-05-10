import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    project = project.merge(employee[['employee_id', 'experience_years']], on='employee_id')
    project = project.groupby('project_id')['experience_years'].mean().round(2).reset_index(name='average_years')
    return project