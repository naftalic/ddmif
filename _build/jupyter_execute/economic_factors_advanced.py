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
# ## Factor premium
