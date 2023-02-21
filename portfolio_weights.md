
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
.\\
E(r_N)
\end{bmatrix}
$$

and 

$$
\Sigma = 
\begin{bmatrix}
1 & 2 & 3\\
a & b & c
\end{bmatrix}
$$

A valid portfolio is specified by an N-dimensional column vector of stock weights, w, where the weight of each stock is represented by wi. The sum of all elements in w must equal 1.

The expected return of the portfolio is given by w′μ, while the risk of the portfolio is represented by w′Σw, where w′ represents the transpose of the weight vector. The portfolio with the minimum risk and expected return of μP is obtained by minimizing the objective function w′Σw while satisfying the constraint w′μ = μP. This is a quadratic optimization problem, and mathematicians have developed quadratic programming to solve it.

The quadratic minimization problem with equality constraints can be rewritten as a set of linear constraints, which have a closed-form solution. Appendix 9A provides further details on this solution. A visual example of the results from a mean-variance optimization can be seen in Figure 9.1, which displays the efficient frontier for the consumer staples sector based on data from January 2016 to December 2020.

To create a minimal-risk portfolio for a given level of expected return, we begin the optimization procedure using the expected return of the lowest expected return stock. We increment the mean return and repeat the optimization until we reach the expected return of the security with the highest mean return. We plot all the points in the diagram and connect them to produce the efficient frontier. The expected-return–expected-risk profile we desire can then be selected from the efficient frontier, and we can pick the weights of the corresponding stocks.
