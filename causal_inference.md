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

# Causal Inference in Finance

# Math background
The expected value, also known as the population mean, of a random variable is calculated as the weighted average of all possible values that the variable can take, where the weights are given by the probabilities of each value's occurrence in the population.

$$
\begin{align}
  E(X) & = x_1p(x_1)+x_2p(x_2)+\dots+x_kp(x_k) \\
  & = \sum_{j=1}^k x_jp(x_j).             
\end{align}
$$

The variance of a random variable in the population is defined as

$$
\begin{align}
   V(X)=\sigma^2 & = E\Big[\big(X-E(X)\big)^2\Big]\  \\
& = E\Big[\big(X^2-2XE(X)+E^2(X)\big)\Big]\  \\
& = E(X^2)-2E(X)E(X)+E^2(X) \\
& = E(X^2)-E^2(X).
\end{align}
$$

The variance of the sum of two random variables is equal to:

$$
\begin{align}
   V(X+Y)=V(X)+V(Y)+2C(X,Y)
\end{align}
$$

where $C(X,Y)$ is the covariance measuring the amount of linear dependence between two random variables X and Y.

