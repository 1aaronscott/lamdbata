"""
Test file for functions to import
"""
import pandas as pd
import numpy as np

DF = pd.DataFrame([5,8,4])

def TVT_split(df):
    train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
    # https://datascience.stackexchange.com/questions/15135/train-test-validation-set-splitting-in-sklearn
    return train, validate, test

def LIST_TO_SERIES_TO_COLUMN(list, df):
    new_column = pd.Series( (v[0] for v in list) )
    # https://chrisalbon.com/python/data_wrangling/pandas_join_merge_dataframe/
    # https://stackoverflow.com/questions/21646791/convert-python-list-to-pandas-series
    return pd.concat([df, new_column], axis=1)
