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
\begin{align}
  E(X) & = x_1p(x_1)+x_2p(x_2)+\dots+x_kp(x_k) \\
  & = \sum_{j=1}^k x_jp(x_j)              
\end{align}

The variance of a random variable in the population is defined as
\begin{align}
   V(X)=\sigma^2=E\Big[\big(X-E(X)\big)^2\Big]\ =E(X^2) - E(X)^2
\end{align}
The last identity follows from the fact that 
\begin{align}
E\Big[\big(X-E(X)\big)^2\Big]\  =
& = E\Big[\big(X^2-2XE(X)+E^2(X)\big)\Big]\
& = E(X^2)-2E(X)E(X)+E^2(X)\
& = E(X^2)-E^2(X)\
\end{align}

\begin{align}
  \sum_{i=1}^n(x_i-\overline{x})^2 & =                                                                                               
  \sum_{i=1}^n (x_i^2-2x_i\overline{x}+\overline{x}^2)
  \\
  & = \sum x_i^2 - 2\overline{x} \sum x_i +n\overline{x}^2                                          \\
  & = \sum x_i^2 - 2 \dfrac{1}{n} \sum x_i \sum x_i +n\overline{x}^2                                \\
  & = \sum x_i^2 +n\overline{x}^2 - \dfrac{2}{n} \bigg (\sum x_i \bigg )^2                          \\
  & = \sum x_i^2+n\bigg (\dfrac{1}{n} \sum x_i \bigg)^2 - 2n \bigg (\dfrac{1}{n} \sum x_i \bigg )^2 \\
  & = \sum x_i^2 - n \bigg (\dfrac{1}{n} \sum x_i \bigg )^2                                         \\
  & = \sum x_i^2 - n \overline{x}^2                                                                 
\end{align}

A more general version of this result is:
\begin{align}
   \sum_{i=1}^n(x_i-\overline{x})(y_i-\overline{y}) & = \sum_{i=1}^n x_i(y_i - \overline{y}) \\
    & = \sum_{i=1}^n (x_i - \overline{x})y_i \\
    & = \sum_{i=1}^n x_iy_i - n(\overline{xy}) \\
\end{align}

