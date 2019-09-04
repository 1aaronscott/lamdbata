"""
Test file for functions to import
"""
import pandas as pd
import numpy as np

DF = pd.DataFrame([5, 8, 4])


def TVT_split(df):
    """Takes a dataframe as input and outputs three numpy arrays: 60% train, 20% validate, 20% test"""
    # improvements: return as dataframes, accept the fractions as arguments
    train, validate, test = np.split(
        df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
    # https://datascience.stackexchange.com/questions/15135/train-test-validation-set-splitting-in-sklearn
    return train, validate, test
