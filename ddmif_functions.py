import pandas as pd
import numpy as np
import yfinance as yf
yf.pdr_override()

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

def eval_submission_file(filename, universe_df):
  symbols = universe_df.sort_values(by=['symbol'])['symbol']
  eps = 1e-3
  try:
    df = pd.read_csv(filename, sep=",", header=0, index_col=0).sort_values(by=['id'])
    assert np.all(list(df['id'])==list(symbols))
    assert len(df)==110
    assert len(df.columns)==7
    f = df[['rank1', 'rank2', 'rank3', 'rank4','rank5']].to_numpy()
    w = np.reshape(df['decision'].to_numpy(),(-1,1))
    assert np.all(f >= 0) 
    assert np.all(np.abs(np.sum(f,axis=1)-1)<eps) 
    assert 1+eps>np.sum(np.abs(w)) 
    assert np.sum(np.abs(w)) >= 0.25
    return print("submission file",filename,"is okay")
  except:
    print('******************')
    print("**Problem** with file", filename)
    print("list of symbols:", np.all(list(df['id'])==list(symbols)))
    print("len of df:", len(df))
    print("len of columns:", len(df.columns))
    print("dimensions:", f.shape, q.shape, S.shape, w.shape)
    print("sum of abs decisions:", df.iloc[:,-1].abs().sum())
    print("sum of ranks equals 1:", np.all(np.abs(df.loc[:,['rank1',	'rank2',	'rank3',	'rank4',	'rank5']].sum(axis=1)-1)<eps) )
    print("all ranks are non negative:", np.all(df.loc[:,['rank1',	'rank2',	'rank3',	'rank4',	'rank5']]>=0) )
    print('******************')
  return print("file is NOT ready for submission")
  
def quintile_rank_with_average_tie(vector):
  data = pd.DataFrame({'value':vector, 'dense_rank':np.argsort(np.argsort(vector))})
  data['quintile'] = pd.qcut(data['dense_rank'], q=5, labels=range(1, 6)).astype('float32')
  data['quintile_rank'] = data.groupby('value')['quintile'].transform(lambda x: x.mean())
  return data['quintile_rank'].values

def map_to_vector(vector):
    quintile_vector = np.zeros((len(vector), 5))
    for i in range(len(vector)):
        quintile_vector[i, int(vector[i])-1] = 1
        if np.abs(int(vector[i])-vector[i])>0:
          quintile_vector[i, int(np.ceil(vector[i]))-1]  = vector[i]-np.floor(vector[i])
          quintile_vector[i, int(np.floor(vector[i]))-1] = np.ceil(vector[i])-vector[i]
    return quintile_vector