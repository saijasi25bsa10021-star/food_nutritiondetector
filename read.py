import pandas as pd

df = pd.read_csv(r"C:\Users\alkas\OneDrive\Desktop\food_project_final\daily_food_nutrition_dataset.csv",
                 on_bad_lines='skip')

print(df.head())
