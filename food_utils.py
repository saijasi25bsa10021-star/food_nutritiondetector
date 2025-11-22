import pandas as pd

class FoodUtil:
    
    def __init__(self, df):
        """Store the dataset for lookup use."""
        self.df = df

    def get_nutrition(self, food_name):
        """
        Searches the dataset for a food item.
        Returns nutrition info as dictionary.
        """

        if self.df is None:
            return None
        
        # Match food name (case-insensitive)
        match = self.df[self.df['Food'].str.contains(food_name, case=False, na=False)]

        if match.empty:
            return None

        # Return the first matched row as a dictionary
        return match.iloc[0].to_dict()

    def list_foods(self):
        """Return a list of all food names in the dataset."""
        if self.df is None:
            return []
        return self.df['Food'].dropna().unique().tolist()
