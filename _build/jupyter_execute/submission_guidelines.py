#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# As part of this course, students will participate in an in-class real-time financial forecasting competition similar to the [M6](https://m6competition.com/). The competition will require students to augment open-source financial data with external open-source datasets of their choice. They will then present their findings to the class by the end of the course.
# 
# The focus of the forecasting competition will be on several key areas, including the ability to estimate future returns and uncertainty, combining estimates into an investment decision, developing a consistent investment strategy, utilizing alternative datasets effectively, and learning from mistakes through teamwork and transparency.
# 
# The winning students of the competition will be guaranteed an A and will receive a special prize as recognition for their achievement.
# 

# # Schedule
# 
# The competition will take place in real-time during the semester.
# 

# # Evaluation
# 
# The competition will consist of two distinct challenges: Forecasting, which will be evaluated using the ranked probability score, and Investment decisions, which will be evaluated using the information ratio.
# 

# # Data
# 
# The competition's investment universe will consist of three asset classes: 50 stocks from the S&P 500 index, 50 international ETFs, and 10 cryptocurrencies. These assets have been selected to provide a broad representation of the overall market.

# # Submission format
# 
# The competition will have 10 submission points, plus an additional test point, with a deadline of 6 PM ET on the Sunday before the start of the corresponding investment period. Participants are required to submit their forecasts and investment decisions at each point, outlining their predictions and strategy for the upcoming week. The forecast horizon is one week, typically five trading days, and there will be no overlapping evaluation periods.
# 
# Example: The deadline for the first submission point is 6 PM ET on September 18th, 2022 (Sunday). Participants are required to submit forecasts and investment decisions reflecting the closing value of the last trading day of the following week, which is September 23rd, 2022 (Friday).
# 

# At each submission point, students may submit a single csv file consisting of seven columns of 110 values each (one per asset):
# 
# * The first column must indicate the asset to which the forecasts and the respective row's investment decisions refer. The acronym of each asset will serve as an identifier.
# 
# * The second to sixth columns must contain positive values summing horizontally to unity that refer to the probabilities of the ranks of the forecasted percentage return for each asset (stocks or ETFs); rank 1 is the lowest forecasted percentage return, and rank 5 is the highest forecasted percentage return.
# 
# * The seventh column must contain numerical values corresponding to the weights for investing in each asset. These values must be positive for long positions, negative for short positions, or zero for no position. 
# 
# For example, if three assets are assigned weights 0.5, 0.3, and -0.2, respectively, and all other assets weights of 0, this means that the participant wishes to invest in only three assets with positions long, long, and short and with a budget allocation of 50%, 30%, and 20% respectively. The submission will be considered invalid if the sum of the absolute weights exceeds 1. If the sum of the absolute weights is less than 1 (less than 100%), then the remainder is assumed to be assigned to an asset with zero return and zero risk (i.e., no investment). However, if the sum of the absolute weights is below 0.25 (25%) the submission will be considered invalid (i.e., some investment must be made and some risk must be taken).

# Example: The following is an example for the first 8 rows of a submission file. In this case, the participant decides to invest in three assets (3rd, 6th, and 7th) with weights of 50%, 30%, and 20% (or 0.5, 0.3, and 0.2) and positions long, long, and short, respectively. Additionally, the participant forecasts that there is a probability of 0.1, 0.2, 0.5, and 0.2 that the first asset (MMM) will be ranked 2nd, 3rd, 4th, and 5th, respectively, with regards to the expected percentage return. Equally, the participant’s forecast is that the second asset (ATVI) will be ranked 3rd.

# In[1]:


import pandas as pd
import numpy as np
cols = ['id','rank1', 'rank2', 'rank3', 'rank4', 'rank5', 'decision']
assets = ['mmm','atvi','googl','aph','bmy','cb','exr','msi']
df = pd.DataFrame(columns = cols)
df["id"] = assets
mat = np.array([[0,0.1,0.2,0.5,0.2,0],               [0,0,1,0,0,0],               [.1,.1,.1,.1,.6,.5],                [.5,.4,.05,.05,0,0],                [.2,.2,.2,.2,.2,0],                [0,0,.1,.4,.5,.3],                [.7,.3,0,0,0,-.2],                [0,0,1,0,0,0]])
print(mat.shape)
df.loc[:,cols[1:]] = mat

print('sum of abs decisions: ', df.iloc[:,-1].abs().sum())
print('sum of ranks equals 1: ', np.all(df.iloc[:,1:-1].sum(axis=1)==1))
print('all ranks are non negative: ', np.all(df.iloc[:,1:-1]>=0))

