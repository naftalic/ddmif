#!/usr/bin/env python
# coding: utf-8

# # Factors
# 
# factors are crucial for financial modeling, and selecting the right ones is important for achieving outperformance. Good factors have a persistent and stable relationship with stock returns that can be explained by economic theory. The best way to find good factors is by using well-reasoned quantitative techniques rather than relying on superficial correlations produced by data mining. 
# 
# A factor in stock market analysis refers to any variable that has the ability to impact or predict stock returns. We can identify four broad types of factors:
# 
# - Fundamental Factors: Fundamental factors describe a company's financial condition and are calculated using data from the company's financial statements, such as the balance sheet, income statement, and cash flow statement. These factors are considered the most common in predicting stock returns and may include financial ratios, such as the price-to-earnings ratio, debt-to-equity ratio, or the return on assets ratio, among others. By analyzing these financial metrics, investors can gain insight into a company's financial health, earnings potential, and growth prospects.
# 
# - Technical Factors: Technical factors, on the other hand, are based on technical analysis and focus on the historical price and volume data of a stock. Technical analysts believe that patterns in the stock's price and volume movements can be used to predict future price movements. Technical factors include chart patterns, moving averages, trend lines, and momentum indicators, among others. These factors are used to make predictions about future price movements and to identify potential buying or selling opportunities.
# 
# - Economic Factors: Economic factors refer to broad macroeconomic trends and events that impact the stock market as a whole. For example, interest rates, inflation, gross domestic product (GDP), and unemployment are some of the most significant economic factors that can impact stock prices. Economic factors can have a direct effect on companies' earnings and can therefore affect the stock prices of individual companies and the overall stock market.
# 
# - Alternative Factors: Alternative factors refer to any factors that don't fall into the three categories mentioned above. They include a wide range of variables, such as sentiment indicators, news events, and company-specific events, among others. Alternative factors can be difficult to quantify and measure, but they can have a significant impact on stock prices, particularly in the short term. Alternative factors can help investors better understand the market sentiment and provide a complementary perspective to traditional fundamental and technical analysis.
# 
# ## Fundamental Factors
# The fundamental factors can be grouped into seven subcategories: valuation, size, operational efficiency, operating profitability, solvency, financial risk, and corporate activity. Valuation factors, such as the price-to-book (P/B) ratio and the price-to-earnings (P/E) ratio, help determine whether a stock is relatively cheap or expensive. Size factors, like market capitalization, attempt to categorize companies based on their size and examine the effect of size on stock return behavior. Operational efficiency factors, like inventory turnover, and operating profitability factors, like gross profit margin, offer insight into how well the company is being run by management. Solvency factors assess a company's ability to fulfill its short-term obligations in the future, with indicators such as the current ratio and the cash ratio. Financial risk factors, such as debt-to-equity and interest coverage ratios, gauge the financial stability of a company. Lastly, corporate activity factors pertain to decisions made by corporate executives or factors that do not fit into any of the other categories.
# 
# ## Technical Factors
# Technical factors are variables that are constructed from historical price and volume data, such as open prices, high prices, low prices, closing prices, volume, open interest, and bid and ask prices. Technical factors update themselves more frequently than fundamental factors and can be used to capture short-term changes in the relative value of stocks. Technical factors are categorized into four subcategories: liquidity risk factors, price-based factors, volume-based factors, and overall market movement factors.
# 
# Liquidity risk factors help assess the consequences of trading a stock. Price-based factors are generated mainly from stock prices or returns and are used to predict potential future price movements. Volume-based factors are created from past trading or volume data that may signal changing market participant behavior. Overall market movement factors are aggregate technical indicators that can provide insight into the stock market's overall movements and their implications for the near future.
# 
# ## Economic Factors
# Economic factors refer to variables that impact the overall macroeconomy and can have an effect on stock returns. These factors include popular indicators such as Gross Domestic Product (GDP) growth, yield-curve slope, unemployment, and inflation. These variables are usually considered in macroeconomic models of stock returns because they have the potential to influence a significant portion of the market. It is important for portfolio managers to be cautious while using macroeconomic data in their models because these data have a lag and might not be the latest available. They should also account for these delays when using the data in their models.
# 
# ## Alternative Factors
# Alternative factors are a group of factors used in financial analysis and modeling that do not fit into the traditional categories of fundamental, technical, and economic factors. There are three subcategories of alternative factors: analyst factors, captivus factors, and social responsibility factors. Analyst factors include information from Wall Street analysts such as earnings forecasts, buy-sell recommendations, and other relevant information that can be used to predict stock returns. Captivus factors include data captured through GPS, satellite, social media, or news feeds, often captured through sophisticated programs and with a higher frequency than traditional data sources, making it available earlier. Web scraping is a common method of obtaining captivus data. Lastly, social responsibility factors involve quantifying the relationships between management and employees, corporate governance, and issues related to diversity, including the composition of the board and discrimination practices.
# 
# # Factor choices
# The building of investment models is a combination of science and art. However, in quantitative portfolio management, the manager must have a deep understanding of financial and economic theory to choose and combine factors appropriately. There are two types of quantitative stock return models: the fundamental factor model and the economic factor model. To choose factors for the former, univariate and multiple regression techniques can be used, while for the latter, unidimensional and multidimensional zero-investment portfolio techniques are suggested. Additionally, a simple correlation statistic or rank-correlation statistic can be used to determine the correlation among factor choices, helping in combining and grouping factors.
# 
# ## Univariate Regression Tests
# Portfolio managers often use simple regressions as a way to simplify the process of searching for relevant factors in stock returns. They start by identifying a group of factors ($\beta_{i,t}$) that they believe could explain stock returns ($r_{i,t}$) and then run panel regressions on each factor versus the stock returns in the universe. The panel regression provides an estimate of the relationship between the factor and stock returns, and if a factor ($f$) has a significant value, it is considered useful in explaining stock returns.
# For example, 
# 
# $$r_{i,t}=\alpha +f\beta_{i,t}+\epsilon_{i,t}$$,
# 
# where $\beta_{i,t}$ is the factor exposure of stock $i$ at time $t$, and the estimate of $f$ from this panel regression will show the relationship between the factor and stock returns.
# 
# However, univariate regressions have a drawback in that they may lead to finding many variables that are significant in explaining stock returns but are actually surrogates for each other. For example, the P/E and P/B ratios may both explain stock returns, but they represent the same idea, so only one of them may be needed in the model. The ideal situation is to find factors that explain stock returns without being highly correlated with each other.
# 
# Despite these limitations, simple regressions are still used by many portfolio managers because they are easy to perform and provide an early idea of what might be relevant and what might not be. If there are too many potential factors, simple regressions can be used to make the first round of cuts. 
# 
# ## Multiple Regression Tests
# 
# ## Unidimensional Zero-Investment Portfolio
# 
# ## Multidimensional Zero-Investment Portfolio
# 
# ## Techniques to Reduce the Number of Factors
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

