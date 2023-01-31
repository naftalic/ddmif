# Basic Models

The Fundamental Factor Model aims to explain a stock's expected return based on its fundamental characteristics, such as price-to-earnings ratio, market capitalization, and other financial metrics. The idea is that these characteristics are proxies for the underlying risk and growth prospects of a company, which in turn determines the expected return.

The Economic Factor Model, on the other hand, uses macroeconomic variables such as gross domestic product (GDP) and inflation as factors to explain expected returns. The premise is that macroeconomic conditions drive the performance of the overall economy, and in turn, affect the expected return of individual stocks. This type of model can also incorporate other factors, such as sector-specific variables, to provide a more comprehensive view of a stock's expected return.

Both types of factor models are used by quantitative investors to help inform investment decisions. The models provide a systematic way to analyze risk and reward and identify which stocks are likely to outperform based on their factor exposures. However, it's important to note that factor models are not perfect, and past performance does not guarantee future returns. Additionally, changes in economic conditions and company fundamentals can impact the expected return of a stock, and the factor model must be updated to reflect these changes.

# Modeling Stock Returns

The equation for modeling stock returns is known as the Capital Asset Pricing Model (CAPM), which is a widely used model in finance for explaining the relationship between stock returns and systematic risk. The model assumes that each stock's return can be decomposed into two components:

A stock-specific component ($α_i$) which is uncorrelated with the market and represents the expected return of the stock that is not related to systematic risk factors.

A market-related component ($β_{i1}f_1 + β_{i2}f_2 + ... + β_{iK}f_K$) that represents the stock's exposure to systematic risk factors ($f_1, f_2, ..., f_K$). Each factor's return contributes to the stock's return in proportion to the factor's sensitivity to the stock, represented by $β_i$.

The term $ϵ_i$ represents the residual, which is the difference between the actual stock return and the expected return given by the model. The residual represents the unsystematic risk, which is unique to each stock and can be diversified away by holding a well-diversified portfolio.

The CAPM can be used to determine the expected return and risk of each stock and portfolio, and then choose the optimal portfolio based on the results. The optimal portfolio is the one that maximizes expected returns for a given level of risk or minimizes risk for a given level of expected returns. This process is known as Modern Portfolio Theory (MPT) and it is a cornerstone of quantitative investing.


Steps to Form a Model and Make a Portfolio:

- Choose factors: Consider what kind of factors to use and how many factors to include in the model.

- Choose data: Select the type of data to use, such as cross-sectional, time series, or panel data.

- Determine factor exposures: Establish the relationship between the stock and the factors.

- Determine factor premia: The reward for each unit of exposure to a risk factor can be estimated using a zero-investment portfolio, which involves shorting one stock and using the proceeds to buy another stock.

- Determine expected return and risk: Estimate the stock's total risk, including nondiversifiable risk (market risks that can't be removed from the portfolio) and diversifiable risk (stock-specific risks that can be removed by diversifying holdings).

- Forecast: Consider past data vs future data, factor exposure stability, and factor premium changes.

- Weight the portfolio: Determine the objective for the portfolio.

The Fundamental Factor Model and the Economic Factor Model are equivalent if the expected stock return is linearly related to the fundamental factor exposure.


# Screening and Ranking Stocks

Many portfolio managers opt for a stock screening technique instead of a formal model for selecting stocks. Others use Z-scores to screen and rank stocks.

# Exercise

Consider a world with only two stocks, Stock A and Stock B. The current stock returns, $r_{A,t+1}$ and $r_{B,t+1}$, are determined by the end-of-period price-to-earnings (P/E) ratios of the previous period. 

The equation for Stock A is:
$r_{A,t+1} = 0.1\times(P/E)\_{A,t} +ε_{A,t+1}$, $ε_{A,t+1}\sim N(0,20)$.

The equation for Stock B is:
$r_{B,t+1} = 0.1\times(P/E)\_{B,t} +ε_{B,t+1}$, $ε_{B,t+1}\sim N(0,10)$.

ε represents the random component of the stock return. The covariance between the random errors of the two stocks is zero.
For period T, the P/E ratio of Stock A is 20 and of Stock B is 10. Assume stationarity over time and across stocks.
Calculate the Z-scores of the above equations using cross-sectional analysis and calculate the weights of a portfolio comprising Stock A and Stock B that maximizes the Sharpe ratio using a graphical method.

<img width="367" alt="Screenshot 2023-01-31 at 12 20 37 AM" src="https://user-images.githubusercontent.com/16545021/215672394-8e55458c-fbf4-47a2-8d31-dd5f894de9c1.png">

