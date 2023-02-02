#!/usr/bin/env python
# coding: utf-8

# # Stock screening and ranking
# The goal of systematic teams is to make investing more reliable, repeatable, and quantitative by avoiding the biases and errors of traditional stock picking. There are two types of stock screening methods: sequential and simultaneous. In sequential screening, criteria are applied one after the other to eliminate stocks from the investment universe. In simultaneous screening, all criteria are applied at once, and all stocks receive a ranking based on their overall scores. The most popular simultaneous screening method is the z-score approach, which involves choosing factors that explain stock returns and aggregating them into one score to rank stocks. The z-score ranking can be used as the basis for a stock returns model or added to an existing model.
# 
# # Sequential screening
# 
# Sequential Stock Screening is a simple and straightforward method for portfolio managers to select stocks for investment. It involves ranking stocks according to their favorable and unfavorable attributes and eliminating those that don't meet the criteria set by the portfolio manager. The process starts by defining the investment goals and selecting relevant factors, such as P/B ratio or profit margins, to screen the stocks. The screens are then applied in order of importance, starting with the most critical factor. An example of a sequential stock screening process would be selecting the top 25% of stocks with the highest profit margins and then selecting the top 10 of those with the highest B/P ratios. A good stock screen should be easy to automate, replicate, and accurately reflect the portfolio manager's preferences.
# 
# The key to a portfolio manager's success is the ability to determine factors that drive exceptional stock returns. Managers often have a guiding investment style or philosophy, but it can be quantified through stock screening methods. Here, we specify three successful equity managers' strategies, which can be qualitative or fundamental, and translates them into quantifiable screens.
# 
# - Lynch Screen: This is a combination of growth-and-value strategy that seeks a P/E ratio below the industry average but also a PEG ratio below 1.0. Other criteria include a P/E to dividend yield ratio less than 4.0, earnings growth between 0% and 50%, insider buying-to-selling ratio greater than 1.5, long-term debt ratio below industry median, market capitalization less than $5 billion, and institutional ownership less than 50%.
# 
# - Buffett Screen: This screen is based on Warren Buffett's buy-and-hold strategy and focuses on companies with a strong competitive advantage, efficient management, high free cash flow, return on equity greater than or equal to 15%, net profit margins exceeding industry averages, D/E ratio in line with or lower than industry median, and forecasted free cash flow for the next five years greater than the current market price of the stock when discounted back to the present. The screen restricts investments to the top 30% market capitalization of listed equities on the NYSE, AMEX, and NASDAQ.
# 
# - Lakonishok Screen: This is a value screen based on the work of Josef Lakonishok, CEO and founder of LSV Asset Management. The screen focuses on identifying undervalued companies with market capitalizations in the top 30% of the NYSE, AMEX, and NASDAQ. The screen seeks companies with a P/E ratio and P/B ratio below their respective industry median values, consensus earnings estimate for the next fiscal year greater than the current year's estimate, and a forecasted earnings growth rate greater than 5%.
# 
# # Simultaneous screening
# In simultaneous screening, a portfolio manager evaluates all stocks based on a set of criteria, considering all the factors at once instead of one at a time. This eliminates the risk of eliminating a good stock due to its poor performance in an early round of screening and ensures a larger pool of stocks to choose from. To aggregate the factors, the portfolio manager needs to standardize or normalize them by transforming them into a standard unit of measurement, such as the z-score method. This ensures that the variables are comparable and prevents any single factor from dominating the stock ranking.
# 
# # z-score
# The z-score is a statistical method used to standardize the values of a variable within a population of data. It measures how far away a particular observation is from the population mean. To calculate the z-score, the difference between the observed value and the mean of the population is divided by the standard deviation of the population. This results in a normalized score that shows how far the observation is from the norm in terms of standard deviations. Z-scores allow comparison of two different variables, as they are expressed in the same units. If the original data distribution is normal, the z-score can be used to make statements about the rarity or probability of a particular observation. To assign z-scores, the mean and standard deviation of the factor must be calculated for all stocks in the investment universe, and the z-score calculation must be performed for each stock. It is important to make sure that the factors being used are expressed such that high values are good and low values are bad, as the z-scores must match the underlying factor values.
# 
# # Simple z-score combination
# When dealing with multiple factors, we can aggregate z-scores by combining the z-scores for each factor of a stock into a single screening value. The aggregate z-score is calculated by adding the z-scores for each factor of a stock, as z-scores are scale independent. The weighting of each factor in the aggregate z-score can be equal or determined through a sophisticated weighting scheme, with equal weighting being a common method used by portfolio managers due to its stable results. Extreme values in individual factors or stock aggregate z-scores can be handled through winsorizing or throwing out stocks with extreme values, but this may result in the loss of important information.
# 
# # Ad hoc z-score combination
# Ad Hoc Aggregate Z-Score is a method of weighting the individual factor z-scores within the aggregate z-score. Portfolio managers use their own judgement and personal preferences to assign weights to the factors. This method can be influenced by past research or past reading and may not be entirely based on a systematic and quantitative approach. There are several variations of this method, including weighting factors according to their perceived importance, weighting based on the factors' information ratios, and weighting based on the portfolio manager's own investing style. The latter is done by amplifying the importance of the factor that is preferred over others. The method of weighting based on information ratios involves computing the historical information ratio of each factor by creating decile or quintile portfolios. Factors with higher information ratios are assigned more weight. However, this method also fails to take into account the correlation between factors.
# 
# # Optimized z-score combination
# The traditional approach of equally weighting the z-scores is simple, but it ignores important information contained in the data and fails to account for the correlation between factors. On the other hand, ad hoc methods of weighting, which assign weights based on the perceived importance of the factors, are highly subjective.
# 
# An alternative approach is to use econometrics to estimate the optimal exposures using a historical sample data set. The portfolio manager takes a series of monthly returns on all the stocks in the universe, combined with the factor z-score values for each stock at the beginning of the month, and runs a set of cross-sectional regressions to find the optimal Z-score weights.
# 
# The optimal combination of z-scores can be estimated through regression analysis using the historical data. This regression uses the variance-covariance matrix of z-scores and returns to estimate the parameter exposures of each factor. The portfolio manager can run this regression over different time periods and horizons to ensure the robustness of the results.
# 
# Another variation on the optimal weighting scheme is to determine the optimal weights for various economic scenarios. The portfolio manager creates several hypothetical economic environments and calculates a set of optimal z-score weights for each. This method is more subjective as it involves more judgment, but it allows the manager to consider the direction of the economic winds and weight the factors accordingly.
# 
# # By-group combination
# Quantitative portfolio managers may divide their K factors into M factor groups to organize and simplify the screening process. By creating factor groups that represent different aspects of stock returns, the manager can change the relative importance of each factor group according to changing economic conditions. The procedure for computing aggregate z-scores using factor groups is almost identical to the procedure for computing aggregate z-scores. The only difference is that the individual factors are classified into specific factor groups. To compute the aggregate z-score, the z-scores of each factor group are weighted and summed, and the resulting sum represents the aggregate z-score for each stock in the investment universe. The weighting scheme for the factors within and across groups can be determined using similar methods as the normal z-score aggregation without groups.
# 
# # Expected return implied by the z-scores
# 
# The expected return of a stock can be estimated by regressing actual stock returns on the aggregate z-scores. This can be done using a panel series regression of stock returns on the z-score of the prior periods (e.g., of the previous months)
# The regression takes the form of
# $$r_{i,t+1}=a+bz_{i,t}+\epsilon_{i,t+1}$$
# where $a$ is a constant term, $b$ is the coefficient that relates the aggregate z-score to the stock return, and $\epsilon$ is the error term. With the estimated values of $a$ and $b$, the expected return of the stock for the next period can be calculated. However, this methodology has some limitations. Firstly, the z-scores may not change much over time but factor premiums ($b$) may change, leading to unstable or unreliable coefficients. Secondly, there may be a weak correlation between the z-score and subsequent returns, as the equation is not based on a rigorous theory. Lastly, this method adds complexity to the process, which is a drawback as the biggest advantage of the aggregate z-score model is its simplicity.
# 
# 
# # Some Code

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,1,100)
sr = (2*w+(1-w))/np.sqrt(20*w**2+10*(1-w)**2)

print( w[np.argmax(sr)], np.max(sr) )


# In[2]:


plt.plot(w,sr)
plt.show()

