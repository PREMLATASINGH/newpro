import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data4.csv')
print(df.head())
print(df.isnull().sum())
df['Sales'].fillna(df['Sales'].mean(), inplace=True)  
print(df.isnull().sum())
df['Value'].fillna(df['Value'].mean(), inplace=True)    
print(df.isnull().sum())
print(df.tail())
print(df.groupby('Region')['Sales'].mean())
print(df.groupby('Region')['Value'].mean())