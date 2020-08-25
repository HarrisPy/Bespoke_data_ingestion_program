# Bespoke_data_ingestion_program

Automatically finds and imports data files from selected directory. ingestion into dataframes and initial exploration of data performed

## Example Usage
from df_labeller import autosetup

autosetup('C:/Users/chris/Documents/datasets_xfer/epl2020/')

## Output 
runcell(0, 'C:/Users/chris/Documents/datasets_xfer/df_labeller/df_labeller/test.py')
3 .csv files have been ingested

3 DataFrames have been created and stored in dictionary: data_dict

use following keys to access data (recommended to create new variable(s) containing dataframe(s)):

DJI
NFLX
NFLX_daily_by_quarter

DataFrame information for DJI

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12 entries, 0 to 11
Data columns (total 7 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Date       12 non-null     object 
 1   Open       12 non-null     float64
 2   High       12 non-null     float64
 3   Low        12 non-null     float64
 4   Close      12 non-null     float64
 5   Adj Close  12 non-null     float64
 6   Volume     12 non-null     int64  
dtypes: float64(5), int64(1), object(1)
memory usage: 800.0+ bytes
None

               Open          High  ...     Adj Close        Volume
count     12.000000     12.000000  ...     12.000000  1.200000e+01
mean   21576.639323  22090.152507  ...  21937.621745  6.510095e+09
std     1332.002426   1458.599365  ...   1503.771517  6.329533e+08
min    19872.859375  20125.580078  ...  19864.089844  5.392630e+09
25%    20884.259278  21101.965332  ...  20908.442383  6.176700e+09
50%    21211.425781  21732.415039  ...  21620.375000  6.536170e+09
75%    22092.194824  22685.944824  ...  22648.127441  7.010125e+09
max    24305.400391  24876.070313  ...  24719.220703  7.335640e+09

[8 rows x 6 columns]
DataFrame information for NFLX

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12 entries, 0 to 11
Data columns (total 7 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Date       12 non-null     object 
 1   Open       12 non-null     float64
 2   High       12 non-null     float64
 3   Low        12 non-null     float64
 4   Close      12 non-null     float64
 5   Adj Close  12 non-null     float64
 6   Volume     12 non-null     int64  
dtypes: float64(5), int64(1), object(1)
memory usage: 800.0+ bytes
None
