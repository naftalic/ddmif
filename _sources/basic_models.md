---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 2) Basic Models

The Fundamental Factor Model aims to explain a stock's expected return based on its fundamental characteristics, such as price-to-earnings ratio, market capitalization, and other financial metrics. The idea is that these characteristics are proxies for the underlying risk and growth prospects of a company, which in turn determines the expected return.

The Economic Factor Model, on the other hand, uses macroeconomic variables such as gross domestic product (GDP) and inflation as factors to explain expected returns. The premise is that macroeconomic conditions drive the performance of the overall economy, and in turn, affect the expected return of individual stocks. This type of model can also incorporate other factors, such as sector-specific variables, to provide a more comprehensive view of a stock's expected return.

Both types of factor models are used by quantitative investors to help inform investment decisions. The models provide a systematic way to analyze risk and reward and identify which stocks are likely to outperform based on their factor exposures. However, it's important to note that factor models are not perfect, and past performance does not guarantee future returns. Additionally, changes in economic conditions and company fundamentals can impact the expected return of a stock, and the factor model must be updated to reflect these changes.

# Fundamental and economic factor models
The fundamental factor model and the economic factor model are two models that aim to explain the average stock return as the product of the factor premium ($f_k$) and the factor exposure ($β_{ik}$). However, there are some similarities and differences between the two models.

- Similarities:
Both models are based on the principle that the average stock return is determined by the factor premium ($f_k$) and factor exposure ($β_{ik}$).
The factor premium measures the amount that investors are willing to pay for each factor, while the factor exposure measures the sensitivity of the stock return to a factor.

- Differences:
Factor exposures are directly observable in the fundamental factor model, while they must be estimated in the economic factor model. In the fundamental factor model, exposures to fundamental factors can be obtained from financial statements and other data sources, while in the economic factor model, exposures to economic or other factors must be estimated from the historical relationship between stock returns and factor premiums.
The factor premium operates differently in the two models. In the fundamental factor model, the factor premium must be estimated from the historical relationship between stock returns and the factor exposures. In the economic factor model, the factor premium can be determined through methods such as zero-investment portfolios or principal-component analysis, or in some cases, it can be determined up to a proportionality without statistical estimation.

The economic factor model is considered better than the fundamental factor model because it measures the sensitivity of stocks to various economic risk factors, rather than relying on exposures as proxies for risk. The fundamental factor model, while it may be equivalent to the economic factor model if the relationship between stock returns and fundamental factor exposures is linear, is lacking in theoretical backing and econometric justification if the relationship is not linear, leading to a misspecified cross-sectional regression and incorrect estimation of the relationship. The economic factor model is therefore seen as a more accurate measure of underlying stock risk.

Both the fundamental factor model and the economic factor model attempt to explain stock returns by the product of the factor premium and exposure. However, the two models differ in the way factor exposures and premiums are determined and estimated.

# Modeling Stock Returns

The equation for modeling stock returns is known as the Capital Asset Pricing Model (CAPM), which is a widely used model in finance for explaining the relationship between stock returns and systematic risk. The model assumes that each stock's return can be decomposed into two components:

A stock-specific component ($α_i$) which is uncorrelated with the market and represents the expected return of the stock that is not related to systematic risk factors.

A market-related component ($β_{i1}f_1 + β_{i2}f_2 + ... + β_{iK}f_K$) that represents the stock's exposure to systematic risk factors ($f_1, f_2, ..., f_K$). Each factor's return contributes to the stock's return in proportion to the factor's sensitivity to the stock, represented by $β_i$.

The term $ϵ_i$ represents the residual, which is the difference between the actual stock return and the expected return given by the model. The residual represents the unsystematic risk, which is unique to each stock and can be diversified away by holding a well-diversified portfolio.

The CAPM can be used to determine the expected return and risk of each stock and portfolio, and then choose the optimal portfolio based on the results. The optimal portfolio is the one that maximizes expected returns for a given level of risk or minimizes risk for a given level of expected returns. This process is known as Modern Portfolio Theory (MPT) and it is a cornerstone of quantitative investing.

# Modeling process
The steps to form a model and make a portfolio are a process of choosing and analyzing various factors to estimate the expected return and risk of each stock and portfolio. The goal is to make informed investment decisions based on data and mathematical models.

- The first step is to choose factors. This involves considering what type of factors to include in the model and how many factors to use. The most commonly used factors in quantitative finance are the Fundamental Factor Model, which uses stock characteristics such as P/E ratio and market capitalization, and the Economic Factor Model, which uses macroeconomic variables such as GDP and inflation.

