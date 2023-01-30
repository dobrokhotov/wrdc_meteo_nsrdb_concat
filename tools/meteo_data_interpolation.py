from datetime import timedelta
import pandas as pd
import numpy as np

def rp5_hour_interp_3(df):
    '''

    :param df: Rp5 DataFrame with 3 hour data
    :return: Rp5 DataFrame with 1 hour data
    '''

    # Set column Datetime for merging in the future
    df1 = df
    df1['Datetime'] = df1.index

    # Create two additional DataFrames for future interpolation
    df2 = pd.DataFrame()
    df2['Datetime'] = df1['Datetime'] + timedelta(hours=1)
    df3 = pd.DataFrame()
    df3['Datetime'] = df1['Datetime'] + timedelta(hours=2)

    # Merge DataFrames
    df = df1.merge(df2, on='Datetime', how='outer')
    df = df.merge(df3, on='Datetime', how='outer')
    df.index = df['Datetime']
    df = df.sort_index()

    # Linear interpolate for specific columns
    for i in ['T', 'P', 'U', 'Ff', 'N', 'Nh']:
        y = df[i]
        nans, x = nan_helper(y)
        y[nans] = np.interp(x(nans), x(~nans), y[~nans])

    # Forward fill interpolation for specific columns
    for i in ['Cl', 'Cm', 'Ch']:
        df[i] = df[i].fillna(method='ffill')

    df_hour = df

    return df_hour


def rp5_hour_interp_6(df):
    '''

    :param df: Rp5 DataFrame with 3 hour data
    :return: Rp5 DataFrame with 1 hour data
    '''

    # Set column Datetime for merging in the future
    df1 = df
    df1['Datetime'] = df1.index

    # Create two additional DataFrames for future interpolation
    df2 = pd.DataFrame()
    df2['Datetime'] = df1['Datetime'] + timedelta(hours=1)
    df3 = pd.DataFrame()
    df3['Datetime'] = df1['Datetime'] + timedelta(hours=2)
    df4 = pd.DataFrame()
    df4['Datetime'] = df1['Datetime'] + timedelta(hours=3)
    df5 = pd.DataFrame()
    df5['Datetime'] = df1['Datetime'] + timedelta(hours=4)
    df6 = pd.DataFrame()
    df6['Datetime'] = df1['Datetime'] + timedelta(hours=5)

    # Merge DataFrames
    df = df1.merge(df2, on='Datetime', how='outer')
    df = df.merge(df3, on='Datetime', how='outer')
    df = df.merge(df4, on='Datetime', how='outer')
    df = df.merge(df5, on='Datetime', how='outer')
    df = df.merge(df6, on='Datetime', how='outer')
    df.index = df['Datetime']
    df = df.sort_index()

    # Linear interpolate for specific columns
    for i in ['T', 'P', 'U', 'Ff', 'N', 'Nh']:
        y = df[i]
        nans, x = nan_helper(y)
        y[nans] = np.interp(x(nans), x(~nans), y[~nans])

    # Forward fill interpolation for specific columns
    for i in ['Cl', 'Cm', 'Ch']:
        df[i] = df[i].fillna(method='ffill')

    df_hour = df

    return df_hour


def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices of NaNs to 'equivalent' indices
    Example:
        >>> # linear interpolation of NaNs
        >>> nans, x= nan_helper(y)
        >>> y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    """

    return np.isnan(y), lambda z: z.to_numpy().nonzero()[0]