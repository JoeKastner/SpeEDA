# Import libraries
import pandas as pd
import seaborn as sns


''' Name: desc_info
    Description:    Method which combines pandas.describe method with 
                    a few additional fields to get an understanding of the makeup
                    of the data within a dataframe.
    Inputs: 
        - Dataframe
    Outputs: 
        - Dataframe including the following:
            - dtype:    Datatype for the column
            - len:      Total number of records
            - count:    Number of non-null records for numeric columns
            - unique:   Number of unique records
            - null:     Number of null records
            - zero:     Number of records that equal 0
            - mean:     Mean for numeric colulmns
            - std:      Standard deviation for numeric columns
            - min:      Minimum value for numeric columns
            - 25%:      Value representing the 25th percentile for numeric columns
            - 50%:      Value representing the 50th percentile for numeric columns
            - 75%:      Value representing the 75th percentile for numeric columns
            - max:      Maximum value for numeric colums '''
     
def desc_info(self):
    desc = self.describe()
    info = {'dtype': self.dtypes,
        'len' : self.apply(lambda x: len(x), axis=0),
        'null': self.apply(lambda x: x.isnull().sum(), axis=0),
        'zero': self.apply(lambda x: (x == 0).sum(), axis=0),
        'unique': self.apply(lambda x: len(x.unique()), axis=0)}
    info = pd.DataFrame(info).transpose()
    info = pd.concat([desc, info],sort=True)
    idx = ['dtype','len','count','unique','null','zero','mean',
    'std','min','25%','50%','75%','max']
    info = info.reindex(idx)
    return info

setattr(pd.DataFrame, 'desc_info', desc_info)

''' Name:   drop_unpop_cols
    Description:    Method which drops columns that are below
                    the specified level of population.
    Inputs: 
        - Dataframe
    Outputs: 
        - Dataframe including the following:
            - dtype:    Datatype for the column
            - len:      Total number of records
            - count:    Number of non-null records for numeric columns
            - unique:   Number of unique records
            - null:     Number of null records
            - zero:     Number of records that equal 0
            - mean:     Mean for numeric colulmns
            - std:      Standard deviation for numeric columns
            - min:      Minimum value for numeric columns
            - 25%:      Value representing the 25th percentile for numeric columns
            - 50%:      Value representing the 50th percentile for numeric columns
            - 75%:      Value representing the 75th percentile for numeric columns
            - max:      Maximum value for numeric colums '''

def drop_unpop_cols(self, pop_perc=0.4):
    dropped = [col for col in self.columns
        if (self[col].count() / self.shape[0]) < pop_perc]
    if len(dropped) >= 1:
        print('Columns with < %d%% population were dropped: %s' % ((pop_perc * 100), ', '.join(dropped)))
    else:
        print('All columns at least %d%% populated.' % ((pop_perc * 100)))
    return self.drop(columns=dropped)

setattr(pd.DataFrame, 'drop_unpop_cols', drop_unpop_cols)






