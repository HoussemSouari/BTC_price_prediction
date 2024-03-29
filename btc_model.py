# -*- coding: utf-8 -*-
"""Stock market.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F0DEEOgQlGP-11GzUf-SBMskD-1NNvWK
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('btc_stock.csv')

df.head()

df.tail()

df.info()

df.shape

df = df.replace(',', '', regex=True)

df.iloc[:,1:] = df.iloc[:,1:].astype(float)

df

df['profit'] = df['Close'] - df['Open']
df

plt.figure(figsize=(10,7))
sns.regplot(x=df['Open'],y=df['Close'], color='b')
plt.show()

from sklearn.linear_model import LinearRegression

correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Heatmap')
plt.show()

from sklearn.ensemble import RandomForestClassifier

model = LinearRegression()

df.drop(columns='Year', inplace=True)
df

df.isnull().sum()

X=df.iloc[:,:3]
y=df['Close']
X.shape

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

model.fit(X_train,y_train)

X_test

y_pred = model.predict(X_test)
y_pred

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
r2





