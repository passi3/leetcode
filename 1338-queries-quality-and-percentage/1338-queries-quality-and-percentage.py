import pandas as pd

import pandas as pd
 
def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position'] + 1e-6	
    queries['poor_query_percentage'] = queries['rating'].apply(lambda x: 100 if x < 3 else 0)
    return queries.groupby('query_name').agg({'quality':'mean', 'poor_query_percentage':'mean'}).round(2).reset_index()
