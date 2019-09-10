# Import libraries
import pandas as pd 
#   from sklearn.datasets import load_boston

##  There are three functions in here, first two are commented out, the last, which is optimized 
##  from a performance perspective, remains.  Test results are commented at the bottom as well.
##  Thanks to Dan Smilowitz for ideas on optimizing the code.

# original
# def desc_info(self):
#     # get stats for counts, count null, count unique, 
#     # mean, std, max, 25%, 50%, 75%, max
#     column_headers = [i for i in self] #get column headers
#     column_headers.append('type')
#     desc=pd.DataFrame(columns=column_headers) #set column headers

#     # Establish lists for attributes to track
#     datatype = []
#     count = []
#     null = []
#     zero = []
#     unique = []
#     minimum = []
#     quarter = []
#     median = []
#     threequarter = []
#     maximum = []
#     summation = []
#     mean = []
#     std = []
#     counter = 0

#     # get values for each column in the dataframe
#     for i in self:
#         datatype.append(self[i].dtype)
#         count.append(len(self[i]))
#         null.append(self[i].isnull().sum())
#         zero.append((self[i]==0).sum())
#         unique.append((len(self[i].unique())))
#         if self[i].dtype.kind in 'bifc':
#             minimum.append(self[i].min())
#             quarter.append(self[i].quantile(.25))
#             median.append(self[i].quantile(.50))
#             threequarter.append(self[i].quantile(.75))
#             maximum.append(self[i].max())
#             summation.append(self[i].values.sum())
#             mean.append(summation[counter]/count[counter])
#             std.append(self[i].std())
#         else:
#             minimum.append('NaN')
#             quarter.append('NaN')
#             median.append('NaN')
#             threequarter.append('NaN')
#             maximum.append('NaN')
#             summation.append('NaN')
#             mean.append('NaN')
#             std.append('NaN')
#         counter += 1

#     # Add row header for each row
#     datatype.append('Data Type')
#     count.append('Count')
#     null.append('Null')
#     zero.append('Zero')
#     unique.append('Unique')
#     minimum.append('Min')
#     quarter.append('25%')
#     median.append('50%')
#     threequarter.append('75%')
#     maximum.append('Max')
#     summation.append('Sum')
#     mean.append('Mean')
#     std.append('Std')

#     # Set values  for reach row and column in desc
#     desc.loc[1] = datatype
#     desc.loc[2] = count
#     desc.loc[3] = null
#     desc.loc[4] = zero
#     desc.loc[5] = unique
#     desc.loc[6] = minimum
#     desc.loc[7] = quarter
#     desc.loc[8] = median
#     desc.loc[9] = threequarter
#     desc.loc[10] = maximum
#     desc.loc[11] = summation
#     desc.loc[12] = mean
#     desc.loc[14] = std

#     # Set type as index
#     desc.set_index('type',inplace=True)
#     desc.index.name = None

#     return(desc)

# # version 2
# def desc_info(self):
#     cols = self.columns

#     desc = {}
#     for col in cols:
#         # get info for each column
#         info = [
#             self[col].dtype,  # datatype
#             len(self[col]),  # count
#             self[col].isnull().sum(),  # missing
#             (self[col] == 0).sum(),  # zero
#             len(self[col].unique())  # unique
#         ]
#         # summaries for numeric columns
#         if self[col].dtype.kind in 'iufc':
#             info += [
#                 self[col].min(),  # minimum
#                 self[col].quantile(0.25),  # first quartile
#                 self[col].quantile(0.5),  # median
#                 self[col].quantile(0.75),  # third quartile
#                 self[col].max(),  # max
#                 self[col].sum(),  # sum
#                 self[col].mean(),  # mean
#                 self[col].std()  # standard deviation
#             ]
#         # fill with nans for non-numeric
#         else:
#             info += [pd.np.nan] * 8
    
#         # assign to dict
#         desc[col] = info

#     # index of summaries
#     idx = ['Data Type', 'Count', 'Null', 'Zero', 'Unique', 'Min',
#         'Q1', 'Median', 'Q3', 'Max', 'Sum', 'Mean', 'Std']
    
#     # convert to df
#     return pd.DataFrame(desc, index=idx)

# Optimized
def desc_info(self):
    desc = self.describe(include='all')
    # dtype, null, zero, unique, sum
    info = {'dtype': self.dtypes,
        'null': self.apply(lambda x: x.isnull().sum(), axis=0),
        'zero': self.apply(lambda x: (x == 0).sum(), axis=0),
        'unique': self.apply(lambda x: len(x.unique()), axis=0)}
    info = pd.DataFrame(info).transpose()
    info = pd.concat([desc, info])
    idx = ['dtype','count','unique','null','zero','mean',
    'std','min','25%','50%','75%','max']
    info = info.reindex(idx)
    return info

# set as method
setattr(pd.DataFrame, 'desc_info', desc_info)

# # get some data
# boston_data = load_boston()
# boston = pd.DataFrame(boston_data['data'],
#     columns=boston_data['feature_names'])
# boston['MEDV'] = boston_data['target']

# boston['test'] = ['a'] * 500 + [pd.np.nan] * 6
# boston['test2'] = [True, False] * 253

# # test results
# orig = boston.info2()  # 227 ms ± 47.8 ms
# updt = boston.desc_info()  # 98 ms ± 5.75 ms
# steal = boston.steal_desc()  # 77.5 ms ± 5.18 ms

# orig.index = ['Data Type', 'Count', 'Null', 'Zero', 'Unique', 'Min',
#         'Q1', 'Median', 'Q3', 'Max', 'Sum', 'Mean', 'Std']
# orig == updt

# # same for *almost* all values
#   # original returns 'NaN' for object; original returns np.nan
#   # original runs on bool; update doesn't
#   # some means are different -- rounding error (1e-13)

