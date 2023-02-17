#!/usr/bin/env python
# coding: utf-8

# # The Fundamental Factor Model
# 
# In financial economics, the average return of a stock is believed to be the reward for taking on risk. In a factor model, the risk exposure of a stock is represented by its factor exposure vector $\beta_i = (\beta_{i,1},...,\beta_{i,K})$. The factor premium vector $f = (f_1,...,f_K)$ represents the reward to an investor who takes on the risk by buying the stock.
# 
# The return on stock i can be expressed as:
# 
# $r_i = \alpha + β_1f_1 + β_2f_2 + ... + β_Kf_K + \epsilon_i = \alpha + \beta_i^T f + \epsilon_i$
# 
# where $\alpha$ is the constant term, $\beta_i$ and $f$ are the vector notations for the factor exposure and premium, and $\epsilon_i$ is the error term, representing the part of the stock return that does not depend on the K factors.
# 
# The fundamental factor model assumes that a stock's factor exposure, which is a measure of its exposure to a specific type of risk, can be represented by an observable characteristic such as market capitalization or book-to-market ratio. However, the factor premium, which represents the reward for taking on that risk, must be estimated through observation of the relationship between the average stock return and the factor exposure.
# 
# ## Return 
# 
# Using the assumption that the average $\epsilon_i$ is zero, we calculate the average stock return as
# 
# $$E(r_i) = E(\alpha) + E(β_if)+E(\epsilon_i)=\alpha + β_iE(f)$$
# 
# where $\alpha$, and $β_i$ are constants and $E(\epsilon_i)=0$. Hence, the average stock return is simply the product of the factor exposure and the factor premium.
# 
# ## Risk
# 
# The average stock return represents the reward for taking risk, but what exactly is this risk? Stock risk is composed of two parts: diversifiable risk and nondiversifiable risk.
# 
# Total risk  = Nondiversifiable risk + Diversifiable risk
# 
# Since diversifiable risk can be removed from a portfolio through diversification, the market only rewards exposure to nondiversifiable risk. Therefore, we can conclude that: The average stock return is a reward for taking on nondiversifiable risk.
# 
# The risk that cannot be diversified away can be represented as the square of the factor exposure multiplied by the risk per unit of exposure, referred to as the factor risk. Thus, Nondiversifiable risk = factor exposure^2 * factor risk.
# 
# Within the framework of the fundamental factor model, the total risk of a stock (nondiversifiable risk plus diversifiable risk) can be measured by the variance:
# 
# $$
# \begin{align}
# V(r_i) &= V( \alpha + β_1f_1 + β_2f_2 + ... + β_Kf_K + \epsilon_i)\newline
# &= V( \alpha) + V(β_1f_1 + β_2f_2 + ... + β_Kf_K) + V(\epsilon_i)\newline
# &= V(β_1f_1 + β_2f_2 + ... + β_Kf_K)+ V(\epsilon_i)\newline
# &= \beta_i^TV(f)\beta_i+ V(\epsilon_i)
# \end{align}
# $$
# 
# In this model, the total risk $V(r_i)$ of an investment can be decomposed into two components: the nondiversifiable component and the diversifiable component. The nondiversifiable component, which is the part of the risk rewarded by the market, is given by the product of the square of the factor exposure and the factor premium risk $V(f)$, represented by the term $\beta_i^TV(f)\beta_i$. The diversifiable component, which can be reduced through diversification, is represented by the term $V(\epsilon_i)$. The model expresses each component of the total risk, allowing for a better understanding of the risk structure.
# 
# 
# The fundamental factor model is a tool for predicting the returns and risks of stocks, helping portfolio managers make informed investment decisions. The process of formulating this model involves four steps: 
# 1) preliminary work, including choosing the factors, treating the risk-free rate, defining the data time frame and investment universe, 
# 2) determining the factor exposures of each stock, 
# 3) estimating the factor premium and constant α from the factor exposure and returns, and 
# 4) evaluating total risk by estimating both the factor risk (nondiversifiable risk) and diversifiable risk.
# 
# 
# # Preliminary Work
# The preliminary work in constructing a sound portfolio model involves making crucial decisions that serve as the foundation of the model. The most important decision is choosing the factors that represent risk, which can be fundamental (e.g. dividend yield, debt-to-equity ratio), technical (e.g. 12-month momentum), or analyst (e.g. analyst rating changes) and are selected based on their ability to capture the characteristics of the stock or market conditions accurately.
# 
# In addition to choosing the factors, the portfolio manager must also decide on the shape of the data set, including the nature of stock returns, the interval between data points, and the overall time horizon. These decisions significantly impact the accuracy of the factor model.
# 
# The treatment of the risk-free rate is another key decision that must be made in the preliminary stage. The objective is to focus on the portion of the stock return that rewards risk. To achieve this, some portfolio managers subtract a risk-free rate from the stock return. Although it's a theoretically sound move, finding a truly risk-free asset to use as the risk-free rate is challenging. Despite this difficulty, subtracting an estimated risk-free rate is believed to provide more accurate results.
# 
# Finally, the portfolio manager must select the time interval and time period for the data set. The time interval refers to the frequency of collecting data points (e.g. daily or weekly), while the time period refers to the overall length of the data set (e.g. 5 years). These decisions affect the amount of data available for analysis and should align with the goals of the portfolio model.
# 
# In addition to the questions regarding the nature and time span of the data, the portfolio manager must decide on the number of stocks to consider when applying the model. There may already be external restrictions on the investment universe of the portfolio, or the portfolio manager may have a preliminary screening strategy to narrow down the list of potential investments.
# 
# In the absence of external restrictions, the number of stocks is not a technological issue given the current state of computing technology. A personal computer can handle thousands of stocks without much difficulty. However, the size of the stock universe does affect some aspects of implementation. A large investment universe provides a vast pool of stocks to select from, but calculation of stock correlations becomes less precise as the number of stocks increases, making the model less reliable. For this reason, we do not recommend starting with an investment universe of more than a few thousand stocks.
# 
# # Benchmark and residual return
# Portfolio managers use a benchmark to measure the performance of their portfolios. To incorporate the benchmark into the fundamental factor model, one approach is to use the model to predict only the residual return, which is the part of the stock return not correlated with the benchmark. This can be achieved by running a regression of the stock return on the benchmark. The portfolio manager's value-added is wrapped up in the term $\alpha$. Alternatively, the benchmark can be added to the model as one of the factors. Accounting for the benchmark at this stage is not necessary, and some portfolio managers prefer to deal with it later in the process by controlling for tracking error.
# 
# # Factor exposure
# Factor exposure is a measure of a stock's risk exposure in the fundamental factor model, determined by an observable or easily calculable characteristic that can be found on a price-volume chart or in a company's financial statements. Once the factors have been selected, calculating factor exposure is typically a simple task.
# 
# Some commonly used factors include the E/P ratio, which is the annual earnings per share divided by the share price, the B/P ratio, which is the value of common equity reported in the balance sheet divided by the share price, the D/E ratio, which is the total value of liabilities divided by the total value of equity reported in the balance sheet, LogSize, which is the natural log of the company's market capitalization (in millions of dollars), and Momentum, which is the average monthly return over the previous 12 months expressed as a percentage.
