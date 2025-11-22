import pandas as pd

def load_dataset():
    try:
        df = pd.read_csv("daily_food_nutrition_dataset.csv", 
                         engine="python", 
                         on_bad_lines="skip")
        print("File loaded successfully! ")
        return df
    except Exception as e:
        print("Error loading file:", e)
        print("\nIMPORTANT: Make sure 'daily_food_nutrition_dataset.csv' is in the SAME folder.\n")
        return None

df = load_dataset()

if df is not None:
    print(df.head())



