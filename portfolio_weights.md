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



