import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    unique_p_id = set(tree['p_id'].dropna().drop_duplicates())
    tree['type'] = tree.apply(lambda x: 'Root' if pd.isna(x['p_id']) else 'Leaf' if x['id'] not in unique_p_id else 'Inner', axis=1)
    return tree[['id', 'type']]