# импорт пакетов
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

plt.style.use('ggplot')
from matplotlib.pyplot import figure

# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12, 8)

pd.options.mode.chained_assignment = None

# чтение данных
df = pd.read_csv(r'C:\Users\user\Downloads\sberbank.csv')

# shape and data types of the data
# print(df.shape)
# print(df.dtypes)

# отбор числовых колонок
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
# print(numeric_cols)

# отбор нечисловых колонок
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
# print(non_numeric_cols)
#
# for column in df.columns:
#     empty_data = df[column].isnull().sum()
#     # print(df[column].count(), empty_data)
#     # print(f"{column} - {round(empty_data/df.shape[0], ndigits=2)}")
#
# for column in df_numeric:
#     med = df[column].median()
#     # print(med)
#     df[column] = df[column].fillna(med)
#     # print(df[column])

# for col in non_numeric_cols:
#     missing = df[col].isnull()
#     num_missing = np.sum(missing)
#
#     if num_missing > 0:  # only do the imputation for the columns that have missing values.
#         # print('imputing missing values for: {}'.format(col))
#         df['{}_ismissing'.format(col)] = missing
#         med = df[col].median()
#         df[col] = df[col].fillna(med)
#
# print(df.shape)
# unique_rec = []
# for index, row in df.iterrows():
#     if row['id'] in unique_rec:
#         df_less_nonunique_rec = df.drop(row, axis=1)
#     else:
#         unique_rec.append(row['id'])
#
# print(df.shape)
