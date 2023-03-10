#!/usr/bin/env python
# coding: utf-8

# # Causal Inference in Finance
# 
# # Probability and Regression background
# 
# ## Expected value, variance, and covariance
# The expected value, also known as the population mean, of a random variable is calculated as the weighted average of all possible values that the variable can take, where the weights are given by the probabilities of each value's occurrence in the population.
# 
# $$
# \begin{align}
#   E(X) & = x_1p(x_1)+x_2p(x_2)+\dots+x_kp(x_k) \\
#   & = \sum_{j=1}^k x_jp(x_j).             
# \end{align}
# $$
# 
# The variance of a random variable in the population is defined as
# 
# $$
# \begin{align}
#    V(X)=\sigma^2 & = E\Big[\big(X-E(X)\big)^2\Big]\  \\
# & = E\Big[\big(X^2-2XE(X)+E^2(X)\big)\Big]\  \\
# & = E(X^2)-2E(X)E(X)+E^2(X) \\
# & = E(X^2)-E^2(X).
# \end{align}
# $$
# 
# The variance of the sum of two random variables is equal to:
# 
# $$
# \begin{align}
#    V(X+Y)=V(X)+V(Y)+2C(X,Y)
# \end{align}
# $$
# 
# where $C(X,Y)$ is the covariance measuring the amount of linear dependence between two random variables X and Y.
# 
# The definition of covariance is 
# 
# $$
# C(X,Y) = E(XY) - E(X)E(Y).
# $$
# 
# If X and Y are independent, then $E(XY) = E(X)E(Y)$ and $C(X,Y)=0$, but $C(X,Y)=0$ doesn't imply independence as the dependency between X and Y can be nonlinear.
# 
# The covariance between two linear functions is:
# 
# $$
# \begin{align}
#    C(a_1+b_1X, a_2+b_2Y)=b_1b_2C(X,Y).
# \end{align}
# $$
# 
# The correlation between X and Y is defined as the scaled covariance. That is,
# 
# $$
# \text{Corr}(X,Y) = \dfrac{C(X,Y)}{\sqrt{V(X)V(Y)}}.
# $$
# 
# ## Population model
# This section focuses on cross-sectional analysis, where we collect a random sample from the population of interest. We consider two variables, X and Y, and aim to examine the relationship between them. The model we use 
# 
# $$
# y=\beta_0+\beta_1x+u
# $$
# 
# is based on the assumption that it holds true for the population. The equation defines a linear bivariate regression model. In models that aim to capture causal effects, the variables on the left side of the equation are considered as the effects, while those on the right side are considered as the causes.
# 
# The above equation includes a random variable called the error term, $u$, to account for other factors that may affect Y. It also assumes a linear relationship between X and Y by including a linear dependence. The coefficient of X is referred to as the intercept parameter, while the coefficient of Y is known as the slope parameter. These parameters describe the population, and our goal in empirical work is to estimate their values. However, we never observe these parameters directly because they are not data. Our task is to estimate these parameters using data and assumptions. To do this, we need credible assumptions to make accurate estimates using the data. In this simple regression framework, all unobserved variables that determine Y are encompassed by the error term $u$.
# 
# * The first assumption that we make is that 
# $$
# E(u)=0
# $$
# and we can always adjust $\beta_0$ to acheive this goal. In example, 
# $$
# \begin{align}
#    y=(\beta_0+E(u))+\beta_1x+(u-E(u)).
# \end{align}
# $$
# 
# * The second assumption is that 
# $$
# E(u\mid x)=0.
# $$
