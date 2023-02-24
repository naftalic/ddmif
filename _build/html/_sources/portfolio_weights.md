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

# 7) Portfolio Weights

In the previous chapters, we discussed various ideas for stock selection that are crucial in identifying good and bad stocks. However, constructing a portfolio requires more than just identifying individual stocks. A skilled manager needs to assign relative weights to the stocks to create a cohesive portfolio.

There are several ways to generate stock weights, ranging from simple methods like equal weighting or market capitalization weighting to more complex techniques based on modern portfolio theory. For portfolio managers who manage against a benchmark, there are additional weighting possibilities, such as ensuring the weighted-average factor exposures of the portfolio match those of the benchmark or maximizing excess expected return while limiting tracking error.

To minimize tracking error or risk when weighting stocks, the manager needs to know each stock's expected return, risk or variance, and covariances among stocks. Additionally, the manager may want to impose constraints on the portfolio creation process, such as prohibiting short sales or upholding diversification rules. The manager can then use a quadratic optimizer to determine the optimal weights for the portfolio.

We begin by discussing two methods for creating a portfolio that is not managed against a benchmark: ad hoc methods that use rules of thumb to weight stocks and the mean-variance optimization method, which minimizes the portfolio's total risk given its expected return. We then explore the four potential approaches to creating a portfolio that is managed against a specific benchmark, including ad hoc weighting methods, stratification, factor exposure targeting, and tracking-error minimization. Of these techniques, only those that minimize risk have theoretical rigor, but they also require a larger skill set, more time, and more effort than the less quantitatively precise methods.

# Ad hoc methods
After selecting the stocks for a portfolio, there are several ad hoc methods for determining the portfolio weights. The two most common are equal weighting and value weighting.

Equal weighting assigns the same weight to every stock, regardless of market capitalization or other factors. For example, if there are 10 stocks in the portfolio, each stock will have a weight of 0.1 (= 1/10). While this approach is simple and quick, it does not consider the expected returns or risks of the stocks and may not be suitable for portfolios where such information is available.

Value weighting, on the other hand, assigns weights proportional to the stocks' market capitalizations. For example, if the market capitalization of stock A is twice as great as that of stock B, then the weight of stock A will also be twice the weight of stock B. This method ensures that the portfolio's performance matches that of the market average, but it still does not reflect the expected returns or risks of individual stocks.

There are variations of value weighting, such as weighting stocks by the square root or cube root of their market capitalization, which reduces bias towards large stocks. Another ad hoc weighting method is price weighting, where the portfolio manager buys the same number of shares in each stock so that the weights are proportional to the stock prices. This is how the Dow Jones Industrial Average and the Nikkei 225 are calculated.

Other ad hoc weighting methods may be used for benchmarked portfolios, which will be discussed later. Ultimately, the choice of weighting method will depend on the portfolio manager's information and objectives.

# Mean-variance optimization method
Standard Mean-Variance Optimization (MVO) is a technique used to identify the portfolio with the lowest risk given the mean and variance of future stock returns. To accomplish this, we theoretically compare the ex-ante risks and expected returns of all potential portfolios with identical expected returns, computed from the variances and covariances of the returns of all stocks. Quadratic programming is then used to find the minimum-risk portfolio without the need to calculate every portfolio's risk and return explicitly.

However, MVO has its limitations, as estimation errors could result in overweighting certain outlier stocks with low variances or high means. To mitigate this risk, additional portfolio constraints, such as short-sale, diversification, or sector constraints, may be imposed to limit the maximum and minimum stock weights. It is crucial to strike a balance between the constraints to avoid contradiction.

The portfolio manager's role is to carefully evaluate the estimation errors and decide on the necessary constraints, while allowing the optimizer to handle the rest. Nonetheless, caution must be taken not to over-constrain the portfolio and avoid hindering the full investment of the portfolio.


## No constraints
Using MVO without any additional constraints requires building a model of expected stock returns and risk, either by utilizing previously discussed models or by using commercial software models in combination with excess-return models. The portfolio manager begins by incorporating all relevant information about individual stock returns into a column vector μ and a matrix Σ, where μ represents the expected returns of individual stocks and Σ represents the variances and covariances of individual stock returns. 
Thus,

$$
\mu^\top = 
\begin{bmatrix}
E(r_1)\\
.\\
.\\
E(r_N)
\end{bmatrix}
$$

and 

$$
\Sigma = 
\begin{bmatrix}
V(r_1)      & C(r_1,r_2) &\cdots & C(r_1,r_N) \\
C(r_2,r_1)  & V(r_2)     &\cdots & C(r_2,r_N) \\
.           & .          &\cdots & .          \\
.           & .          &\cdots & .          \\
C(r_N,r_1)  & C(r_N,r_2) &\cdots & V(r_N)     \\
\end{bmatrix}
$$

A valid portfolio is specified by an $N$-dimensional column vector of stock weights, $w$, where the weight of each stock is represented by $w_i$. The sum of all elements in w must equal 1.

The expected return of the portfolio is given by $w^\top μ$, while the risk of the portfolio is represented by $w^\top Σw$, where $w^\top$ represents the transpose of the weight vector. The portfolio with the minimum risk and expected return of $μ_P$ is obtained by minimizing the objective function $w^\top Σw$ while satisfying the constraint $w^\top μ = μ_P$. This is a quadratic optimization problem, and mathematicians have developed quadratic programming to solve it.

The quadratic minimization problem with **equality** constraints can be rewritten as a set of linear constraints, which have a **closed-form** solution. 

