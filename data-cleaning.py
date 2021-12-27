# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z8NpyuPLuqB_e4-nExo0_Kom_-7RO7YT
"""

from google.colab import drive
import numpy as np
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib.pyplot
import matplotlib.dates
import os
import plotly.graph_objects as go
import plotly.express as px

#function for read data frame(csv file)

def read_df(path):
    df=pd.read_csv(path)
    return df

"""read from google drive"""

drive.mount('/content/drive')
path= '/content/drive/MyDrive/out.csv'

"""functions"""

#function for count row

def count_row(df):
    index= df.index
    row_num= len(index)
    return row_num

#function for delete missing source function

def drop_missing_source(df):
    source= df.dropna(subset=['source'], how='any')
    return source

#delete missing repositories

def drop_missing_repo(df):
    repo= df.dropna(subset=['repo'], how='any')
    return repo

#funciton for delete missing author

def drop_missing_author(df):
    author= df.dropna(subset=['author'], how='any')
    return author

#delete missing time

def drop_missing_times(df):
    time= df.dropna(subset=['commit_time', 'author_time'], how='any')
    return time

#delete missing time

def drop_missing_tz(df):
    tz= df.dropna(subset=['commit_tz', 'author_tz'], how='any')
    return tz

#delete missing timezone

def drop_missing_tz(df):
    tz= df.dropna(subset=['commit_tz', 'author_tz'], how='any')
    return tz

#drop Limits less than 6 characters

def drop_short_message(df):
  short_message= df.drop(df[df['message'].str.len() <= 6].index)
  return short_message

#delete all missing data

def drop_all_missing_value(df):
    droped= df.dropna(subset=['source', 'repo', 'author', 'author_time', 'commit_time', 
                                 'message', 'committer'], how='any')
    return droped

#function for sort values

def asc_sort_values(df, case):
  sorted= df.sort_values(by=case, ascending=True)
  return sorted

#save csv data frame

def save_csv(extention, name, df):
  full_name= name + '.' + extention
  csv_name= name + '.' + 'csv'
  compression_opts = dict(method=extention,
                        archive_name=csv_name)
  df.to_csv(full_name, index=False,
          compression=compression_opts)

"""read data frame"""

dataframe= read_df(path)

"""Export csv file"""

confirmed= drop_all_missing_value(dataframe)
final_version= drop_short_message(confirmed)
save_csv('zip', 'clean-data', final_version)
#dataframe.isnull().sum()