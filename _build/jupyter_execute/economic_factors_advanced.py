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
# The economic factor model has been the only factor model deemed valid in academia, with the fundamental factor model gaining recent credibility. However, the academic literature fails to distinguish between the two and uses the term multifactor pricing model to refer generally to factor models.
