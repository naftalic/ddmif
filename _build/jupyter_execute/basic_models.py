#!/usr/bin/env python
# coding: utf-8

# # Basic Models
# 
# The Fundamental Factor Model aims to explain a stock's expected return based on its fundamental characteristics, such as price-to-earnings ratio, market capitalization, and other financial metrics. The idea is that these characteristics are proxies for the underlying risk and growth prospects of a company, which in turn determines the expected return.
# 
# The Economic Factor Model, on the other hand, uses macroeconomic variables such as gross domestic product (GDP) and inflation as factors to explain expected returns. The premise is that macroeconomic conditions drive the performance of the overall economy, and in turn, affect the expected return of individual stocks. This type of model can also incorporate other factors, such as sector-specific variables, to provide a more comprehensive view of a stock's expected return.
# 
# Both types of factor models are used by quantitative investors to help inform investment decisions. The models provide a systematic way to analyze risk and reward and identify which stocks are likely to outperform based on their factor exposures. However, it's important to note that factor models are not perfect, and past performance does not guarantee future returns. Additionally, changes in economic conditions and company fundamentals can impact the expected return of a stock, and the factor model must be updated to reflect these changes.
# 
# # Modeling Stock Returns
# 
# The equation for modeling stock returns is known as the Capital Asset Pricing Model (CAPM), which is a widely used model in finance for explaining the relationship between stock returns and systematic risk. The model assumes that each stock's return can be decomposed into two components:
# 
# A stock-specific component ($α_i$) which is uncorrelated with the market and represents the expected return of the stock that is not related to systematic risk factors.
# 
# A market-related component ($β_{i1}f_1 + β_{i2}f_2 + ... + β_{iK}f_K$) that represents the stock's exposure to systematic risk factors ($f_1, f_2, ..., f_K$). Each factor's return contributes to the stock's return in proportion to the factor's sensitivity to the stock, represented by $β_i$.
# 
# The term $ϵ_i$ represents the residual, which is the difference between the actual stock return and the expected return given by the model. The residual represents the unsystematic risk, which is unique to each stock and can be diversified away by holding a well-diversified portfolio.
# 
# The CAPM can be used to determine the expected return and risk of each stock and portfolio, and then choose the optimal portfolio based on the results. The optimal portfolio is the one that maximizes expected returns for a given level of risk or minimizes risk for a given level of expected returns. This process is known as Modern Portfolio Theory (MPT) and it is a cornerstone of quantitative investing.
# 
# 
# The steps to form a model and make a portfolio are a process of choosing and analyzing various factors to estimate the expected return and risk of each stock and portfolio. The goal is to make informed investment decisions based on data and mathematical models.
# 
# The first step is to choose factors. This involves considering what type of factors to include in the model and how many factors to use. The most commonly used factors in quantitative finance are the Fundamental Factor Model, which uses stock characteristics such as P/E ratio and market capitalization, and the Economic Factor Model, which uses macroeconomic variables such as GDP and inflation.
# 
# The next step is to choose the type of data to use. There are three main types of data used in quantitative finance: cross-sectional, time series, and panel data. Cross-sectional data provides a snapshot of all stocks in the market at a given point in time, while time series data provides a historical view of a single stock. Panel data combines both cross-sectional and time series data.
# 
# Once the factors and data have been selected, the next step is to determine the factor exposures, which is the relationship between the stock and the factors. This information is used to determine the expected return and risk of each stock and portfolio.
# 
# The reward for each unit of exposure to a risk factor is known as the factor premium and can be estimated using a zero-investment portfolio. This portfolio involves shorting one stock and using the proceeds to buy another stock. The difference in return between these two stocks represents the factor premium.
# 
# Expected return and risk are estimated by considering the total risk of each stock, including both diversifiable and non-diversifiable risks. Diversifiable risks are stock-specific and can be removed by diversifying holdings, while non-diversifiable risks are market risks that can't be removed from the portfolio.
# 
# Finally, the portfolio is weighted based on the investment objective and the forecast for future performance. This includes considering past data versus future data, factor exposure stability, and changes in factor premiums.
# 
# In conclusion, the steps to form a model and make a portfolio involve a systematic process of choosing and analyzing factors, selecting data, and estimating expected returns and risks to make informed investment decisions.
# 
# 
# # Screening and Ranking Stocks
# 
# A stock screening technique involves using specific criteria to identify stocks that meet certain investment goals. This technique is simpler than using a formal model, as it doesn't require in-depth analysis of factors and their exposures. Instead, it focuses on easily obtainable data points such as earnings growth, dividend yield, P/E ratio, or market capitalization.
# 
# Z-scores are a measure of how far a value is from the mean, expressed in terms of the standard deviation. In the context of stock selection, Z-scores can be used to rank stocks based on their deviation from the mean return of a particular factor, such as earnings growth or P/E ratio. Z-scores can help identify stocks that are undervalued or overvalued compared to their peers and provide a simple way to screen and rank stocks based on a specific factor.
# 
# While these techniques are quick and convenient, they may not provide a complete picture of a stock's risk and reward profile, and may not account for the dynamic relationships between different factors. Portfolio managers may opt to use a combination of these techniques and formal models to select stocks for their portfolio.
# 
# # Exercise
# 
# You are given a world with two stocks, Stock A and Stock B. The returns of the stocks in the next period, $r_{A,t+1}$ and $r_{B,t+1}$, are determined by their current Price-to-Earnings (P/E) ratios. 
# The equations for Stock A and Stock B's returns are given as 
# 
# $r_{A,t+1} = 0.1\times(P/E)_{A,t} +ε_{A,t+1}$, $ε_{A,t+1}\sim N(0,20)$, and
# $r_{B,t+1} = 0.1\times(P/E)_{B,t} +ε_{B,t+1}$, $ε_{B,t+1}\sim N(0,10)$.
# 
# As seen, the returns are influenced by the P/E ratios and their random components are represented by ε. ε is a random variable distributed following a normal distribution and different standard deviations for each stock. The covariance between the random errors of the two stocks is zero.
# 
# Now, it is given that for period T, the P/E ratios of Stock A and Stock B are 20 and 10, respectively. We assumes that the relationship between the stock returns and the P/E ratios is stationary over time and across stocks.
# 
# Calculate the Z-scores of Stock A and Stock B using cross-sectional analysis (for period T) and then calculate the weights of a portfolio that contains both stocks and maximizes the Sharpe ratio using a graphical method.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,1,100)
sr = (2*w+(1-w))/np.sqrt(20*w**2+10*(1-w)**2)

print( w[np.argmax(sr)], np.max(sr) )


# In[2]:


plt.plot(w,sr)
plt.show()


# <img width="367" alt="Screenshot 2023-01-31 at 12 20 37 AM" src="https://user-images.githubusercontent.com/16545021/215672394-8e55458c-fbf4-47a2-8d31-dd5f894de9c1.png">
