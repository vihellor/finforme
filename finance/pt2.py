import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

##start = dt.datetime(2000,1,1)
##end = dt.datetime(2017,4,29)
##
##df = web.DataReader('TSLA','google',start,end)
##df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
##print(df.head())

##df.plot()

print(df[['Open', 'High']].head())

##precio de cierre
df['Close'].plot()

plt.show()