- The next step is to choose the type of data to use. There are three main types of data used in quantitative finance: cross-sectional, time series, and panel data. Cross-sectional data provides a snapshot of all stocks in the market at a given point in time, while time series data provides a historical view of a single stock. Panel data combines both cross-sectional and time series data.

- Once the factors and data have been selected, the next step is to determine the factor exposures, which is the relationship between the stock and the factors. This information is used to determine the expected return and risk of each stock and portfolio.

- The reward for each unit of exposure to a risk factor is known as the factor premium and can be estimated using a zero-investment portfolio. This portfolio involves shorting one stock and using the proceeds to buy another stock. The difference in return between these two stocks represents the factor premium.

- Expected return and risk are estimated by considering the total risk of each stock, including both diversifiable and non-diversifiable risks. Diversifiable risks are stock-specific and can be removed by diversifying holdings, while non-diversifiable risks are market risks that can't be removed from the portfolio.

- Finally, the portfolio is weighted based on the investment objective and the forecast for future performance. This includes considering past data versus future data, factor exposure stability, and changes in factor premiums.

In conclusion, the steps to form a model and make a portfolio involve a systematic process of choosing and analyzing factors, selecting data, and estimating expected returns and risks to make informed investment decisions.


# Screening and Ranking Stocks

A stock screening technique involves using specific criteria to identify stocks that meet certain investment goals. This technique is simpler than using a formal model, as it doesn't require in-depth analysis of factors and their exposures. Instead, it focuses on easily obtainable data points such as earnings growth, dividend yield, P/E ratio, or market capitalization.

Z-scores are a measure of how far a value is from the mean, expressed in terms of the standard deviation. In the context of stock selection, Z-scores can be used to rank stocks based on their deviation from the mean return of a particular factor, such as earnings growth or P/E ratio. Z-scores can help identify stocks that are undervalued or overvalued compared to their peers and provide a simple way to screen and rank stocks based on a specific factor.

While these techniques are quick and convenient, they may not provide a complete picture of a stock's risk and reward profile, and may not account for the dynamic relationships between different factors. Portfolio managers may opt to use a combination of these techniques and formal models to select stocks for their portfolio.

# Exercise

You are given a world with two stocks, Stock A and Stock B. The returns of the stocks in the next period, $r_{A,t+1}$ and $r_{B,t+1}$, are determined by their current Price-to-Book (P/B) ratios. 
The equations for Stock A and Stock B's returns are given as 

$r_{A,t+1} = 0.3\times(P/B)_{A,t} +ε_{A,t+1}$, $ε_{A,t+1}\sim N(0,9)$, and
$r_{B,t+1} = 0.2\times(P/B)_{B,t} +ε_{B,t+1}$, $ε_{B,t+1}\sim N(0,16)$.

As seen, the returns are influenced by the P/B ratios and their random components are represented by ε. ε is a random variable distributed following a normal distribution and different standard deviations for each stock. The covariance between the random errors of the two stocks is zero.

Now, it is given that for period T, the P/B ratios of Stock A and Stock B are 20 and 10, respectively. We assumes that the relationship between the stock returns and the P/B ratios is stationary over time and across stocks.

Calculate the weights of a portfolio that contains both stocks and maximizes the Sharpe ratio using a graphical method.

# Solution
```{code-cell}
---
mystnb:
  figure:
    align: center
    caption_before: true
    caption: This is my table caption, above the table
---
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell}
w = np.linspace(0,1,100)
sr = (0.3*20*w+0.2*10*(1-w))/np.sqrt(9*w**2+16*(1-w)**2)

print( w[np.argmax(sr)], np.max(sr) )
```

```{code-cell}
plt.plot(w,sr)
plt.show()
```

Since the objective function is not convex, we can use a non-convex optimization solver like the SLSQP algorithm from the SciPy library in Python.

Here's an implementation:

```{code-cell}
import numpy as np
from scipy.optimize import minimize

w = np.linspace(0, 1, 100)
sr = (0.3*20*w + 0.2*10*(1-w))/np.sqrt(9*w**2 + 16*(1-w)**2)

def objective(x):
    return -sr[np.argmax(sr)]

bounds = [(0, 1)]
initial_guess = np.array([0.5])

result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds)

print(f"Optimal value: {-result.fun:.4f}")
print(f"Optimal w: {w[np.argmax(sr)]:.4f}")
```