To create a minimal-risk portfolio for a given level of expected return, we begin the optimization procedure using the expected return of the lowest expected return stock. We increment the mean return and repeat the optimization until we reach the expected return of the security with the highest mean return. We plot all the points in the diagram and connect them to produce the efficient frontier. The expected-return–expected-risk profile we desire can then be selected from the efficient frontier, and we can pick the weights of the corresponding stocks.

## Short-Sale and Diversification Constraints

Investment portfolio managers may face various constraints, such as legal restrictions or prospectus mandates, that limit their investment options. One of the main constraints faced by long-only portfolio managers is the short-sale restriction, which prohibits shorting securities. Mathematically, this restriction can be represented as the condition that each stock has a weight of at least zero:

$$
w\ge 0
$$

However, this is an inequality constraint, and quadratic optimization problems with inequality constraints do not have a simple analytical solution, requiring numerical methods instead. Techniques designed to solve these types of problems are known as quadratic programming, which can be easily entered into commercial software or a quadratic optimizer.
When using the same data as before and applying quadratic optimization programming with short-sale constraints, the efficient frontier shifts to the right. This is because the additional constraint increases the lowest-risk portfolio's risk. 

In addition to short-sale constraints, portfolio managers may also want to impose diversification constraints to comply with the [Investment Company Act of 1940](https://en.wikipedia.org/wiki/Investment_Company_Act_of_1940) or to reduce diversifiable risk. Such constraints can be expressed as maximum and minimum allowed weight vectors and added easily to the optimization problem, satisfying both the short-sale and diversification constraints simultaneously.
For example,

$$
\underline w \le w \le \overline w
$$

where $\underline w$ and $\overline w$  are $N$-dimensional vectors of minimum and maximum allowed weights.

# Sector or Industry Constraints
Portfolio managers, particularly those who manage against a benchmark, often aim to limit the sector weightings of their portfolio. To achieve this, a straightforward modification can be made to the framework by constraining the sector weightings using the following formula:

$$
\underline w_j \le w_j \le \overline w_j
$$

## Trading-Volume Constraint
One common constraint added to optimization by portfolio managers is the trading-volume constraint, which is particularly relevant when managing large portfolios that could have a significant price impact on the market. To avoid negative price impact, portfolio managers may restrict the holdings of each stock to a certain threshold amount, often a fraction of the average trading volume of each stock.

For example, if a portfolio is valued at $500 million and the manager wishes to keep the holding of one stock below 10% of its average daily trading volume (ADV), the constraint can be expressed as 

$$
500w_i \le 0.1x_i
$$

where $w_i$ is the portfolio weight of stock $i$ and $x_i$ is the average trading volume of stock $i$ measured in millions of dollars.

## Risk-Adjusted Return
In the previous section, we presented the mean-variance optimization problem as a risk minimization problem. However, some portfolio managers may prefer an alternative formulation that focuses on expected return maximization instead. This can be expressed as follows: maximize $μ_P$ subject to other constraints.
The expected return maximization formulation may be more useful if the portfolio manager has a specific target risk level $σ_P$, while the risk minimization may be more appropriate if the portfolio manager has a target expected return.
For example,


$$
\max\limits_w w^\top\mu\text{ s.t. } w^\top\Sigma w = \sigma_P \text{ or } \min\limits_w w^\top\Sigma w\text{ s.t. } w^\top\mu = \mu_P.
$$


In cases where the portfolio manager has neither a target risk nor a target expected return, the mean-variance optimization can be expressed in terms of risk-adjusted expected return. This can be achieved by adjusting the expected return for the risk, which is done by subtracting some multiple of the risk, i.e., $μ_P - Aσ^2$. Here, A is the risk-aversion parameter, and a high value of A indicates that the portfolio manager considers the risk to be very costly.

For instance, if the value of A is 2, it means that the portfolio manager equates a 1% increase in the variance with a 2% decrease in the expected return. Once the value of the risk-aversion parameter is determined, the mean-variance problem can be formulated as follows:

$$
\max\limits_w μ_P - Aσ^2
$$

subject to other constraints.

This formulation can be useful in certain applications, as it allows the portfolio manager to balance the trade-off between expected return and risk.

# Benchmark
Benchmarking is a common practice for portfolio managers. While some managers strictly adhere to the benchmark, known as index managers, others take a more flexible approach and are called active or enhanced index managers. **The aim of active managers is to generate returns that exceed the benchmark while maintaining a portfolio that is broadly similar to it**. Striking a balance between outperforming the benchmark and adhering to it can be challenging, but it becomes easier when the benchmark is not efficient. To achieve outperformance, managers can utilize various techniques such as ad hoc methods, stratification, factor exposure targeting, and tracking error minimization. Among these, the most popular method is tracking error minimization, as it offers the highest level of risk control while still giving the manager the freedom to select preferred stocks.


## Ad hoc
A straightforward way to ensure that a benchmarked portfolio closely tracks its benchmark is by using a simple weighting approach. This involves selecting the largest holdings in the benchmark and including them in the portfolio. For example, if the portfolio is meant to include 50 stocks, the 50 stocks with the largest market capitalization in the benchmark could be chosen. The weights of these 50 stocks can then be computed based on their relative market capitalizations. If desired, a manager could adjust the weights slightly to favor their preferred stocks.

Several approaches exist for adjusting weights to favor preferred stocks. Assuming that the portfolio manager has used the aggregate z-score methodology explained earlier to rank stocks, the manager should renormalize the aggregate z-scores such that the sum of the z-scores of the chosen subset of 50 stocks (or any number of stocks selected) equals zero. To modify the relative market capitalization weighting, the following steps should be taken: First, the manager must determine the maximum percentage deviation in weight that they are willing to allow from the market-cap weighting for the highest absolute z-score value. This value is denoted as η. Second, identify the highest absolute z-score of all the stocks within the 50-stock universe by taking the absolute value of all individual z-scores and finding the maximum, which is denoted as $z_\text{max}$. Third, compute the z-score multiplier $m = η/z_\text{max}$. Finally, compute the new weights of the portfolio using the formula $(w_i + mz_i)$, where $w_i$ represents the relative market capitalization weight within the benchmark. After completing these steps, the adjusted portfolio is ready.

While selecting the largest holdings of the benchmark for a portfolio is one way to track the benchmark, it is not the optimal solution. This method does not consider minimum tracking error versus the index, nor does it control for other risk factors or asset-specific risk. Additionally, the small number of stocks in the portfolio represents only a fraction of the benchmark's total market capitalization, making it an inefficient approach.

While other ad hoc methods exist, a professional portfolio manager would likely find them unsatisfactory due to their amateurish nature. Ultimately, a manager seeks to quantify their risk versus the benchmark, something that these other methods cannot achieve.

## Stratification
Stratification, also known as stratified sampling, is a simple method for building portfolios while maintaining a basic risk control mechanism. It was originally developed for statisticians who wanted to understand the characteristics of a population without having to observe every member. The method involves dividing the stock universe into nonoverlapping groups, or strata, based on certain characteristics, such as industry or size. From each stratum, a proportion of stocks is chosen to create a representative sample of the universe, while minimizing risk exposure across multiple dimensions.

To use stratification for portfolio management, the portfolio manager would first predict the excess returns of all stocks in the universe and then aim to choose high-alpha stocks while controlling risk versus the benchmark. After dividing the stock universe into strata, the manager would select representative stocks from each stratum based on some criterion, such as z-score or expected return. Suppose the stock universe is categorized by sectors and the portfolio manager needs to select four stocks from the transportation sector. In that case, the manager may opt to choose the stocks with the highest ranking based on future risk-adjusted returns.

Although stratification provides a simple way to control risk through broad diversification, it lacks a precise, quantitative control mechanism. Professional portfolio managers may be hesitant to use stratification as it does not allow them to precisely quantify the risks they are taking. Overall, while stratification can be an effective method for some portfolio managers, it may not be the best solution for all.

# Factor exposure targeting
One method of aligning the portfolio with the benchmark is to target the benchmark's factor exposures as the desired factor exposures for the portfolio. Alternatively, the portfolio's overall beta relative to the benchmark can be set to approximately 1. This ensures that the portfolio closely tracks the benchmark's performance.

The beta of a portfolio relative to its benchmark is calculated as the weighted average of the betas of the individual stocks in the portfolio. Specifically, let β be an $N$-dimensional column vector representing the benchmark beta of each stock, where $β_i$ is the beta of stock $i$ with respect to the benchmark. The portfolio beta is then given by the product of the transpose of the portfolio weight vector, $w^\top$, and $β$. To ensure that the portfolio beta aligns with the benchmark, one approach is to set a constraint on the portfolio beta, such as requiring it to fall within a specified range: $0.9 \le w^\top β\le 1.1$. Alternatively, we could add a constraint to the optimization problem directly: $ w^\top β=1$.

To expand on the concept of targeting a portfolio's benchmark beta, we can also specify a range for each of the portfolio's other factor exposures. This is known as **factor tilting**, where the portfolio is adjusted to increase exposure to certain factors and decrease exposure to others based on market conditions and our view on the factors. For example, if a portfolio manager believes the market will rally, they may wish to have a higher market beta than the benchmark while keeping other factor exposures equal to the benchmark, thus tilting the portfolio towards the market factor.

The factor exposure of a portfolio is determined by the weighted average of the factor exposures of individual stocks. We can represent this with an $N x K$ matrix $B$, where $K$ is the number of relevant factors, and $β_{i,k}$ is the exposure of stock $i$ to factor $k$. The factor exposure of a portfolio with weight $w$ is simply $B^\top w$. Therefore, we can add a general factor exposure constraint to ensure the portfolio is tilted towards certain factors.

By assigning a minimum exposure value (such as 0.9) to a particular factor, the portfolio manager can express their management style and orient the portfolio towards certain types of investments. For example, setting the first element of β to 0.9 for the growth factor would tilt the portfolio towards growth investments.

# Tracking-error minimization
Portfolio managers who use benchmarks often use the minimization of tracking error (TE) approach to construct their portfolios. There are two methods to formulate this optimization problem: one approach minimizes the TE given an expected excess return over the benchmark, while the other maximizes the expected excess return over the benchmark subject to a maximum TE constraint. 

To minimize TE, portfolio managers use the standard deviation of portfolio returns minus benchmark returns:

$$
\text{TE}=s(r_P-r_B)=\sqrt{V(r_P-r_B)}.
$$

They typically use all TE constraints available to them as long as they enhance the expected excess return over the benchmark. These constraints vary from portfolio to portfolio and range from 0.5% to 10% per annum.


The quadratic optimization framework discussed earlier applies to tracking-error minimization, and only minor adjustments are necessary for the optimization problem. To find a portfolio that minimizes the tracking error 

$$
V(r_P-r_B)=V(r_P)-2C(r_P,r_B)+V(r_B),
$$

we minimize the variance of portfolio returns minus twice the covariance between portfolio returns and benchmark returns (e.g., $V(r_P)-2C(r_P,r_B)$) because we cannot control the variance of the benchmark.

To find the portfolio that minimizes tracking error, we need to solve the quadratic minimization problem. The same quadratic programming routine used in the preceding section can solve this problem as well. Typically, the chosen portfolio mean $μ_P$ will be some excess return over the benchmark. Practically, we should think of $μ_P$ as the expected return of the benchmark plus a small amount ($μ_P=$μ_B+\delta$) that we add according to our desire, and then run the optimization to find the portfolio weights.
Hence,

$$
\min\limits_w w^\top\Sigma w-2w^\top\gamma, \text{ s.t. } w^\top\mu=\mu_P,
$$

with $\gamma^\top = (C(r_1,r_B),\cdots, C(r_N,r_B))$.
Finally, we can add various additional constraints, such as the short-sale, diversification, and style constraints, as in the case of a portfolio with no benchmark.

# Tracking by factor exposure
There exists an alternative, yet equivalent method to represent the tracking-error minimization issue. Recall that an individual stock $i$'s variance can be estimated as follows:

$$
V(r_i)=\beta_i^\top V(f)\beta_i+V(\epsilon_i).
$$

If we assume that the covariance between the residuals of the stocks is 0, then we can express the variance-covariance matrix of all stock returns as:

$$
\begin{align}
\Sigma &= 
\begin{bmatrix}
\beta_{1,1} & \cdots & \beta_{1,K} \\
\vdots     & \vdots & \vdots     \\
\beta_{N,1} & \cdots & \beta_{N,K} \\
\end{bmatrix}
\begin{bmatrix}
V(f_1)     & \cdots & C(f_1,f_K) \\
\vdots     & \vdots & \vdots     \\
C(f_K,f_1) & \cdots & V(f_K)     \\
\end{bmatrix}
\begin{bmatrix}
\beta_{1,1} & \cdots & \beta_{1,K} \\
\vdots     & \vdots & \vdots     \\
\beta_{N,1} & \cdots & \beta_{N,K} \\
\end{bmatrix}
+
\begin{bmatrix}
V(\epsilon_1)     & \cdots & 0 \\
\vdots     & \vdots & \vdots     \\
0 & \cdots & V(\epsilon_N)     \\
\end{bmatrix}\\
&=B V(f) B^\top +V(\epsilon)
\end{align}
$$

where $B$ is an $N\times K$ matrix of factor exposures, $V(f)$ is a $K\times K$ matrix of factor premium variances and covariances, and $V(ε)$ is an $N\times N$ diagonal matrix of error variances.

With this, we can define the squared tracking error as:

$$
TE^2 = (w^P-w^B)^\top B V(f) B^\top (w^P-w^B)+(w^P-w^B)^\top V(\epsilon)^\top (w^P-w^B)
$$

where $w_P$ and $w_B$ are the weight of the portfolio and benchmark, respectively. By adding relevant constraints, this tracking-error minimization problem can be solved using a quadratic optimizer.

When minimizing tracking error, the portfolio's factor exposures will be very similar to those of the benchmark. Consequently, the first term on the right-hand-side of the above equation becomes less important than the second term. If the portfolio manager has predetermined values for the portfolio factor exposures, they may disregard the first term entirely. This results in a simpler optimization problem where the portfolio's error term variance is minimized, subject to additional constraints on portfolio factor exposure. This is known as factor tilting.

Suppose the portfolio manager desires to shift the portfolio towards small growth stocks while maintaining all other factor exposures identical to those of the benchmark. They may achieve this by setting the portfolio's exposures to the size and growth factors higher than those of the benchmark while keeping the other factor exposures equal to the benchmark's. 

# Ghost benchmark tracking
Ghost benchmark tracking refers to a scenario where the portfolio manager lacks knowledge of the weights of the benchmark's underlying securities or cannot estimate all the benchmark's factor exposures. In such cases, the objective of minimizing tracking error involves minimizing the deviation of the portfolio's historical returns from that of the benchmark. 

# Risk-adjusted tracking error
Risk-adjusted tracking error is a common constraint that portfolio managers use to limit tracking error within a certain percentage, such as 3% per annum. To achieve this constraint, the portfolio manager can increase the expected excess return until the desired tracking error level is reached. This process is similar to what we discussed earlier, with the objective function being the expected return of the portfolio and the constraint being the tracking error. In example,

$$
\max\limits_w w^\top\mu \text{ s.t. } V(r_P-r_B)=\sigma_x^2
$$

given the target tracking error of $\sigma_x$.
If there is no specific target tracking error or expected return, the problem can be expressed in terms of the tracking-error-adjusted expected return. The expected return can be adjusted for tracking risk by subtracting a multiple of the squared tracking error, where the multiplier A is known as the tracking-error aversion parameter. This parameter indicates the level of cost the portfolio manager considers acceptable for tracking error. In example,

$$
\max\limits_w w^\top\mu -AV(r_P-r_B)
$$

subject to other additional constraints. It is important to note that the two formulations are related, and the maximum-return portfolios obtained from varying the target tracking error $σ_x$ are identical to the optimal portfolios obtained by varying the tracking-error aversion parameter $A$. Therefore, if a commercial software package does not support maximizing the expected return subject to a quadratic constraint, the tracking-error-adjusted expected return can be maximized for a specific value of $A$, and the value of $A$ can be changed iteratively until the tracking-error constraint is met. 

# Quadratic programming

The general quadratic programming problem can be expressed as minimizing the function 

$$
\min\limits_w 0.5 w^\top \Sigma w + w^\top c \quad\text{s.t.}\quad Aw\le b
$$ 

where $w$ is the vector of unknowns, $\Sigma$ is a symmetric positive semidefinite matrix supplying coefficients on the quadratic terms, $c$ is a vector of coefficients related to the linear objective function, $A$ is a matrix of coefficients for the constraints, and $b$ is a vector of constraint values.

This general quadratic optimization problem works for both quadratic and linear optimization problems. For linear optimization problems, $\Sigma$ can be set to 0, and the problem becomes a linear programming problem. In contrast, for quadratic optimizations, the appropriate $\Sigma$ is used.

Let's examine two special cases of the general quadratic optimization program. One case only involves equality constraints, while the other case includes both inequality and equality constraints. We separate these into two categories because with equality constraints, we can solve for the optimal weights using a closed-form solution. Although the objective function and constraints are abstract mathematical concepts in the general optimization problem, they become more meaningful when applied to real-world problems. In the next section of this appendix, we will demonstrate this.

## Quadraric programming with equality constraints
In the case of quadratic optimization problems with only equality constraints, a closed-form solution can be obtained. Specifically, the problem can be formulated as follows:

$$
\min\limits_x 0.5 w^\top \Sigma w + w^\top c \quad\text{s.t.}\quad Aw= b
$$ 

Given that matrix $A$ is of full rank and matrix $\Sigma$ is positive definite, a unique solution for $w$ exists. By unique solution, we refer to a set of values for $w$ that yields the minimum value of our objective function. 

:::{note}
A matrix $A$ is said to be of full rank if its rows or columns are linearly independent. In other words, there are no redundant rows or columns that can be expressed as linear combinations of other rows or columns. This implies that the matrix has the maximum possible number of linearly independent rows or columns, which is equal to the minimum of the number of rows or columns of the matrix.
A matrix of full rank has an inverse, and it is invertible. Additionally, the determinant of a matrix of full rank is non-zero.

A matrix $\Sigma$ is positive definite if it satisfies the following two conditions:
* The matrix $\Sigma$ is symmetric, meaning that $\Sigma$ is equal to its transpose: $\Sigma = \Sigma^\top$.
* For any non-zero vector $w$, the scalar value $x^\top \Sigma w$ is positive. This means that $w^\top \Sigma w > 0$ for any non-zero vector $w$.
Geometrically, this means that the quadratic form defined by the matrix $\Sigma$ is always positive, and thus the matrix $\Sigma$ defines a "bowl-shaped" surface.
The concept of positive definiteness is important in many areas of mathematics, particularly in linear algebra and optimization. For example, if the objective function of a quadratic optimization problem involves a positive definite matrix $\Sigma$, then the optimization problem has a unique global minimum, and this minimum can be found by solving a system of linear equations.
:::

To solve this minimization problem, we can apply the Lagrange method and derive the first-order optimality conditions.
The Lagrangian for this problem is given by:

$$
\mathcal{L} = 0.5 w^\top \Sigma w + w^\top c-\lambda^\top(b-Aw)
$$

Taking partial derivatives with respect to $w$ and λ, we can derive the Lagrange necessary (or first-order) conditions for a solution:

$$
\Sigma w + A^\top \lambda + c = 0, \text{  and } Aw-b = 0. 
$$

:::{note}
The Lagrange method is a powerful tool for solving constrained optimization problems. It involves introducing Lagrange multipliers to convert a constrained optimization problem into an unconstrained optimization problem. The method is named after Joseph Louis Lagrange, a celebrated mathematician and physicist who was a professor at the University of Turin in 1755 and later served as director of mathematics at the Berlin Academy of Science, succeeding Euler in this position.
:::

We can obtain the optimal value of $w$ by solving these equations algebraically. Specifically, we can start by solving the first equation for $w$, which gives:

$$
\begin{align*}
\Sigma w &= -A^\top \lambda - c\\
w &= -\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c
\end{align*}
$$

Substituting this expression for $w$ into the second equation yields:

$$
\begin{align*}
&Aw-b = 0 \\
&A(-\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c)-b= 0 \\
&\lambda = -(A\Sigma^{-1}A^\top)^{-1}(A\Sigma^{-1}c+b)
\end{align*}
$$

Finally, we can substitute the value of λ into the expression for $w$ to obtain a closed-form solution for $w$:

$$
\begin{align*}
w &= -\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c \\
  &= -\Sigma^{-1}A^\top [-(A\Sigma^{-1}A^\top)^{-1}(A\Sigma^{-1}c+b)] - \Sigma^{-1}c \\
  &= -\Sigma^{-1}[ -A^\top(A\Sigma^{-1}A^\top)^{-1}A\Sigma^{-1} +I]c 
  +\Sigma^{-1}A^\top(A\Sigma^{-1}A^\top)^{-1}b\\
\end{align*}
$$

where $I$ is the identity matrix.

:::{note}
The identity matrix is a square matrix with ones on the diagonal and zeros elsewhere. 
:::

### A Numerical Example
In a portfolio risk-minimization problem, the objective is to minimize the variance of the portfolio for a given expected return level, subject to an equality constraint that the weights of the portfolio sum to 1. This can be translated into a quadratic optimization problem, where the risk of a portfolio is given by the variance-covariance matrix of the stock returns and the vector of stock weights. The mean return of the portfolio can be expressed as the dot product of the vector of mean returns and the vector of stock weights.

To illustrate this, let's consider a six-stock portfolio with known annualized mean returns and a variance-covariance matrix. We can construct the matrix A and vector b to reflect the equality constraint of summing to 1 by solve the following quadratic optimization problem:

$$
\begin{align*}
A&=
\begin{bmatrix}
1 & \cdots & 1 \\
\mu_1 & \cdots & \mu_N \\
\end{bmatrix}\\
b &=
\begin{bmatrix}
1 \\
\mu_P \\
\end{bmatrix}\\
c &= 0
\end{align*}
$$

It follows that

$$
\begin{align*}
w &= \Sigma^{-1}A^\top(A\Sigma^{-1}A^\top)^{-1}b\\
\end{align*}
$$

To provide a detailed illustration of the application, let's consider a simple portfolio consisting of six stocks. The annualized mean returns for these stocks are as follows: $μ_1$ = 14.4, $μ_2$ = 10.19, $μ_3$ = 9.87, $μ_4$ = 7.52, $μ_5$ = 20.05, and $μ_6$ = 2.66. The variances and covariances are expressed in percentage terms. For instance, the annualized variance for stock 1 is 452.33, which is equivalent to a variance of 452% per year (or a standard deviation of 21.26% per year). Finally, we select the value of $μ_P$ to reflect an annualized return of 8%.

Now, we can determine the optimal weights for the six stocks that will minimize the risk while achieving an expected mean return of 8% per year.

```{code-cell}
---
mystnb:
  figure:
    align: center
    caption_before: true
    caption: This is my table caption, above the table
---
import numpy as np
from numpy.linalg import inv

Sigma = np.array([[452.33, 249.33 , 189.23, 70.75,  481.14 , 106.5],
                  [249.33, 1094.09, 356.85, 93.51 , 1216.91, 135.05],
                  [189.23, 356.85 , 617.57, 161.82, 1304.29, 110.74],
                  [70.75 , 93.51  , 161.82, 372.35, 462.57 , 107.52],
                  [481.14, 1216.91, 1304.29, 462.57, 5658.42, 425.35],
                  [106.5 , 135.05,  110.74, 107.52, 425.35 , 244.31]])
print(Sigma)
```

```{code-cell}
Sigma.T==Sigma
```

```{code-cell}
A = np.array([[1,1,1,1,1,1],[14.4,10.19,9.87,7.52,20.05,2.66]])
print(A)
```

```{code-cell}
b = np.array([1, 8])
print(b)
```

```{code-cell}
w = inv(Sigma) @ A.T @ inv( A @ inv(Sigma) @ A.T) @ b
print(w)
```

```{code-cell}
import cvxpy as cp

N = 6
w = cp.Variable(N)
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Minimize(risk), [A@w == b])
prob.solve(solver=cp.SCS)   

print( w.value, prob.value)
```

The optimal solution for a portfolio with a capital of \$1 is to allocate \$0.305 to stock 1, \$0.057 to stock 2, \$0.204 to stock 3, \$0.274 to stock 4, short sell -\$0.085 of stock 5, and allocate \$0.245 to stock 6. However, the short position in stock 5 may not be feasible for many portfolio managers due to various reasons. Therefore, the portfolio manager may want to impose inequality constraints, such as requiring the weight of security 2 to be greater than 10%. Additionally, the portfolio manager may want to ensure that the weights of all securities are greater than zero. These restrictions were not applied in the preceding optimization, but we will introduce them in the next application of our example.


## Quadraric programming with inequality constraints
The quadratic optimization problem with inequality constraints is generally more complex than the case of only equality constraints, and a closed-form solution may not be available. Therefore, numerical solution methods are often used to solve this type of problem. With the advances in computing power and optimization algorithms, numerical methods have become more reliable and efficient for solving quadratic programming problems with inequality constraints.

One commonly used approach is the active-set method or projection method, which involves iteratively updating a set of active constraints and solving a linear system of equations to find a new candidate solution. Another popular method is the interior-point method, which involves transforming the original problem into a sequence of barrier problems and solving a sequence of smaller optimization problems to approximate the solution to the original problem.

While these numerical methods can be quite effective, they do require a good understanding of the underlying mathematics and may be computationally intensive for large-scale problems. Fortunately, many software packages and optimization libraries are available that implement these methods and make it easier for portfolio managers and researchers to solve quadratic programming problems with inequality constraints. Therefore, it is not necessary to delve into the technical details of each method, but it is important to understand their underlying principles and limitations in order to use them effectively in practice.

### A Numerical Example
To further illustrate the application, we will continue with the previous numerical example and introduce some inequality constraints. We will use the active-set method to solve the problem. Specifically, we will add three inequality constraints that specify that the weights of each individual stock cannot be less than zero, except for stock 2, which cannot have a weight less than 0.10. Therefore, we have $w ≥ 0$ and $w_2 ≥ 0.10$. These inequality constraints can be easily incorporated into the matrix $A$. 
The resulting optimization problem has the first two rows of $A$ representing equality constraints and the last seven rows representing inequality constraints. The formulation of the problem is as follows:

```{code-cell}
A = np.array([[1,1,1,1,1,1],
              [14.4,10.19,9.87,7.52,20.05,2.66],
              [-1,0,0,0,0,0],
              [0,-1,0,0,0,0],
              [0,0,-1,0,0,0],
              [0,0,0,-1,0,0],
              [0,0,0,0,-1,0],
              [0,0,0,0,0,-1],
              [1,0,1,1,1,1]])
print(A)
```


```{code-cell}
b = np.array([1, 8,0,0,0,0,0,0,0.9])
print(b)
```

```{code-cell}
import cvxpy as cp

N = 6
w = cp.Variable(N)
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Minimize(risk), [A[:2,:]@w == b[:2], A[2:,:]@w <= b[2:]])
prob.solve(solver=cp.SCS)   

print( np.round(w.value,3), np.round(prob.value,3))
```

It's worth noting that we expressed the constraint $w_2 ≥ 0.10$ as $w_1+w_3+w_4+w_5+w_6 ≤ 0.90$. This is because in certain cases, such as when using certain programming tools, the most apparent constraints may require some tweaking or reengineering to fit into the optimization problem.

# Advanced Techniques for Quadratic Optimization
While the basic techniques covered in this chapter address most portfolio optimization problems, there are scenarios where the optimization setup needs to be expanded. For instance, a portfolio manager may need to factor in transaction costs or create a market-neutral portfolio with leverage constraints. Other situations may involve restrictions on the number of stocks in the portfolio, where the number falls between a minimum and maximum or where the weights of any security are either zero or within a minimum and maximum weight. These and other preferences in the optimization require an expanded optimization framework. Additionally, some portfolio optimization problems may involve quadratic constraints, which are not part of the typical optimization framework. In this section, we will discuss the fundamental building blocks for expanding the optimization framework to address these advanced optimization scenarios.

### Phantom weights
In standard portfolio optimization problems, we typically only have $N$ unknowns, which are the portfolio weights. However, in certain nonstandard portfolio problems, it can be useful to introduce what we call "phantom weights." The idea of phantom weights is to create additional weights, in addition to the actual weights of the portfolio, that the optimizer will also find optimal values for. These additional weights can be used for various purposes, such as creating a set of buy and sell weights. For example, if the optimization problem has $N$ stocks, we can create an additional $2N$ weights, denoted as $b_1$ to $b_N$ and $s_1$ to $s_N$. With these additional weights, the new optimization problem becomes more complex, as we now have $3N$ weights to choose from. However, phantom weights offer many benefits in portfolio optimization. Often, the phantom weights have a specific relationship to the underlying weights, such as $b + s = 1$, where $b$ and $s$ are the buy and sell weights, respectively.

### Binary weights
In portfolio optimization, it may be beneficial to use binary variables as optimization weights in addition to phantom weights. Binary variables are weights that are constrained to have a value of either 0 or 1. One practical application of binary variables is to ensure that phantom weights are orthogonal. This is important because having both a long position and a short position on the same stock (i.e., $b>0$ and $s>0$) is a wasteful solution. By creating binary variables and for each of the $N$ stocks, we can add a constraint to force the phantom weights to be orthogonal. The constraint can be formulated as follows:

To incorporate binary variables as optimization weights, one can create $v_i^+$ and $v_i^-$ binary variables for each of the $N$ stocks. By adding the constraint

$$
\begin{align*}
& v_i^+\kappa_l \le b_i \le v_i^+\kappa_h \\
& v_i^-\gamma_l \le s_i \le v_i^-\gamma_h \\
\end{align*}
$$

and setting $\kappa_l = \gamma_l = 0$ and $\kappa_h = \gamma_h = 1$, the weights can fluctuate between 0 and 1, and the constraint $v_i^++v_i^-\le 1$ ensures that the phantom weights are orthogonal. If $b_i>0$, then $s_i=0$ and vice versa for every stock $i$. However, the addition of binary and phantom weights and their associated constraints makes the optimization problem more complex and challenging to solve.

### Market neutrality with leverage constraints

Adding the following constraints to the optimization problem will create a market-neutral portfolio that is dollar neutral and has limited leverage:

$$
\begin{align*}
& w_i = w_i^{+} - w_i^{-} \\
& \sum\limits_{i=1}^N w_i^+ = \sum\limits_{i=1}^N w_i^-\\
& w_i^+ \ge 0\\
& w_i^- \ge 0\\
& \sum\limits_{i=1}^N w_i^+ + \sum\limits_{i=1}^N w_i^- \le 2\\
\end{align*}
$$

where $w_i^{+}=b_i$ and $w_i^{-}=s_i$.
These constraints ensure that the sum of the weights of the long stocks equals the sum of the weights of the shorted stocks, creating a dollar-neutral portfolio. The leverage of the portfolio is limited to 2, meaning that the portfolio is 100% long and 100% short of the assets under management.

If the market-neutral manager wanted to increase the leverage, they could adjust the constraints on the sum of the phantom long and short weights. For example, to create a 130-30 long-short portfolio, one could set $L_l = 1.3$ and $L_s = 0.3$ in the following constraints:

$$
\begin{align*}
& \sum\limits_{i=1}^N w_i^+=L_l\\
& \sum\limits_{i=1}^N w_i^-=L_s
\end{align*}
$$

This would result in a portfolio with long exposure of 130% and short exposure of 30%.


## Transactions costs
When we want to rebalance a portfolio while considering transaction costs (or market impact), we can use phantom weights and binary variables to find an exact solution to the portfolio optimization problem. To do this, we need to add constraints to the optimization problem that consider the current weights of the portfolio represented by $w_b$ and the target weights after rebalancing represented by $w_a$:

$$
w_i^a = w_i^b+w_i^+-w_i^-
$$

The relationship between the binary variables and the phantom weights is set such that $\kappa_l = \gamma_l = 0$ and $\kappa_h = \gamma_h = 1$, which allows the weights to fluctuate between 0 and 1. We also add the constraint that $v_i^++v_i^-\le 1$ to ensure the phantom weights are orthogonal. Stocks that have reduced weight from the prior portfolio will have negative net weights but positive phantom weights, denoted by $w_i^-$. We can multiply the transactions cost vector by their value. Conversely, stocks that have increased weight will have positive phantom weights, denoted by $w_i^+$, and can also be multiplied by the transactions cost vector. The final optimized weights of the portfolio will be $w_i$. In the case of transaction costs, the phantom weights serve as a mechanism to denote the change to the current weights, storing the positive changes in the positive phantom weights and the negative changes in the negative phantom weights. Both positive and negative phantom weights are positive, so the transaction cost vector remains positive, and the transaction cost rebalance problem is resolved.


## Elimination of small-weight stocks
Portfolio managers may want to reduce the number of securities in their portfolio, which can be achieved by constructing an optimized portfolio that forces individual stock weights to be above a minimum or below a maximum weight. However, the traditional method of adding inequality constraints to optimize weights may not always result in a solution, as it forces all stocks to be within a given range, which may not be optimal. The use of binary variables can create an optimization that limits the optimizer to find weights between the minimum and maximum or forces the weight of a particular stock to zero. This results in more successful optimizations and aligns better with the portfolio manager's thought process.

To illustrate, we will focus on the situation where all stock weights should be between a lower bound ($\kappa_l$) and an upper bound ($\kappa_h$) for the long portion of the portfolio. Using the inequality relationship of the binary variables and phantom weights, we can set $v_i^+\kappa_l \le b_i \le v_i^+\kappa_h$ and $v_i^-\gamma_l \le s_i \le v_i^-\gamma_h$. Once we specify the values for $\kappa_l$, $\gamma_l$, $\kappa_h$, and $\gamma_h$, we can effectively achieve our goal. If the portfolio is only a long portfolio, phantom weights are not needed, and we should construct one set of binary variables with respect to the actual weights, $w_i$. The binary variables can be either 0 or 1, and the weights of the portfolio will be selected to be within the minimum and maximum weights or set to zero.


## A numerical example
Continuing with the prebious  numerical example we  seek a portfolio with an average annualized return of 8%, with no short sales allowed, and the weights of the portfolio must sum to 1. We now add the constraint that a stock can only have a weight greater than 0.03 (i.e., 3%) or less than 0.30 (i.e., 30%) or else it must have a value of 0.

The first two rows of this A matrix are the equality constraints that the sum of weights equals 1 and that the target mean is 8%. For the binary weights (the six additional elements in the vector $x$), a 0 is placed in the matrix since binary weights are not relevant for these constraints. The rest of the rows represent inequality constraints to
restrict the weights of every stock between 0.03 and 0.30, or a weight of 0. That is, we chose the values of $\kappa_l$ and $\kappa_h$ such that $0.03v_i^+ \le w_i \le 0.3v_i^+$. Since $v_i^+$  is a binary variable, if this
variable equals 1, then the weight of stock $i$ will be forced to lie in the range of 0.03 and 0.30; however, if it’s more optimal to make its weight 0, then $v_i^+= 0$ and $w_i$ will also be equal to 0.



```{code-cell}
!pip install gurobipy

import numpy as np
import gurobipy as gp

# Define the matrix A and vector b
A = np.array([[1,1,1,1,1,1,0,0,0,0,0,0],
              [14.4,10.19,9.87,7.52,20.05,2.66,0,0,0,0,0,0],
              [1,0,0,0,0,0,-0.3,0,0,0,0,0],
              [0,1,0,0,0,0,0,-0.3,0,0,0,0],
              [0,0,1,0,0,0,0,0,-0.3,0,0,0],
              [0,0,0,1,0,0,0,0,0,-0.3,0,0],
              [0,0,0,0,1,0,0,0,0,0,-0.3,0],
              [0,0,0,0,0,1,0,0,0,0,0,-0.3],
              [-1,0,0,0,0,0,0.03,0,0,0,0,0],
              [0,-1,0,0,0,0,0,0.03,0,0,0,0],
              [0,0,-1,0,0,0,0,0,0.03,0,0,0],
              [0,0,0,-1,0,0,0,0,0,0.03,0,0],
              [0,0,0,0,-1,0,0,0,0,0,0.03,0],
              [0,0,0,0,0,-1,0,0,0,0,0,0.03]])

print(A)

b = np.array([[1,8,0,0,0,0,0,0,0,0,0,0,0,0]])
print(v)

Sigma = np.array([[452.33, 249.33 , 189.23, 70.75,  481.14 , 106.5],
                  [249.33, 1094.09, 356.85, 93.51 , 1216.91, 135.05],
                  [189.23, 356.85 , 617.57, 161.82, 1304.29, 110.74],
                  [70.75 , 93.51  , 161.82, 372.35, 462.57 , 107.52],
                  [481.14, 1216.91, 1304.29, 462.57, 5658.42, 425.35],
                  [106.5 , 135.05,  110.74, 107.52, 425.35 , 244.31]])
print(Sigma)

# Create a GurobiPy model
model = gp.Model()

# Create the decision variables
w = model.addVars(12, vtype=[gp.GRB.CONTINUOUS]*6 + [gp.GRB.BINARY]*6)

# Add the constraints Aw = b for the first two rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) == b[0,j] for j in range(2))

# Add the constraints Aw <= b for the rest of the rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) <= b[0,j] for j in range(2,14))

risk = 0.5 * gp.quicksum(Sigma[i,j]*w[i]*w[j] for i in range(6) for j in range(6))
model.setObjective(risk, gp.GRB.MINIMIZE)

# Set the objective function to zero (since this is a feasibility problem)
model.setObjective(risk, sense=gp.GRB.MINIMIZE)

# Solve the model
model.optimize()

# Print the solution
if model.status == gp.GRB.OPTIMAL:
    print("Solution found!")
    for i in range(12):
        print(f"w[{i}] = {w[i].x}")
else:
    print("No solution found.")
```

