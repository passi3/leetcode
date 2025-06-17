import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["category"] = accounts["income"].apply(lambda x: "Low Salary" if x < 20000 else ("High Salary" if x>50000 else "Average Salary"))
    accounts = accounts.groupby("category").size().reset_index(name="accounts_count")
    categories = pd.DataFrame({
        "category": ["Low Salary", "Average Salary", "High Salary"]
    })
    categories = categories.merge(accounts, how="left", on="category").fillna(0)
    return categories