df


# #Measuring the performance of the forecasts:
# 
# The forecasting performance for a specific submission point will be measured by the Ranked Probability Score (RPS). The realized percentage total returns of all assets over the period are divided into quintiles, ranking from 1 (worst performing) to 5 (best performing). Given 110 assets, 22 of these will receive a rank of 5, 22 a rank of 4, and so forth. In cases involving a tie on the margins of the classes, the tied assets will all be assigned the respective average rank. 
# 
# For example, if four assets are tied at the 20th place, then they will all get a rank of (5+5+5+4)/4=4.75, with three "5" in this expression being the rank of the 3 assets in the first quintile, and the "4" being the rank of the asset in the second quintile. The actual return ranking of each asset is described by a vector $q_{i,t}$ of order 5. For example, if asset i is ranked in quintile 3 at time t, then $q_{i,t}=(0,0,1,0,0)$ and a rank of 4.75 for asset j at time t will have $q_{j,t}=(0,0,0,0.25,0.75)$
# 
# 

# We construct a vector denoting the probabilities of each rank for a particular asset $f_{i,t}$, as submitted by a participant. The RPS for asset $i$ in period $t$ is then 
# 
# $$RPS_{i,t}=\frac{1}{5}\sum_{j=1}^5(\sum_{k=1}^jq_{i,t,k} -\sum_{k=1}^{j}f_{i,t,k})^2.$$
# 
# Example: We wish to compute the overall RPS of a participant for a particular asset, $i$, at one submission point, $t$. The submitted probabilities for the ranks are 0, 0.2, 0.3, 0.4, and 0.1, while the actual rank was 4. As such $q_{i,t}=(0,0,0,1,0)$, $f_{i,t}=(0,0.2,0.3,0.4,0.1)$, and 
# 
# $$RPS_{i,t}=\frac{[(0-0)^2+(0-0.2)^2+(0-0.5)^2+(1-0.9)^2+(1-1)^2]}{5}=0.06.$$

# The portfolio $RPS$ is
# 
# $$RPS_t=\frac{1}{N}\sum_{i=1}^{N}RPS_{i,t},$$ where $N$ is the number of assests (e.g., $N=110$). 
# 
# The overall RPS for multiple submission points $t_1$ to $t_2$ is $$RPS_{t_1-t_2}=\frac{1}{N(t_2-t_1+1)}\sum_{t=t_1}^{t_2}\sum_{i=1}^{N}RPS_{i,t}.$$

# In[ ]:


#Example

import numpy as np

f = np.cumsum(np.array([[0, 0.2, 0.3, 0.4, 0.1]]), axis=1)
q = np.cumsum(np.array([[0,0,0,1,0]]), axis=1)
np.sum((q-f)**2,axis=1)/f.shape[1]


# In[ ]:


#Example

#forecasting
f = np.array([[0,0,0,0.25,0.75],[0.2,0.2,0.2,0.2,0.2],[0,0,0.25,0.5,0.25],[0,0.25,0.5,0.25,0],[0.5,0,0,0,0.5],              [0,0,0,0.25,0.75],[0.2,0.2,0.2,0.2,0.2],[0,0,0.25,0.5,0.25],[0,0.25,0.5,0.25,0],[0.5,0,0,0,0.5]])
pd.DataFrame(data = f)


# In[ ]:


#Example

#actual
q = np.array([[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0],              [0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0]])
pd.DataFrame(data = q)


# In[ ]:


def forecast_performance(f,q):
  
  eps = 1e-3
  assert np.all(q >= 0) and np.all(f >= 0) and np.all(np.abs(np.sum(f,axis=1)-1)<eps) and np.all(np.abs(np.sum(q,axis=1)-1)<eps),         "f or q are not conditioned well"
  
  q = np.cumsum(q, axis=1) 
  f = np.cumsum(f, axis=1) 
  fp = np.sum((q-f)**2, axis=1)/f.shape[1] #forecast performance
  return np.mean(fp) #mean forecast performance

forecast_performance(f,q)


