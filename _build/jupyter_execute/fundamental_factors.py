#!/usr/bin/env python
# coding: utf-8

# # 5) The Fundamental Factor Model
# 
# In financial economics, the average return of a stock is believed to be the reward for taking on risk. In a factor model, the risk exposure of a stock is represented by its factor exposure vector $\beta_i = (\beta_{i,1},...,\beta_{i,K})$. The factor premium vector $f = (f_1,...,f_K)$ represents the reward to an investor who takes on the risk by buying the stock.
# 
# The return on stock i can be expressed as:
# 
# $r_i = \alpha + β_1f_1 + β_2f_2 + ... + β_Kf_K + \epsilon_i = \alpha + \beta_i^T f + \epsilon_i$
# 
# where $\alpha$ is the constant term, $\beta_i$ and $f$ are the vector notations for the factor exposure and premium, and $\epsilon_i$ is the error term, representing the part of the stock return that does not depend on the K factors.
# 
# The fundamental factor model assumes that a stock's factor exposure, which is a measure of its exposure to a specific type of risk, can be represented by an **observable** characteristic such as market capitalization or book-to-market ratio. However, the factor premium, which represents the reward for taking on that risk, must be **estimated** through observation of the relationship between the average stock return and the factor exposure.
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
# The average stock return represents the reward for taking risk, but what exactly is this risk? Stock risk is composed of two parts: nondiversifiable risk and diversifiable risk.
# 
# Total risk  = Nondiversifiable risk + Diversifiable risk
# 
# Since diversifiable risk can be removed from a portfolio through diversification, the market only rewards exposure to nondiversifiable risk. Therefore, we can conclude that: **The average stock return is a reward for taking on nondiversifiable risk**.
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
# In this model, the total risk $V(r_i)$ of an investment can be decomposed into two components: the nondiversifiable component and the diversifiable component. The nondiversifiable component, which is the part of the risk rewarded by the market, is given by the product of the square of the factor exposure and the factor premium risk $V(f)$ (a $K\times K$ matrix), represented by the term $\beta_i^TV(f)\beta_i$. The diversifiable component, which can be reduced through diversification, is represented by the term $V(\epsilon_i)$. The model expresses each component of the total risk, allowing for a better understanding of the risk structure.
# 
# # The model
# The fundamental factor model is a tool for predicting the returns and risks of stocks, helping portfolio managers make informed investment decisions. The process of formulating this model involves four steps: 
# 1) pre-analysis work, including choosing the factors, treating the risk-free rate, defining the data time frame and investment universe, 
# 2) determining the factor exposures of each stock, 
# 3) estimating the factor premium and constant α from the factor exposure and returns, and 
# 4) evaluating total risk by estimating both the factor risk (nondiversifiable risk) and diversifiable risk.
# 
# 
# ## Pre analysis
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
# ## Benchmark and residual return
# Portfolio managers use a benchmark to measure the performance of their portfolios. To incorporate the benchmark into the fundamental factor model, one approach is to use the model to predict only the residual return, which is the part of the stock return not correlated with the benchmark. This can be achieved by running a regression of the stock return on the benchmark. The portfolio manager's value-added is wrapped up in the term $\alpha$. Alternatively, the benchmark can be added to the model as one of the factors. Accounting for the benchmark at this stage is not necessary, and some portfolio managers prefer to deal with it later in the process by controlling for tracking error.
# 
# ## Factor exposure
# Factor exposure measures a stock's risk exposure in the fundamental factor model based on an observable or easily calculable characteristic found on a price-volume chart or in a company's financial statements. The calculation of factor exposure is straightforward once the factors have been selected. Commonly used factors include the E/P ratio, B/P ratio, D/E ratio, LogSize (log of market cap), and momentum.
# 
# To ensure accurate factor exposure values, it's crucial to update them as they change over time. For monthly intervals (and to avoid look-ahead bias), factor exposure recorded at the start of the month, or at the end of the previous month, is commonly used.
# 
# However, when using financial statement data, caution must be exercised as companies may not immediately release statements after the fiscal quarter ends. For instance, the most recently available financial statements as of December 2022 may represent the second or third quarter of 2022.
# 
# In calculating financial ratios such as the E/P ratio, we use quarterly data. For example, as of December 2022, we use earnings from the 12-month period ending in August, July, or June, depending on the company's fiscal quarter end date. If the fiscal quarter ends in September, we exclude the earnings for the July-September quarter from our calculation. Similarly, we use figures for fiscal quarters ending on or before August to calculate the B/P and D/E ratios. In general, a two- to three-month lag is advisable between the end of a fiscal period and the availability of the corresponding data.
# 
# ## Factor premium
# In the fundamental factor model, the factor premium represents the payoff for each unit of factor exposure or risk that a stock holds. The factor premium is typically estimated using a panel regression of the stock return on the factor exposure. This estimation is possible because the premium is expected to remain relatively constant across stocks and over several years.
# 
# We can estimate the following equation using the returns of $N$ stocks over $T$ time periods, ${(r_{1,1}, ..., r_{N,1}), ..., (r_{1,T}, ..., r_{N,T})}$, and the factor exposures of $N$ stocks over $T$ time periods, ${(β_{1,1}, ..., β_{N,1}), ..., (β_{1,T}, ..., β_{N,T})}$:
# 
# $$
# \begin{align}
# r_{it}=\alpha+f\beta_{i,t}+\epsilon_{i,t}
# \end{align}
# $$
# 
# There are several methods available to estimate this equation, including the ordinary least squares (OLS) approach, which is the simplest. However, while the OLS estimator is easy to obtain, it may not always be the most reliable. As such, we recommend that portfolio managers perform several robustness checks on the OLS estimator and then decide whether to use a more sophisticated technique.
# 
# The OLS estimator for the factor premium $f$ is:
# 
# $$
# \hat{f}=\frac{\text{cov}(r,\beta)}{\text{var}(\beta)}, \text{ with }\text{var}(\hat f)=\frac{\hat\sigma^2}{\text{var}(\beta)}
# $$
# 
# and $\hat\sigma^2$ is the estimated variance of $\epsilon_{i,t}$ that can be calculated from the data as $\epsilon_{i,t}=r_{it}-\hat\alpha+\hat f\beta_{i,t}$.
# 
# It's important to recognize that a model is typically not an exact representation of reality, but rather a useful approximation. In statistics, discrepancies between the model and reality are referred to as specification errors. When estimating the factor premium in a regression, specification errors can arise, as with any other regression analysis. However, we should aim to create models that capture persistent and stable patterns.
# 
# To assess the robustness of our estimation, we can perform a robustness check to determine whether our factor premium estimates are stable in the face of minor changes to the estimation process. If the current estimation is not robust, alternative estimation techniques should be explored.
# 
# To perform a robustness check, it is possible to partition the dataset into several subsets based on different criteria such as time, sector, among others. By comparing the estimates obtained from these subsets, we can determine if the estimation is robust. Specifically, if the estimates are consistent across all subsets, we can conclude that the estimation is robust. One way to create these subsets is by dividing the dataset along the time dimension to evaluate the stability of the estimation over time.
# 
# ## MAD Estimator
# The ordinary least squares (OLS) method is susceptible to outliers because it seeks to minimize the sum of the squared residuals. If a robustness check reveals that the OLS estimator is highly unstable, an alternative estimation technique that is less vulnerable to outliers may be necessary.
# 
# The minimum absolute deviation (MAD) estimation, also referred to as median estimation, is one such alternative. MAD minimizes the sum of the absolute values of residuals instead of the squared residuals. This approach is less affected by outliers since it avoids squaring the residuals. Standard statistical software supports the MAD approach, making it easily implementable.
# 
# ## HAC standard error
# Despite its limitations, OLS estimation has been the standard empirical tool for many generations of empirical analysts. While adopting alternative estimation techniques may introduce additional errors, as each technique is based on its own set of assumptions, which may not be more realistic than the assumptions driving OLS. Therefore, a popular approach is to continue reporting the OLS estimates while adjusting for standard errors to relax certain OLS assumptions.
# 
# Specifically, when calculating standard errors, we can relax two OLS assumptions: (1) that all error terms of different stocks have the same variance (homoscedasticity assumption), and (2) that the error terms of different time periods are independent (no autocorrelation assumption). Heteroscedasticity- and autocorrelation-consistent (HAC) standard errors are the standard errors we obtain after relaxing these assumptions. However, certain restrictions on error terms still apply even with HAC standard errors. For instance, we do not allow error terms of different stocks to be correlated, although we allow error terms of one stock for different periods to be correlated. Additionally, HAC requires error terms of one stock for different periods to have the same variance, although we allow error terms of different stocks to have different variances.
# 
# These maintained assumptions ensure that the OLS estimates remain consistent, meaning they are correct if the sample size is large enough, though they may not be the most efficient estimates, and other estimates may be more precise.
# 
# ## Decomposition of risk
# To construct an optimal portfolio, it is important to consider the risk of the stock return. In the fundamental factor model, the risk of the stock return has two components: nondiversifiable risk captured by the factor premium estimate $\hat f\beta_i$ and diversifiable risk captured by the error term $ε_i$. The total risk of the stock return is the sum of these two risks.
# 
# Nondiversifiable risk arises from the randomness of the factor premium, and it can be measured by the sample variance obtained from a time series of factor premium and constant estimates. The diversifiable risk represents the part of the variation in the stock return that the variation in the model’s factors cannot explain and can be measured by the variance of the error term.
# 
# When finding the optimal portfolio, it is also important to consider the correlations between stock returns. The correlation between the returns on a pair of stocks consists of the correlation between their nondiversifiable components and the correlation between their diversifiable components. However, estimating the diversifiable component of the return can be challenging due to the large number of parameters to estimate and the minimal impact it has on the stock return for investors.
# 
# For these reasons, it is conventionally assumed that diversifiable risk is equal to zero. The total risk of a stock is composed of nondiversifiable risk and diversifiable risk, and the correlation between the returns of two stocks is estimated by their nondiversifiable components.
