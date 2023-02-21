
In previous chapter we discussed ideas for stock selection, which serve as crucial tools for identifying good and bad stocks. However, constructing a portfolio requires more than just identifying individual stocks. A skilled manager needs to assign relative weights to the stocks to create a cohesive portfolio.

There are several ways to generate stock weights, ranging from simple methods like equal weighting or market capitalization weighting to more complex techniques based on modern portfolio theory. For portfolio managers who manage against a benchmark, there are additional weighting possibilities, such as ensuring the weighted-average factor exposures of the portfolio match those of the benchmark or maximizing excess expected return while limiting tracking error.

To minimize tracking error or risk when weighting stocks, the manager needs to know each stock's expected return, risk or variance, and covariances among stocks. Additionally, the manager may want to impose constraints on the portfolio creation process, such as prohibiting short sales or upholding diversification rules. The manager can then use a quadratic optimizer to determine the optimal weights for the portfolio.

We begin by discussing two methods for creating a portfolio that is not managed against a benchmark: ad hoc methods that use rules of thumb to weight stocks and the mean-variance optimization method, which minimizes the portfolio's total risk given its expected return. We then explore the four potential approaches to creating a portfolio that is managed against a specific benchmark, including ad hoc weighting methods, stratification, factor exposure targeting, and tracking-error minimization. Of these techniques, only those that minimize risk have theoretical rigor but also require a larger skill set, more time, and more effort than the less quantitatively precise methods.

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

# Short-Sale and Diversification Constraints

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

# Trading-Volume Constraint
One common constraint added to optimization by portfolio managers is the trading-volume constraint, which is particularly relevant when managing large portfolios that could have a significant price impact on the market. To avoid negative price impact, portfolio managers may restrict the holdings of each stock to a certain threshold amount, often a fraction of the average trading volume of each stock.

For example, if a portfolio is valued at $500 million and the manager wishes to keep the holding of one stock below 10% of its average daily trading volume (ADV), the constraint can be expressed as 

$$
500w_i \le 0.1x_i
$$

where $w_i$ is the portfolio weight of stock $i$ and $x_i$ is the average trading volume of stock $i$ measured in millions of dollars.

More generally, the trading volume constraint can be expressed as a linear inequality constraint, where x is a vector of average daily trading volume in dollar terms, and c is a constant indicating the threshold:

∑i wi xi ≤ c, where i represents each stock in the portfolio.

where $w_j$ denotes the weight of sector $j$ in the portfolio.



