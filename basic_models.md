# Basic Models in Financial Economics

Quantitative research in finance uses mathematical models to predict stock returns and volatility, which form the basis for stock selection. 
The central concept in financial economics is that a stock's average return reflects the reward for taking on risk.

Factor models express this risk-reward relationship by showing that a stock's average return is proportional to its exposure to different types 
of risk represented by factors, and the reward for each unit of exposure to the risk.

There are two main types of factor models:

- The Fundamental Factor Model: uses stock characteristics such as P/E ratio and market capitalization as factors.
- The Economic Factor Model: uses macroeconomic variables such as GDP and inflation, but it can also incorporate other types of factors.

# Modeling Stock Returns

Stock returns can be modeled as:
$r_i = α_i + β_{i1}f_1 + β_{i2}f_2+··· + β_{iK}f_K +ϵ_i$.
This equation can be used to determine the expected return and risk of each stock and portfolio, 
and then choose the optimal portfolio based on the results.

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

# Exercise:

Consider a world with only two stocks, Stock A and Stock B. The current stock returns, $r_{A,t+1}$ and $r_{B,t+1}$, are determined by the end-of-period price-to-earnings (P/E) ratios of the previous period. The equation for Stock A is:

$r_{A,t+1} = 0.1\times(P/E)\_{A,t} +ε_{A,t+1}, ε_{A,t+1}\~ N(0,20)$
The equation for Stock B is:
$r_{B,t+1} = 0.1\times(P/E)\_{B,t} +ε_{B,t+1}, ε_{B,t+1}\~ N(0,10)$

ε represents the random component of the stock return. The covariance between the random errors of the two stocks is zero.
For period T, the P/E ratio of Stock A is 20 and of Stock B is 10. Assume stationarity over time and across stocks.
Calculate the Z-scores of the above equations using cross-sectional analysis and calculate the weights of a portfolio comprising Stock A and Stock B that maximizes the Sharpe ratio using a graphical method.
