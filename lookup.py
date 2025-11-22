import pandas as pd

def get_nutrition(food_name):
    try:
        df = pd.read_csv("daily_food_nutrition_dataset.csv", engine="python")
    except Exception as e:
        print("Error loading dataset:", e)
        return None

    # Search the food item
    match = df[df['Food'].str.contains(food_name, case=False, na=False)]

    if match.empty:
        return None

    return match.iloc[0].to_dict()