# #Measuring the performance of the investment decisions: 
# 
# The performance of investment decisions is evaluated using the Information Ratio (IR), calculated as the ratio of portfolio return (ret) to the standard deviation of portfolio return (sdp):
# 
# $$IR=\frac{ret}{sdp}$$
# 
# Where ret represents continuously compounded portfolio returns and sdp represents the standard deviation of these returns, calculated daily. It's important to note that all IR values reported are annualized. 
# This variant of the Information Ratio uses a benchmark return of 0 and is similar to the Sharpe Ratio, with a risk-free rate of 0
# 
# The formula for calculating daily portfolio holding period return is:
# $$RET_t=\sum_{i=1}^Nw_i(\frac{S_{i,t}}{S_{i,t-1}}-1)$$
# 
# Where N is the number of assets, $w_i$ is the portfolio weight, and $S_{i,t}$ is the adjusted closing price of asset i at the end of trading day t. $t-1$ refers to the previous trading day. The continuously compounded portfolio return is then calculated as:
# $$ret_t=log(1+RET_t)$$
# 
# This $RET_t$ is measured for a single day, $t$, and represents the percentage return associated with each asset selected for investment, averaged by the corresponding investment decision weight for each asset. To calculate returns for a holding period longer than one day, the sum of daily returns is taken. In particular, the return for the holding period from $t_1$ to $t_2$ is calculated as:
# $$ret_{t_1:t_2}=\sum_{t=t_1}^{t=t_2}ret_t$$
# 
# The standard deviation, $sdp_{t_1:t_2}$, is calculated using the same $t_2-t_1+1$ values of $ret_t$ as those used in the calculation of $ret_{t_1:t_2}$.
# 
# It is calculated as follows:
# $$varp_{t_1:t_2}=\frac{1}{T-1}\sum_{t=t_1}^{t_2}(ret_t-\frac{ret_{t_1:t_2}}{T})^2$$
# And
# $$sdp_{t_1:t_2}=\sqrt{varp_{t_1:t_2}}$$
# Where T is defined as $T=t_2-t_1+1$.
# Higher values of the Information Ratio (IR), which is the ratio of portfolio return (ret) to the standard deviation of portfolio return (sdp), suggest better investment performance.
# 

# Example: To calculate the Information Ratio (IR) of a one-week investment decision of a participant over a 5-day assessment period, we first calculate the daily compound returns, yielding 5 $ret_t$ observations. Summing these observations yields $ret_{1:5}=0.01$. We also calculate that $sdp_{1:5}=0.01$. Then, we have:
# $$IR_{t_1:t_2}=\frac{252/5\times 0.01}{\sqrt{252}\times 0.01}=0.79.$$
# Note that in this example, as in all our investment performance assessments, daily returns on investment decisions are utilized. This allows for more degrees of freedom when calculating the standard deviation, providing a more accurate representation of the investment's performance over the given period.

# In[ ]:


# Example

# weights
w = np.array([.2,.3,-.4])

# prices, end of trading day, Fri -> Fri
np.random.seed(10) 
S = np.random.normal(25, 6, size=(3, 6)) 

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

decision_performance(S, w)


# #Measuring the combined performance of the forecasts and the investment decisions
# 
# The combined performance of a forecasting and investment decision is measured by the arithmetic mean of the ranks of the ranked probability score (RPS) and the performance of the investment decision (IR), assuming equal importance between the two tasks. The overall rank for submission $t$ (OR) is calculated as:
# $$OR=\frac{rank(RPS)+rank(IR)}{2}$$
# Where rank(•) returns the rank of a participant relative to all other participants for that measure (RPS or IR). 
# 
# To calculate the overall forecasting rank, RPS, across all 12 submission points, the arithmetic mean of the RPS as calculated in each week is taken.

# # Submission example

# Submission guidelines summary:
# 
# * Submit a CSV file, not Google Sheet or XML
# * Name the file: GROUPNAME__DATETIME.csv (double underscores)
# * Columns must be named: "id", "rank1", "rank2", "rank3", "rank4", "rank5", "decision" (no "symbol" or "name" column)
# * File should contain 7 columns and 110 rows (not including header row)
# * "id" names must be unique and match asset universe
# * Values in "rank" columns should be between 0 and 1
# * Sum of "rank" columns for each row must equal 1
# * Sum of absolute values of "decision" column must be <= 1
# * Use a copy of the notebooks, do not edit provided notebooks unless necessary.

# In[ ]:


get_ipython().system('pip install yfinance')

import os
import sys
from google.colab import drive
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import shutil
import yfinance as yf
yf.pdr_override()

root_dir = '/content/drive/' 
drive.mount(root_dir)

main_dir = root_dir+'MyDrive/teaching/ddmif_spring_2023/' 
data_dir = main_dir+'data/'
ddmif_dir = root_dir+'MyDrive/teaching/ddmif'
sys.path.append(main_dir)
sys.path.append(data_dir)
os.chdir(main_dir)

