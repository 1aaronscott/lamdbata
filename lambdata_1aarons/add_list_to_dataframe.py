"""
Test file for functions to import
"""

import numpy as np

DF = pd.DataFrame([5, 8, 4])


def LIST_TO_SERIES_TO_COLUMN(list, df):
    """Takes a list and a dataframe, converts the list to a column, makes it the new rightmost column"""
    new_column = pd.Series((v[0] for v in list))
    # https://chrisalbon.com/python/data_wrangling/pandas_join_merge_dataframe/
    # https://stackoverflow.com/questions/21646791/convert-python-list-to-pandas-series
    return pd.concat([df, new_column], axis=1)
