import os
import pandas as pd
import functools as ft

from tools import MeteoReader
from tools import meteo_data_interpolation

wrdc_path = 'F:/SCIENCE 2023/Radiation Models Effiency/WRDC Data/Fukuoka/fukuoka.csv'
meteo_path_1 = 'F:/SCIENCE 2023/Radiation Models Effiency/rp5 Data/Fukuoka/47807.01.02.2005.31.12.2015.1.0.0.en.utf8.00000000.csv.gz'
meteo_path_2 = 'F:/SCIENCE 2023/Radiation Models Effiency/rp5 Data/Fukuoka/47807.01.01.2016.31.12.2020.1.0.0.en.utf8.00000000.csv.gz'
nsrdb_path = 'F:/SCIENCE 2023/Radiation Models Effiency/NSRDB Data/Fukuoka/'
res_path_xls = 'F:/SCIENCE 2023/Radiation Models Effiency/Results/fukuoka_all.xlsx'
res_path_csv = 'F:/SCIENCE 2023/Radiation Models Effiency/Results/fukuoka_all.csv'

#WRDC DATA HANDLE
df_wrdc = pd.read_csv(wrdc_path, index_col=0, parse_dates=True)
df_wrdc['Datetime'] = df_wrdc.index
df_wrdc['glo'] = pd.to_numeric(df_wrdc['glo'], errors='coerce')
df_wrdc['dif'] = pd.to_numeric(df_wrdc['dif'], errors='coerce')
df_wrdc['dir'] = pd.to_numeric(df_wrdc['dir'], errors='coerce')
df_wrdc['glo'] = df_wrdc['glo'].apply(lambda x: x*2.78) # from J cm2 Hour into W m2
df_wrdc['dif'] = df_wrdc['dif'].apply(lambda x: x*2.78) # from J cm2 Hour into W m2
df_wrdc['dir'] = df_wrdc['dir'].apply(lambda x: x*2.78) # from J cm2 Hour into W m2

#NSRDB DATA HANDLE
for i in range(0, len(os.listdir(nsrdb_path))):
    if i == 0:
        df_nsrdb = pd.read_csv(nsrdb_path+(os.listdir(nsrdb_path))[i], skiprows=2)
    else:
        df = pd.read_csv(nsrdb_path+(os.listdir(nsrdb_path))[i], skiprows=2)
        df_nsrdb = pd.concat([df_nsrdb, df], axis=0)

df_nsrdb['Datetime'] = pd.to_datetime(df_nsrdb[['Year', 'Month', 'Day', 'Hour', 'Minute']])
df_nsrdb['Datetime'] = df_nsrdb['Datetime'].apply(lambda x: x.replace(microsecond=0, second=0, minute=0))


#METEO DATA HANDLE 1
meteo_reader = MeteoReader.MeteoReader(folder=meteo_path_1)
df_meteo = meteo_reader.rp5_data_reader()
df_meteo_1 = df_meteo[df_meteo.index < '2010-02-01 12:00:00'] # 6 hours
df_meteo_2 = df_meteo[df_meteo.index >= '2010-02-01 12:00:00']
df_meteo_2 = df_meteo_2[df_meteo_2.index < '2013-12-17'] # 3 hours
df_meteo_3 = df_meteo[df_meteo.index >= '2013-12-17'] # 1 hours

df_meteo_1_interpol = meteo_data_interpolation.rp5_hour_interp_6(df_meteo_1)
df_meteo_2_interpol = meteo_data_interpolation.rp5_hour_interp_3(df_meteo_2)
df_meteo_3_interpol = df_meteo_3

df_meteo_3_interpol['N'] = df_meteo_3_interpol['N'].interpolate()
df_meteo_3_interpol['N'] = df_meteo_3_interpol['N'].fillna(method='bfill')
df_meteo_3_interpol['Nh'] = df_meteo_3_interpol['Nh'].interpolate()
df_meteo_3_interpol['Nh'] = df_meteo_3_interpol['Nh'].fillna(method='bfill')

df_meteo_3_interpol['Cl'] = df_meteo_3_interpol['Cl'].fillna(method='ffill')
df_meteo_3_interpol['Cl'] = df_meteo_3_interpol['Cl'].fillna(method='bfill')
df_meteo_3_interpol['Cm'] = df_meteo_3_interpol['Cl'].fillna(method='ffill')
df_meteo_3_interpol['Cm'] = df_meteo_3_interpol['Cl'].fillna(method='bfill')
df_meteo_3_interpol['Ch'] = df_meteo_3_interpol['Cl'].fillna(method='ffill')
df_meteo_3_interpol['Ch'] = df_meteo_3_interpol['Cl'].fillna(method='bfill')

df_meteo_interpol = pd.concat([df_meteo_1_interpol, df_meteo_2_interpol, df_meteo_3_interpol], axis=0)

#METEO DATA HANDLE 2
meteo_reader2 = MeteoReader.MeteoReader(folder=meteo_path_2)
df_meteo2 = meteo_reader2.rp5_data_reader()

df_meteo_4 = df_meteo2[df_meteo2.index < '2020-12-23 01:00:00'] # 1 hours
df_meteo_5 = df_meteo2[df_meteo2.index > '2020-12-23 01:00:00'] # 3 hours

df_meteo_4_interpol = df_meteo_4
df_meteo_5_interpol = meteo_data_interpolation.rp5_hour_interp_3(df_meteo_5)

df_meteo_4_interpol['N'] = df_meteo_4_interpol['N'].interpolate()
df_meteo_4_interpol['N'] = df_meteo_4_interpol['N'].fillna(method='bfill')
df_meteo_4_interpol['Nh'] = df_meteo_4_interpol['Nh'].interpolate()
df_meteo_4_interpol['Nh'] = df_meteo_4_interpol['Nh'].fillna(method='bfill')

df_meteo_4_interpol['Cl'] = df_meteo_4_interpol['Cl'].fillna(method='ffill')
df_meteo_4_interpol['Cl'] = df_meteo_4_interpol['Cl'].fillna(method='bfill')
df_meteo_4_interpol['Cm'] = df_meteo_4_interpol['Cl'].fillna(method='ffill')
df_meteo_4_interpol['Cm'] = df_meteo_4_interpol['Cl'].fillna(method='bfill')
df_meteo_4_interpol['Ch'] = df_meteo_4_interpol['Cl'].fillna(method='ffill')
df_meteo_4_interpol['Ch'] = df_meteo_4_interpol['Cl'].fillna(method='bfill')

df_meteo_all_interpol = pd.concat([df_meteo_interpol, df_meteo_4_interpol, df_meteo_5_interpol], axis=0)
df_meteo_all_interpol = df_meteo_all_interpol.sort_index()
df_meteo_all_interpol['Datetime'] = df_meteo_all_interpol.index


#MERGE DATAFRAMES
dfs = [df_wrdc, df_meteo_all_interpol, df_nsrdb]
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on='Datetime'), dfs)

df_final.to_excel(res_path_xls)
df_final.to_csv(res_path_csv)