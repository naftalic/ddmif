#!pip install yfinance

import pandas as pd
import numpy as np
#import yfinance as yf
#yf.pdr_override()

def get_universe(data_dir, universe_file):
    
    return pd.read_csv(data_dir + universe_file)

def get_data(data_dir, universe_df, first_friday, first_saturday, first_sunday, last_saturday):
    
    assets_df = pd.DataFrame()
    for s in universe_df['symbol'].to_list():
      data = yf.download(s, start=first_friday, end=last_saturday, auto_adjust=True)
      df = data.reset_index()[['Date','Close']]
      df['Date']   = pd.to_datetime(df['Date'])
      df['symbol'] = s
      df = df.rename(columns={'Close': 'price','Date': 'date'})
      df = df[['symbol','date','price']]
      assets_df = assets_df.append(df)
    
    assets_df = assets_df.reset_index(drop=True)
    assets_df = assets_df.groupby(['symbol','date'])['price'].last().reset_index()
    
    df_ = pd.pivot_table(assets_df, index='date', values='price', columns='symbol').transform(lambda v: v.ffill()).reset_index()
    df_['date'] = pd.to_datetime(df_['date'],utc=True).dt.strftime('%Y-%m-%d')
    df_ = df_.set_index('date').stack().reset_index(name='price')
    df_ = df_.groupby(['symbol','date'])['price'].agg(['last']).reset_index()
    assets_df = pd.pivot_table(df_, index='date', values='last', columns='symbol').drop(index=[first_saturday,first_sunday])
    return assets_df
    
def decision_performance(S, w):
  import numpy as np
  eps = 1e-3
  assert 1+eps>np.sum(np.abs(w)) and np.sum(np.abs(w)) >= 0.25, "w is not conditioned well"

  if np.sum(np.abs(w))<1: # add cash to the portfolio
    w1 = 1- np.sum(np.abs(w))
  else:
    w1 = 0
  w = np.array(list(w)+[w1])

  cash = np.array([100,100,100,100,100,100])
  S = np.vstack((S, cash))

  RET = np.nansum(np.reshape(np.vstack(w),(-1,1))*(S[:,1:]/S[:,:-1]-1), axis=0)
  ret = np.log(1 + RET)

  std = np.nanstd(ret, ddof=1)
  ret = np.nansum(ret)
  ir = (252/5)*ret/(np.sqrt(252)*std)
  return ir
  
def forecast_performance(f,q):
  
  eps = 1e-3
  assert np.all(q >= 0) and np.all(f >= 0) and np.all(np.abs(np.sum(f,axis=1)-1)<eps) and np.all(np.abs(np.sum(q,axis=1)-1)<eps), \
        "f or q are not conditioned well"
  
  q = np.cumsum(q, axis=1) 
  f = np.cumsum(f, axis=1) 
  fp = np.sum((q-f)**2, axis=1)/f.shape[1] #forecast performance
  return np.mean(fp) #mean forecast performance 