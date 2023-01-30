import gzip
import pandas as pd
import numpy as np
from datetime import timedelta
from tools import MeteoDicts

class MeteoReader:

    def __init__(self, folder):
        self.folder = folder

    def rp5_data_reader(self):
        '''

        :param path:  path to meteodata file source
        :return: return pandas DataFrame with meteodata
        '''

        csv_file = gzip.open(self.folder, 'rb')
        # Read meteodata file from path
        df = pd.read_csv(csv_file, skiprows=6, sep=";", index_col=False, error_bad_lines=False)

        # Set datetime as an index with Datetime type
        df.index = pd.to_datetime(df.iloc[:, 0], dayfirst=True)

        # Replace columns according dicts from DictsRp5
        df['N'] = df['N'].replace(MeteoDicts.N_DICT)
        df['Nh'] = df['Nh'].replace(MeteoDicts.N_DICT)
        df['Cl'] = df['Cl'].replace(MeteoDicts.CL_DICT)
        df['Cm'] = df['Cm'].replace(MeteoDicts.CM_DICT)
        df['Ch'] = df['Ch'].replace(MeteoDicts.CH_DICT)
        df['RRR'] = df['RRR'].replace(MeteoDicts.RRR_DICT)

        # Filter data for Nh where N < Nh
        df['N_delta'] = df['N'] - df['Nh']
        df['N_delta'] = df['N_delta'].apply(lambda x: x if x < 0 else 0)
        df['Nh'] = df['Nh'] + df['N_delta']

        self.df = df
        return self.df


    def rp5_hour_interp_3(self):
        '''

        :param df: Rp5 DataFrame with 3 hour data
        :return: Rp5 DataFrame with 1 hour data
        '''

        # Set column Datetime for merging in the future
        df1 = self.df
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
            nans, x = self.nan_helper(y)
            y[nans] = np.interp(x(nans), x(~nans), y[~nans])

        # Forward fill interpolation for specific columns
        for i in ['Cl', 'Cm', 'Ch']:
            df[i] = df[i].fillna(method='ffill')

        self.df_hour = df

        return self.df_hour

    def rp5_hour_interp_3(self):
        '''

        :param df: Rp5 DataFrame with 3 hour data
        :return: Rp5 DataFrame with 1 hour data
        '''

        # Set column Datetime for merging in the future
        df1 = self.df
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
            nans, x = self.nan_helper(y)
            y[nans] = np.interp(x(nans), x(~nans), y[~nans])

        # Forward fill interpolation for specific columns
        for i in ['Cl', 'Cm', 'Ch']:
            df[i] = df[i].fillna(method='ffill')

        self.df_hour = df

        return self.df_hour

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

if __name__ == '__main__':

    folder = 'D:/DATA/IT-BCi/Meteo/16289.01.05.2017.31.10.2017.1.0.0.en.utf8.00000000.csv.gz'

    meteo_reader = MeteoReader(folder=folder)
    meteo_reader.rp5_data_reader()
    df = meteo_reader.rp5_hour_interp()
    print (df)
