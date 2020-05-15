import configparser
import v20 
import pandas as pd 
#import pandas_datareader.data as pdr
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import json
import requests

#loading oanda configuration file
config = configparser.ConfigParser()
config.read('oanda.cfg')

#calling oanda's practice environment 
oanda = v20.API(environment='practice', access_token=config['oanda']['access_token'])

#getting euro to usd on december 8-10th over minute breaks
data = oanda.get_history(instrument='EUR_USD', start='2016-12-08', end='2016-12-10', granularity='M1')

df = pd.DataFrame(data['candles']).set_index('time')
df.index = pd.DatetimeIndex(df.index)

df.info()
