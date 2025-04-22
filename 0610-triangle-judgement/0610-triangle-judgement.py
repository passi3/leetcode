import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def is_triangle(row):
        segments = sorted([row['x'], row['y'], row['z']])
        return 'Yes' if segments[0] + segments[1] > segments[2] else 'No'

    triangle['triangle'] = triangle.apply(is_triangle, axis=1)
    return triangle