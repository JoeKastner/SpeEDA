#%% Import libraries
import pandas as pd 
from pandas.core.base import PandasObject

def info(df):

#%% import data set
#df = pd.read_csv(r'/Users/joe/OneDrive/Data_Science/Data_Sets/titanic.csv')

#%% get stats for counts, count null, count unique, 
# mean, std, max, 25%, 50%, 75%, max
    column_headers = [i for i in df] #get column headers
    column_headers.append('type')
    desc=pd.DataFrame(columns=column_headers) #set column headers

#%% Establish lists for attributes to track
    datatype = []
    count = []
    null = []
    zero = []
    unique = []
    minimum = []
    quarter = []
    median = []
    threequarter = []
    maximum = []
    summation = []
    mean = []
    std = []
    counter = 0


#%% get values for each column in the dataframe
    for i in df:
        datatype.append(df[i].dtype)
        count.append(len(df[i]))
        null.append(df[i].isnull().sum())
        zero.append((df[i]==0).sum())
        unique.append((len(df[i].unique())))
        if df[i].dtype.kind in 'bifc':
            minimum.append(df[i].min())
            quarter.append(df[i].quantile(.25))
            median.append(df[i].quantile(.50))
            threequarter.append(df[i].quantile(.75))
            maximum.append(df[i].max())
            summation.append(df[i].values.sum())
            mean.append(summation[counter]/count[counter])
            std.append(df[i].std())
        else:
            minimum.append('NaN')
            quarter.append('NaN')
            median.append('NaN')
            threequarter.append('NaN')
            maximum.append('NaN')
            summation.append('NaN')
            mean.append('NaN')
            std.append('NaN')
        counter += 1


#%% Add row header for each row
    datatype.append('Data Type')
    count.append('Count')
    null.append('Null')
    zero.append('Zero')
    unique.append('Unique')
    minimum.append('Min')
    quarter.append('25%')
    median.append('50%')
    threequarter.append('75%')
    maximum.append('Max')
    summation.append('Sum')
    mean.append('Mean')
    std.append('Std')

#%% Set values  for reach row and column in desc
    desc.loc[1] = datatype
    desc.loc[2] = count
    desc.loc[3] = null
    desc.loc[4] = zero
    desc.loc[5] = unique
    desc.loc[6] = minimum
    desc.loc[7] = quarter
    desc.loc[8] = median
    desc.loc[9] = threequarter
    desc.loc[10] = maximum
    desc.loc[11] = summation
    desc.loc[12] = mean
    desc.loc[14] = std

#%% Set type as index
    desc.set_index('type',inplace=True)
    desc.index.name = None


#%%
    return(desc)