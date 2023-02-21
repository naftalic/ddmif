#!/usr/bin/env python
# coding: utf-8

# # The Economic Factor Model
# 
# The previous chapter, fundamental factor model, covered tools to combine stock-level information to determine returns and risks. The economic factor model is another way to efficiently combine stock information but with a different twist on the factor model framework.
# 
# The economic factor model has the same structure as the fundamental factor model, with stock returns being the payoff for taking risk. However, the roles of factor exposure and factor premium are reversed. In the fundamental factor model, the factor exposure is observable in financial statements, whereas the factor premium must be estimated from a cross-sectional regression. In the economic factor model, the factor premium is the known (global) value, while the factor exposure must be estimated by a time-series regression of stock returns on factor premiums.
# 
# For example, an economic factor model with one factor, inflation, has the observed rate of inflation as the (global) factor premium, and the stock’s sensitivity or reactivity to inflation as the factor exposure, estimated as the relationship between the return on the stock and the rate of inflation. The economic factor model, therefore, assumes the premium that the market places on exposure to risk but requires the estimation of a particular stock’s exposure to risk.
# 
# Mathematically, the economic factor model defines the return to stock $i$, $r_i$, as
# 
# $$
# r_i=\alpha_i+\beta_i\cdot f+\epsilon_i
# $$
# 
# where $f=(f_1, ..., f_K)$ are factor premiums (which do not vary across stocks and so do not have the subscript $i$), and $\beta_i=β_{i,1}, ..., β_{i,K}$ are factor exposures (which do vary across stocks and have the subscript $i$). The term $α_i$ is the constant. The term $\beta_i\cdot f = β_{i,1}f_1 + ... + β_{i,K}f_K$ represents the nondiversifiable risk of the stock, and $ε_i$, the error, reflects the diversifiable risk of the stock. The model is similar to the fundamental factor model in this regard.
# 
# Similar to the fundamental factor model, the average stock return is
# 
# $$E(r_i) =\alpha + β_iE(f)$$
# 
# and the total risk of a stock
# 
# $$
# \begin{align}
# V(r_i) = \beta_i^TV(f)\beta_i+ V(\epsilon_i).
# \end{align}
# $$
# 
# The model can also express the stock return for a particular period. We use the lowercase letter "t" to denote a time period:
# 
# $$
# r_{i,t}=\alpha_i+\beta_i\cdot f_t+\epsilon_{i,t}.
# $$
# 
# It's important to note that the factor premium is denoted with a time subscript "t" because it varies over time. In other words, we consider the factor premium as a random variable with distinct values at different points in time. Conversely, the factor exposure does not have a time subscript "t" as it is assumed to remain constant over time. We view the factor exposure as an unknown parameter rather than a random variable.
# 
# # The model
# Similar to the previous chapter, the economic factor model is a tool for predicting the returns and risks of stocks, which helps portfolio managers make informed investment decisions. The process of formulating this model involves four steps:
# 
# 1) preliminary work, including choosing the factors, treating the risk-free rate, defining the data time frame and investment universe,
# 2) estimating the factor loadings or sensitivities of each stock to the selected factors,
# 3) estimating the factor premiums from historical data, and
# 4) evaluating total risk by estimating both the systematic risk (non-diversifiable risk) and idiosyncratic risk (diversifiable risk).
# 
# ## Pre analysis
# Before constructing an economic factor model, it is essential to plan carefully, just like in the fundamental factor model. The general decisions are the same, including the choice of factors, the treatment of the risk-free rate, and the sample makeup in terms of time interval, time period, and stock universe. Since the criteria for deciding how to treat the risk-free rate, determining the investment universe, and defining the time interval and period are the same for both models, we will focus only on factor selection.
# 
# The strength of the economic factor model is its ability to include practically all kinds of factors. The factors can be broadly categorized into three categories:
# 
# * Economic/behavioral/market factors: These factors include Gross Domestic Product (GDP), inflation, unemployment, interest rates, and other macroeconomic variables. It also includes survey-based indexes like consumer sentiment index, business confidence index, investor sentiment index, and returns on broad market indexes such as the Standard & Poor’s (S&P) 500 or other market group/industry indexes. Computation of these factors is minimal as relevant information is usually publicly available or provided by data vendors.
# * Fundamental/technical/analyst factors: These factors include financial statement information like the log of market capitalization, book-to-price ratio, earnings-to-price ratio, debt-to-equity ratio, and other firm characteristics. It also includes trading data like momentum, trading volume, and other information reflected in trading data. Additionally, it includes information provided by analysts like analyst rating changes, earnings revisions, or other information. Computation of these factors can be somewhat demanding, and even if obtained from an external source, the vendor's methodology should be examined carefully. Studies suggest that thoroughly vetted fundamental/technical/analyst factors predict stock returns more effectively than other factor groups.
# * Statistical factors: These factors are obtained from principal-component analysis applied to historical returns and require the highest level of computation.
# 
# Careful planning is critical when constructing an economic factor model. Factor selection is crucial, and the model can include various types of factors. Computation requirements vary depending on the category of the factor, with statistical factors requiring the most significant computation.
# 
# ## Benchmark and residual return
# Quantitative portfolio managers often manage their portfolios against a benchmark. As we discussed in previous chapters, it is not necessary to account for the benchmark at the outset of creating a model, but it can be useful to adjust for the effects of the benchmark when evaluating portfolio performance. There are two ways to incorporate the benchmark into the economic factor model.
# 
# One way is to remove the benchmark-related return from the stock return before building the model. To do this, we first regress stock returns on the benchmark returns and calculate the residual, which is the part of stock returns that is not correlated with the benchmark return. Then we construct an economic factor model for the residual stock return rather than the total stock return. The resulting model shows the relationship between the factor premium, the factor exposure, and the portion of the stock return that is above and beyond the benchmark return.
# 
# Another way is to explicitly include the benchmark in the economic factor model. If the benchmark is the broad-market index, the capital asset pricing model (CAPM) supports its inclusion in the model as a predictor of stock returns. Even if the benchmark is something other than the broad-market index, including it in the model will clarify the relationship between the portfolio and the benchmark.
# 
# 
# ## Factor premium
# To create the fundamental factor model, the portfolio manager gathers a dataset of many observations of stock returns and factor exposures, where the factor exposures change over time while the factor premium, a single statistically estimated proportion, remains constant. On the other hand, to construct the economic factor model, the portfolio manager needs to collect pairs of stock returns and factor premiums, where the factor premiums change over time. If there are K factors, the portfolio manager needs to find the factor premiums of the $K$ factors at each time interval $t$, $f_t = (f_{1,t}, ..., f_{K,t})$.
# 
# In the economic factor model, the factor premium is a known value, unlike the factor exposure, which is estimated through regression. However, it is not always possible to observe a factor premium directly. Computation for economic/behavioral/market factors is rather straightforward. For fundamental/technical/analyst factors, the computation is somewhat more demanding, while for statistical factors, it presents a significant challenge.
# 
# ### Factor Premium for Economic/Behavioral/Market Factors
# The process of obtaining factor premiums for economic, behavioral, and market factors is straightforward and does not require complex computations. The values can be obtained by referencing reliable sources. Common examples of economic premiums include the unemployment rate, consumer sentiment growth, and overall market return:
# 
# * To calculate the factor premium for unemployment, the unemployment rate can be obtained from the Bureau of Labor Statistics (BLS).
# * The growth rate of the consumer sentiment index can be obtained from the University of Michigan.
# * The market factor premium can be calculated as the difference between the S&P 500 total return and the one-month U.S. Treasury bill return.
# 
# Once all the factor premiums for a specific time interval are obtained, they can be stored in a set of vectors $f_t = (f_1, ..., f_T)$, where $f_t$ represents the factor premium for time $t$, and the first element of $f_t$ always represents the constant term in the return equation.
# 
# ### Factor Premium for Fundamental/Technical/Analyst Factors
# To calculate factor premiums for fundamental, technical, and analyst factors, additional computations are necessary. This involves constructing zero-investment portfolios and calculating their returns. To find the factor premium on value using the book-to-price (B/P) ratio as a proxy, we need to identify portfolios of stocks with high and low exposures to the value factor (i.e., high and low B/P ratios). We can start by ranking all the stocks at time $t$ in order of their B/P ratio, creating a high-value portfolio by equally weighting the top quartile of the list, and a low-value portfolio by equally weighting the bottom quartile. The zero-investment portfolio return is then calculated as the difference between the return on the high-value portfolio and the return on the low-value portfolio.
# 
# Careful consideration of the frequency of zero-investment portfolio construction is important, especially if the sorting variable is not frequently updated. For example, the book-to-price ratio is updated quarterly, while price is updated daily. Thus, creating a zero-investment portfolio too frequently may not reflect the information an investor needs.
# 
# It is important to note that a single piece of data can represent multiple types of factors. For instance, the same B/P ratio value can represent high exposure to a value factor or low exposure to a growth factor. The same numerical figure can stand for either factor, and the sign and name of the factor do not matter as long as we assign consistent meanings to high and low values.
# 
# ### Factor Premium for Statistical Factors
# Obtaining factor premiums for statistical factors is a complex computational process that involves principal-component analysis (PCA). This technique is readily available in standard computer software packages.
# 
# To begin, we estimate the variance-covariance matrix of stock returns, representing $N$ stock returns at time $t$ as an $N$-dimensional column vector, $r_t = (r_{1,t}, ..., r_{N,t})$. We have a total of $T$ such vectors $r_1, ..., r_T$. The variance-covariance matrix of returns $Σ$ is estimated as
# 
# $$
# \hat\Sigma=\frac{1}{T}\Sigma_{t=1}^{T} r^\top_tr_t-\bar r^\top\bar r
# $$
# 
# where $\bar r$ is the time averaged return vector.
# 
# Once we have the $N\times N$ variance-covariance matrix, we "diagonalize" it by finding an orthogonal matrix $Q$ (that is, $Q^{−1} = Q^\top$) such that
# 
# $$
# Q^\top \hat\Sigma Q = D
# $$
# 
# where $D$ is a diagonal matrix whose diagonal elements are eigenvalues (i.e., characteristic values) of $\hat\Sigma$. Each column of $Q$ is an orthonormal (i.e., of unit length) eigenvector corresponding to eigenvalues of $\hat\Sigma$.
# 
# To be more specific, we let $λ_1, ..., λ_N$ be the eigenvalues of $\hat\Sigma$ such that $λ_1 ≥ ... ≥ λ_N ≥ 0$. (Since $\hat\Sigma$ is a positive definite matrix, all the eigenvalues are positive.) Then matrix $D$ is constructed with ordered eigenvalues along its diagonal.
# 
# Let $q_1, ..., q_N$ be the orthonormal eigenvectors corresponding to $λ_1, ..., λ_N$. Matrix $Q$ is then constructed as $Q=(q_1,...,q_N)$.
# 
# If we want to find $K$ factors, we obtain $K$ factor premiums by weighting individual stock returns using the first $K$ columns of $Q$. That is, factor premiums $f_1, ..., f_K$ are defined as
# 
# $$
# f_{1,t}=q_1^\top r_t,..., f_{K,t}=q_K^\top r_t
# $$
# 
# These $K$ factors together have the **highest in-sample explanatory power** for $N$ stock returns among any set of $K$ explanatory variables constructed from linear combinations of $N$ stock returns.
# 
# ## Factor exposure
# 
# In the economic factor model, factor exposures are typically determined using time-series regression of stock returns on factor premiums. The regression coefficients, or factor exposures, measure the sensitivity of the dependent variable (the stock return) to changes in the independent variables (the factor premiums). Factor exposures are also known as factor sensitivities or factor loadings.
# 
# To estimate the factor exposure for a stock $i$ using $T$ periods of returns and factor premiums, $(r_{i,1}, ..., r_{i,T})$ and $(f_1, ..., f_T)$, we can use the following equation:
# 
# $$
# r_{i,t}=\alpha_i+\beta_if_t+\epsilon_{i,t}
# $$
# 
# where the coefficient $β_i$ is the factor exposure we want to discover, and $ε_{i,t}$ is the error term reflecting the diversifiable risk of stock returns. 
# 
# The ordinary least squares (OLS) estimator of βi is given by:
# 
# $$
# \hat\beta_i=\text{cov}(r_{i,t},f_t)/\text{var}(f_t)
# $$
# 
# and 
# 
# $$
# \text{var}(\hat\beta_i)=\hat \sigma_i^2/\text{var}(f_t)
# $$
# 
# where $\hat \sigma_i^2$ is the estimated variance of $ε_{i,t}$ that can can computed once we have $\hat\alpha$ and $\hat\beta$.
# 
# ## Factor exposure for small data
# Portfolio managers rely on time-series regressions to analyze stock returns and factor premiums. However, recent initial public offerings (IPOs) and stocks of merged or divested companies may lack sufficient data to conduct meaningful regressions. In such cases, we can infer a stock's factor exposures by using weighted factor exposures from groups of similar stocks as proxies for the original stock's exposures.
# 
# In the case of a merger, we can find the weighted average of the factor exposures of the premerger firms. We determine the appropriate weights using the market capitalizations of the premerger firms. Suppose that firm A and firm B recently merged. We can find the factor exposures of each firm separately using the stock returns of each firm, $r_{A,t}$ and $r_{B,t}$, respectively, and regressing factor premiums on those returns. The factor exposures of the merged firm, , can then be calculated using the formula:
# 
# $$
# \hat\beta_{AB}=\frac{s_A}{s_A+s_B}\hat\beta_A+\frac{s_B}{s_A+s_B}\hat\beta_B
# $$
# 
# where $s_A$ is the pre-merger market capitalization of firm A, and $s_B$ is the pre-merger market capitalization of firm B.
# 
# For recent IPOs, we can only rely on observable firm characteristics from financial statements. To find similar firms, we calculate the z-score for each of the M characteristics of each firm for which we already have factor exposures. Then we choose a small critical level e and find all firms j such that $(z_i − z_j)^\top(z_i − z_j) < e$ to identify the similar firms. Once we identify the similar firms, we can take the equal-weighted average of their factor exposures as the factor exposure of the IPO. This process of identifying similar firms is known as characteristic matching and can also be applied to searching for other characteristics, such as expected stock return.
# 
# An alternative to characteristic matching is using the industry-average figure. For instance, the average factor exposure of the entire pharmaceutical industry can stand in for the factor exposure of a new pharmaceutical company's stock. However, financial economic research suggests that characteristic matching is more effective than using the industry average.
# 
# ## Decomposition of risk
# The total risk of a stock return can be decomposed into nondiversifiable risk and diversifiable risk. Nondiversifiable risk depends on the factor exposure and variance of the factor premium, while diversifiable risk is equal to the variance of the error term:
# 
# $$
# V(r_i)=\beta_i^\top V(f)\beta_i+V(\epsilon_i)
# $$
# 
# We already have the estimate for $β_i$. We can obtain an estimate for $V(f)$ given the factor premium data $(f_1, ... ,f_T)$ and estimating $V(ε_i)$ is straightforward.
# 
# When finding the optimal portfolio, we need to know the correlation among stock returns. The correlation between two stock returns $r_i$ and $r_j$ has two components: the correlation between nondiversifiable components and the correlation between diversifiable components. The covariance between two stock returns can be estimated from factor exposure: $C(r_i,r_j)=\beta_i^\top V(f)\beta_j+C(ε_i, ε_j)$.
# 
# If T is not large enough, it is conventional to assume that $C(ε_i, ε_j)$ is zero.