ddmif_dir = root_dir+'MyDrive/teaching/ddmif_spring_2023/ddmif'
try:
  shutil.rmtree(ddmif_dir)
except:
  pass

get_ipython().system('git clone https://github.com/naftalic/ddmif.git')
import ddmif.ddmif_functions as ddmif
#pip freeze > requirements.txt


# In[ ]:


first_friday = "2023-01-20"

first_friday   = pd.to_datetime(first_friday, dayfirst=True)
first_saturday = first_friday + pd.Timedelta(days=1)
first_sunday   = first_friday + pd.Timedelta(days=2)
last_saturday  = first_friday + pd.Timedelta(days=8)

#get universe
universe_file = 'universe.csv'
universe_df   = ddmif.get_universe(data_dir, universe_file)

#get price data from yahoo
assets_df  = ddmif.get_data(data_dir, universe_df, first_friday.strftime('%Y-%m-%d'),              first_saturday.strftime('%Y-%m-%d'), first_sunday.strftime('%Y-%m-%d'), last_saturday.strftime('%Y-%m-%d'))
assets_df


# In[ ]:


#submission file example:

import datetime

N = 110
num_groups = 5

for i in range(num_groups):
  
  submission_time = datetime.datetime.now(timezone('EST')).strftime('%Y-%m-%d_%H:%M:%S')

  feature_list          = ['id', 'rank1', 'rank2', 'rank3', 'rank4','rank5', 'decision']
  submission_file       = pd.DataFrame(0, index=np.arange(N), columns = feature_list)
  submission_file['id'] = universe_df['symbol'].copy()

  x = np.random.uniform(0, 1, size=(N, 5))
  submission_file[['rank1', 'rank2', 'rank3', 'rank4','rank5']] = x / np.reshape(np.sum(x,axis=1),(-1,1))

  x = np.reshape(np.random.normal(0, .05, size=N), (-1,1))
  submission_file[['decision']] = x/np.sum(np.abs(x))

  submission_dir = main_dir+'submissions/dueJan15/'
  filename = 'group_'+str(i)+'__'+submission_time
  submission_file.to_csv(submission_dir+filename)
  print(submission_dir+filename)


# In[ ]:


# 'fake' real data
mean_price = 100
std_price  = 20
np.random.seed(10) 
S = np.random.normal(mean_price, std_price, size=(110, 6))

vector = S[:,-1]/S[:,0]

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

vector = S[:,-1]/S[:,0]
quintile_rank = quintile_rank_with_average_tie(vector)
q = map_to_vector(quintile_rank)

print(np.sum(q,axis=0))


# In[ ]:


submission_dir = main_dir+'submissions/dueJan15/'
symbols = universe_df.sort_values(by=['symbol'])['symbol']
eps = 1e-3
from glob import glob
lst = glob(submission_dir+'/*')

stats = pd.DataFrame(columns=['group_name','forecast_performance','decision_performance'])
group_name = []

for i in range(len(lst)):
  
  try:
    ddmif.eval_submission_file(lst[i], universe_df)

    df = pd.read_csv(lst[i],sep=",", header=0,index_col=0).sort_values(by=['id'])
    f = df[['rank1', 'rank2', 'rank3', 'rank4','rank5']].to_numpy()
    w = np.reshape(df['decision'].to_numpy(),(-1,1))
    stats.loc[i,:] = lst[i].split('/')[-1].split('__')[0], forecast_performance(f, q), decision_performance(S, w)
  except:
    print('******************')
    print("**Problem** with file:", i, lst[i].split('/')[-1])
    stats.loc[i,:] = lst[i].split('/')[-1].split('__')[0], 1e6, 1e6

stats['overall_rank'] = (pd.Series(stats['forecast_performance']).rank(method='dense') +                                     pd.Series(stats['decision_performance']).rank(method='dense'))/2

scoring_dir = main_dir+'scoring/'
stats.to_csv(scoring_dir+'dueJan15.csv')


# In[ ]:


lst2 = glob(scoring_dir+'/*')

for i in range(len(lst2)):
  df = pd.read_csv(lst2[i],sep=",", header=0,index_col=0)
  if i==0:
    final_stats = pd.DataFrame()
    final_stats['group_name'] = df['group_name']
  final_stats['OR_'+str(i)] = df['overall_rank']

cols = [i for i in final_stats.columns if 'OR' in i]
final_stats['mean_OR'] = final_stats[cols].mean(axis=1)

final_stats


# In[ ]:




