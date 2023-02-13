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

# Probability and Regression background

## Expected value, variance, and covariance
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

The definition of covariance is 

$$
C(X,Y) = E(XY) - E(X)E(Y).
$$

If X and Y are independent, then $E(XY) = E(X)E(Y)$ and $C(X,Y)=0$, but $C(X,Y)=0$ doesn't imply independence as the dependency between X and Y can be nonlinear.

The covariance between two linear functions is:

$$
\begin{align}
   C(a_1+b_1X, a_2+b_2Y)=b_1b_2C(X,Y).
\end{align}
$$

The correlation between X and Y is defined as the scaled covariance. That is,

$$
\text{Corr}(X,Y) = \dfrac{C(X,Y)}{\sqrt{V(X)V(Y)}}.
$$

## Population model
This section focuses on cross-sectional analysis, where we collect a random sample from the population of interest. We consider two variables, X and Y, and aim to examine the relationship between them. The model we use 

$$
y=\beta_0+\beta_1x+u
$$

is based on the assumption that it holds true for the population. The equation defines a linear bivariate regression model. In models that aim to capture causal effects, the variables on the left side of the equation are considered as the effects, while those on the right side are considered as the causes.

The above equation includes a random variable called the error term, $u$, to account for other factors that may affect Y. It also assumes a linear relationship between X and Y by including a linear dependence. The coefficient of X is referred to as the intercept parameter, while the coefficient of Y is known as the slope parameter. These parameters describe the population, and our goal in empirical work is to estimate their values. However, we never observe these parameters directly because they are not data. Our task is to estimate these parameters using data and assumptions. To do this, we need credible assumptions to make accurate estimates using the data. In this simple regression framework, all unobserved variables that determine Y are encompassed by the error term $u$.

The first assumption that we make is that 

$$
E(u)=0
$$

and we can always adjust $\beta_0$ to acheive this goal. In example, 

$$
\begin{align}
   y=(\beta_0+E(u))+\beta_1x+(u-E(u)).
\end{align}
$$

The second assumption which is called the zero conditional mean assumption is that 

$$
E(u\mid x)=E(u) =0.
$$

It means that the expected value of $u$ given $x$, or the mean of the error term $u$ for each “slice” of the population $x$ is eqaul to zero for all x. It implies that $E(ux)=0$ as $E(ux)=E(u\mid x)E(x)=0$.

This assumption that $E(u\mid x)=0$ also results in

$$
E(y\mid x)=\beta_0+\beta_1x.
$$

which shows the population regression function is a linear function of $x$.

## Ordinary least squares (OLS)
Given data on $x$ and $y$, can we estimate the population parameters, $\beta_0$ and $\beta_1$? Let the pairs of $\{(x_i,y_i): i=1,2,\dots,n\}$ be random samples of size $n$ from the population. Plug any observation $i$ into the population equation to get $y_i=\beta_0+\beta_1x_i+u_i$ where we observe $y_i$ and $x_i$ but not $u_i$.

We now use the two population restrictions $E(u)=0$ and $E(u\mid x)=0$ to estimate $\beta_0$ and $\beta_1$:

$$
\begin{align}
  E(u) = E(y-\beta_0-\beta_1x)           \approx \dfrac{1}{n}\sum_{i=1}^n\Big(y_i-\widehat{\beta}_0-\widehat{\beta}_1x_i\Big) & = 0 \\
  E(ux) = E\Big(x[y-\beta_0-\beta_1x]\Big) \approx \dfrac{1}{n}\sum_{i=1}^n
  \Big(x_i \Big[y_i - \widehat{\beta}_0 - \widehat{\beta}_1 x_i \Big]\Big) & = 0                
\end{align}
$$

where $\widehat{\beta}_0$ and $\widehat{\beta}_1$ are the estimates from the data.

The first equation implies that $\widehat{\beta}_0=\overline{y}-\widehat{\beta}_1 \overline{x}$ where $\overline{y}$ and $\overline{x}$ are 
the sample averages. Pluging $\widehat{\beta}_0$ into the second equation gives

$$
\begin{align}
  \widehat{\beta}_1 & = \dfrac{\sum\limits_{i=1}^n (x_i-\overline{x}) (y_i-\overline{y})}{\sum\limits_{i=1}^n(x_i-\overline{x})^2 } = \dfrac{C(x,y)}{V(x)}
\end{align}
$$

where the last term is the sample covariance over the sample variance.

With the estimated $\widehat{\beta}_0$ and $\widehat{\beta}_1$ the fitted value for each $i$ is:

$$
\begin{align}
   \widehat{y}_i=\widehat{\beta}_0+\widehat{\beta}_1x_i
\end{align}
$$

The residual $\widehat{u}$ is now defined as the prediction error between $y$ and $\widehat{y}_i$. That is

$$
\begin{align}
   \widehat{u}_i & = y_i-\widehat{y}_i.
\end{align}
$$

Note that the residual is the difference between the actual value and the predicted value, which is known as the **prediction error**. This can be easily calculated using any sample of data. On the other hand, the **error term**, represented without the hat symbol, is not observable by the researcher as it includes all factors that affect the outcome but are not included in the model. The residual will be present in the data once the regression analysis has been performed, but the error term will never appear in the data. 


We had $E(u)=0$ and we approximated $u$ with $\widehat{u}$, so clearly,

$$
\sum_{i=1}^n \widehat{u}_i=0.
$$

By the same argument we get that

$$
\sum_{i=1}^n x_i \widehat{u}_i=0.
$$

Because the $\widehat{y}_i$ are linear functions of the $x_i$ the fitted values and residuals are uncorrelated too it follows that 

$$
\sum_{i=1}^n \widehat{y_i} \widehat{u_i}=0.
$$

## Expected value of OLS

So far, we have used a population model to explain simple regression, but our analysis has only been based on a sample of data. The OLS estimator is used to calculate residuals, which average to zero in the sample, regardless of any underlying model. Now, we need to study the statistical properties of the OLS estimator in the context of a population model and random sampling.

Mathematical statistics is concerned with the behavior of estimators across different samples of data. For example, if we repeat the sample multiple times, will we get the correct answer on average? The expected value of the OLS estimators, which represents the average outcome across all possible random samples, must be determined to determine whether the estimators are unbiased.

$$
E(\widehat{\beta})=\beta
$$

Unbiasedness means that if we could take as many random samples on $y$ as we want from the population and compute an estimate each time, the average of the estimates $\widehat{\beta}$ would be equal to $\beta$.

There are multiple assumptions that must be met for the OLS estimator to be unbiased:

* Linearity: The population relationship between the randoms $x$ and $u$ and $y$ is linear: $y=\beta_0+\beta_1 x+u$. It implies that $y$ is also random.
* Sampling: We draw random samples of size $n$ from the population: $y_i=\beta_0+\beta_1x_i+u_i$
* Sample variations: The sample outcomes are not all the same value. Without that, the denominator of the estimated slope $\sum\limits_{i=1}^n(x_i-\overline{x})^2$ is zero and the slope is undefined.
* The zero conditional mean assumption: In the population, the error term has zero mean given any value of the explanatory variable: $E(u\mid x) = E(u) = 0$.

Givent the above assumptions, let's now show that $\widehat{\beta}_1$ is an unbiased estimate of $\beta$:

The estimated slope is given as 

$$
\begin{align}
   \widehat{\beta}_1=\dfrac{\sum_{i=1}^n (x_i - \overline{x})y_i}{\sum_{i=1}^n (x_i - \overline{x})^2}.
\end{align}
$$

Let's expand the numerator first.

\begin{align}
   \sum_{i=1}^n (x_i - \overline{x})y_i & =\sum_{i=1}^n (x_i - \overline{x})(\beta_0+\beta_1 x_i+u_i)                                                                  
   \\
                & = \beta_0 \sum_{i=1}^n (x_i - \overline{x})+\beta_1 \sum_{i=1}^n (x_i - \overline{x})x_i+\sum_{i=1}^n (x_i+\overline{x}) u_i
   \\
                & =0+\beta_1 \sum_{i=1}^n (x_i - \overline{x})^2+ \sum_{i=1}^n (x_i - \overline{x})u_i                                         
   \\
                & = \beta_1 SST_x+\sum_{i=1}^n (x_i - \overline{x}) u_i                                                                        
\end{align}



