def __init__(self, df):
    """
    Basic init — storing the dataframe.
    I *think* this is the right place to do it… unless there's some fancy pattern I'm missing.
    Anyway, leaving it simple.
    """
    # NOTE: Should probably check df type but I'm trusting whoever calls this.
    self.df = df  
    self._last_query = None   # not used yet, but maybe someday? idk
    # print("FoodUtil initialized")  # debug thing I might use again


def get_nutrition(self, food_name):
    """
    Look up nutrition for something the user typed.
    Very rough matching — but hey, it gets the job done.
    """

    # sanity check — learned the hard way after forgetting df once
    if self.df is None:
        # FIXME: maybe raise ValueError in the future?
        return None

    # I had plans to preprocess food_name but got distracted
    query_text = str(food_name).strip()
    self._last_query = query_text  # just saving it because why not

    try:
        # basic substring match — surprisingly effective
        results = self.df[
            self.df['Food'].str.contains(
                query_text,
                case=False,
                na=False
            )
        ]
    except Exception as oops:
        # leaving this here for when I inevitably break something
        print("String matching exploded for some reason:", oops)
        return None

    if results.empty:
        # No match? oh well
        return None

    # TODO: let user choose? multi-match UI someday??
    chosen = results.iloc[0]

    # Convert series to dict — easy, clean, reliable
    data_dict = chosen.to_dict()

    # Might add some postprocessing here later... maybe
    return data_dict


def list_foods(self):
    """
    Returns list of foods from the dataframe.
    Nothing tricky — unless 'Food' column goes missing (pls don't happen).
    """

    if self.df is None:
        return []

    # pulling column — I probably shouldn't assume it exists but here we are
    col = self.df['Food']

    # removing NaNs because printing 'nan' drove me insane once
    cleaned_up = col.dropna()

    # unique so we don't get duplicates — learned that trick way after I should have
    foods_array = cleaned_up.unique()

    # listify — Python should honestly have a better word for this
    foods_list = list(foods_array)

    # random thought: sorting might be nice, but unpredictable ordering is kinda charming
    # TODO: maybe add option: sort=True
    return foods_list

