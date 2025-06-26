import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values(["customer_id", "order_date"]).drop_duplicates(subset="customer_id", keep="first")
    delivery["immediate"] = (delivery["order_date"]==delivery["customer_pref_delivery_date"]).astype(int)
    result = pd.DataFrame({
        "immediate_percentage": [round(delivery["immediate"].mean()*100, 2)]
    })
    return result