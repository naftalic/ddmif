#!/usr/bin/env python
# coding: utf-8

# # 9) Rebalancing and Transaction Costs
# In April 2020, Invesco made a costly rebalancing error with its Equally-Weighted S&P 500 Fund, which resulted in a loss of $105 million over five days. Invesco misinterpreted the altered schedule by S&P Dow Jones Indices, which had delayed and separated the quarterly rebalancing dates for its indexes due to market volatility. Invesco failed to rebalance the funds on April 24, the scheduled date for S&P Dow Jones Indices to rebalance the index.
# 
# On April 29, Invesco discovered the omission and rebalanced the funds, injecting approximately $105 million into the funds to compensate investors for the performance difference between April 24 and April 29. Although Invesco does not expect this matter to have a material impact on its financial condition, the rebalancing error illustrates the importance of rebalancing decisions and the need to consider transaction costs when making portfolio adjustments.
# 
# Rebalancing decisions can be triggered by various factors, such as changes in market conditions, asset prices, or investor preferences. When the decision to rebalance is made, transaction costs become a significant consideration in determining the optimal portfolio composition. However, transaction costs are often overlooked during the initial creation of the portfolio, as they do not have an immediate impact.
# 
# As a result of this rebalancing error, Invesco had to compensate investors for the performance difference between April 24 and April 29, resulting in a significant financial loss. Understanding and managing transaction costs is crucial for portfolio managers in ensuring investment success and avoiding costly errors.
# 
# # When and how to make the right decisions
# Determining the optimal time and method for rebalancing a portfolio is crucial for investment success. Rebalancing decisions involve two key considerations: when to rebalance and how to do it.
# 
# The optimal rebalancing period can be determined relatively easily from an econometric perspective. The factor model used to select stocks specifies a particular rebalancing frequency. For example, if monthly returns were used to estimate the model, then the optimal portfolio is only valid for one month. If quarterly returns were used, then the portfolio would be optimal for one quarter. The rebalancing period is simply the model's periodicity, which is discussed in the first part of this section.
# 
# The more complex aspect of rebalancing involves deciding how to adjust the model's parameters, such as α, to update the portfolio. This can be a challenging task, as it requires balancing the potential benefits of improving the portfolio's performance against the costs associated with incurring transactions costs. In the second part of this section, we will explore different strategies for adjusting the portfolio's parameters to effectively rebalance the portfolio while minimizing costs.
# 
# Overall, effective rebalancing requires a careful consideration of both the optimal rebalancing period and the appropriate adjustment of the model's parameters. By carefully managing these factors, portfolio managers can maximize returns while minimizing costs, ultimately leading to investment success.
# 
# ## Rebalancing and the importance of model periodicity in financial markets
# 
# The accuracy of models in predicting daily stock returns has long been recognized as limited by financial experts. While models can capture patterns that emerge over time, they often fail to consider specific news and events that heavily influence daily returns. For hourly returns, a model's predictive power is close to zero. While some researchers have found moderate success in applying their models to weekly returns, such returns remain too susceptible to the influence of specific events.
# 
# Most financial research is conducted using monthly returns as a viable middle-of-the-road solution to the tradeoff between predictive power and parameter stability. While longer periods such as annual or quarterly returns offer a larger sample size, the risk of unstable parameters and changing market conditions make monthly returns a more reliable option.
# 
# The decision to rebalance a portfolio depends on several factors, including market stability and external restrictions on the portfolio manager. The general recommendation is to update the estimation of models at least once a month to ensure the most current information is available, and from there, decide whether to rebalance. Model periodicity is crucial to understanding when to rebalance and how to go about it. The timing of rebalancing is relatively straightforward, while the adjustment of parameters to update the portfolio requires careful consideration. In the following section, we will discuss different strategies for adjusting the model's parameters to effectively rebalance the portfolio while minimizing costs.
# 
# ## Adjusting α and other parameters
# Modifying the parameters of a stock-return model may trigger the need to rebalance a portfolio. As previously discussed in the factor model, the stock return can be represented as:
# 
# $$
# r_i = \alpha_i+\beta_{i,1}f_1+\cdots+\beta_{i,K}f_K+\epsilon_i
# $$
# 
# If an economic factor model is used to anticipate stock returns, changes in α and the factor exposures ($\beta_{i,1}, \cdots, \beta_{i,K}$) should be monitored. For a fundamental factor model, α and the factor premiums ($f_1, \cdots, f_K$) should be considered.
# 
# Parameters can shift anytime, and corporate actions and significant changes in the business environment can impact a model's parameters. For instance, if Firm A merges with Firm B, the α and other parameters of Firm A will most likely change. Similarly, if the government imposes a new restriction on the activity of Firm A, its α and other parameters may also change. Even the retirement of a CEO can impact a stock's parameters. Additionally, there are changes that are not publicly disclosed. If the portfolio manager bases α on private information, new private information could affect α.
# 
# Quantitative portfolio managers must always keep the model in mind. If a manager comes across negative news about a stock, they should take the time to consider whether the news lowers the value of α or another parameter.
# 
# When the portfolio manager suspects that a parameter has changed, it is necessary to re-estimate the model. Updating the parameter values updates the expected return and risk of each stock, altering the optimal portfolio. After determining the new optimal portfolio, the manager can decide whether to rebalance the portfolio by weighing the benefits of rebalancing against the transaction costs. In the following section, we will discuss various strategies for adjusting the model's parameters and rebalancing a portfolio.
# 
# # Understanding transactions costs
# Transaction costs refer to the expenses incurred when buying or selling financial assets. These costs go beyond the commission charged by brokers and include other hidden expenses that investors should be aware of.
# 
# One of these costs is the bid-ask spread, which is the difference between the highest price a buyer is willing to pay (the bid price) and the lowest price a seller is willing to accept (the ask price). The spread varies depending on the asset's liquidity, with less liquid assets having a wider spread. For instance, a small-cap stock with low trading volume may have a wider bid-ask spread than a large-cap stock with high trading volume.
# 
# Another hidden cost is the price impact, which refers to the effect of a large buy or sell order on the asset's market price. When a large order is placed, it can move the market price, causing the investor to pay more when buying or receive less when selling than the price quoted before the trade. The price impact depends on the order's size relative to the asset's market size or daily trading volume.
# 
# Although broker commissions are straightforward, estimating bid-ask spreads and price impacts can be difficult as they depend on various factors and can vary over time. Investors can estimate these costs using historical data and by consulting with their broker or financial advisor.
# 
# For example, suppose an investor wants to buy shares of a newly-listed company with a wide bid-ask spread of 5% and a price impact of 2% due to a large order relative to trading volume. Including the broker's commission, the total transaction cost for this trade would be around 7%. In contrast, buying shares of a well-established company with high trading volume may result in a much lower transaction cost of around 0.5%.
# 
# As another example, let's consider two stocks: Stock A and Stock B. For Stock A, the transaction cost is 1% of the investment amount, and the expected return is 𝜇=12%. For Stock B, the transaction cost is 0.1% of the investment amount, and the expected return is 𝜇=10%. Suppose you want to compare the difference in expected investment value with and without transaction costs for each stock.
# 
# Without transaction costs, if you invest $100 in Stock A, you expect to see an increase in value to $112, while for Stock B, you expect an increase in value to $110. The difference between the two is Δ=(112-110)/110=1.81%.
# 
# However, with transaction costs factored in, the expected investment value changes. For Stock A, you would pay a 1% transaction cost upfront, reducing your initial investment to $99. You would then expect a return of 12%, resulting in a final investment value of $110.88. Similarly, for Stock B, you would pay a 0.1% transaction cost upfront, reducing your initial investment to $99.90. You would then expect a return of 10%, resulting in a final investment value of $109.89.
# 
# After including transaction costs, the difference in expected investment value between Stock A and Stock B is Δ=(110.88-109.89)/109.89=0.9%. This illustrates how transaction costs can significantly impact investment returns and emphasizes the importance of considering them when making investment decisions.
# 
# In summary, understanding transaction costs is an essential aspect of investing, and by estimating and minimizing these costs, investors can increase their chances of achieving their financial goals.
# 
# 
# # Modeling transaction costs
# Modeling transaction costs can be a challenging task because they are complex and unpredictable. Typically, a fixed proportion of the total transaction value is used to approximate transaction costs, represented by a constant denoted as $c$. For instance, if $c$ is set to 5 or 10 basis points, the transaction cost per dollar transaction would be $10 \times c$ for a transaction value of $10.
# 
# To calculate the total transaction value (TV), use the weights of stocks in the current portfolio ($w_1^b,\cdots,w_N^b$) and the weights of stocks in the future portfolio ($w_1^a,\cdots,w_N^a$) to determine the current portfolio's dollar value ($V_t$). The superscripts 'b' and 'a' denote 'before' and 'after', respectively. If $V_tw_i^a$ is greater than $V_tw_i^b$, buying stock $i$ is recommended; otherwise, selling stock $i$ is recommended. The difference between $V_tw_i^a$ and $V_tw_i^b$, represented as $V_tw_i^a-V_tw_i^b$, is the amount to buy or sell in dollar terms. Therefore, the transaction value is the sum of this difference across all stocks, which is given by
# 
# $$
# \text{TV} = \sum\limits_{i=1}^N|V_tw_i^a-V_tw_i^b|
# $$
# 
# The transaction cost (TC) is a constant fraction of the transaction value, represented by $cV_t\sum\limits_{i=1}^N|w_i^a-w_i^b|$. To include the transaction cost formula in an optimization problem, it is helpful to express TC as a linear function, which is given by
# 
# $$
# \text{TC} = V_t\sum\limits_{i=1}^Nc_i(w_i^a-w_i^b)
# $$ 
# 
# The values of $c_i$ depend on the values of $w_a$ and $w_b$. If $w_i^a>w_i^b$, $c_i$ is set to $c$; conversely, if $w_i^a<w_i^b$, $c_i$ is set to $-c$. By defining the vector of current weights as $w_b$, the vector of future weights as $w_a$, and the vector of transaction costs as $c$, the transaction cost can be expressed as a vector product of the weight vector and the transaction cost vector, which is given by
# 
# $$
# \text{TC} = V_t(w^a-w^b)^\top c
# $$
# 
# To account for different stocks having varying transaction costs, modeling transaction costs can be proportional to the liquidity of each stock, considering the bid-ask spread and the price impact. Assume that the trading cost is inversely proportional to the average trading volume of each stock. In this case, elements of $c$ would have different signs and absolute values.
# 
# # Portfolio Construction
# Portfolio construction involves selecting a portfolio with an optimal balance of expected return and risk, irrespective of any limitations or expenses that may arise. When managing against a benchmark, the aim is to achieve the best combination of expected excess return and tracking error. While transaction costs are a new factor to consider when determining the optimal portfolio or tracking portfolio, they do not alter the underlying principle of selection.
# 
# ## The Optimal Portfolio with Transactions Costs
# When optimizing a portfolio that incurs transaction costs, we can approach the problem by minimizing the risk for a given expected return or maximizing the risk-adjusted return, which is the expected return minus the variance. Accounting for transaction costs requires recalculating the expected return of the portfolio, which now includes subtracting the cost from the ending portfolio value and the expected return. The effective expected return has three components: the gross expected return, the transactions cost expressed as a fraction of the portfolio value, and the time value of the transactions cost. However, the time value is often negligible and can be ignored for realistic values of transaction costs and expected return.
# 
# To calculate the risk-adjusted return, we use additional notation, such as the expected return vector ($μ$) and the variance-covariance matrix of stock returns ($Σ$). The risk-aversion parameter ($A$) is denoted as the level of tolerance for an increase in variance if the expected return increases by 2%. For example, a value of 2 means that the portfolio manager would tolerate a 1% increase in variance. The risk-adjusted return is then calculated as the expected return minus $A$ times the variance of the prospective portfolio return.
# 
# When incorporating transaction costs, the effective risk-adjusted return is expressed as the expected return of the prospective portfolio minus the transactions costs, minus $A$ times the variance of the prospective portfolio return.
# 
# $$
# \begin{aligned}:
# \text{effective risk-adjusted return} &= \mu_P-(1+\mu)(w^a-w^b)^Tc-A\sigma^2_P\\
# &\approx \mu_P-(w^a-w^b)^Tc-A\sigma^2_P
# \end{aligned}
# $$
# 
# where the last approximation is made by omitting the negligible time value, which represents the loss in return on the transaction cost.
# 
# To find the optimal portfolio, we must maximize the effective risk-adjusted return subject to relevant constraints. However, the effective risk-adjusted return is highly nonlinear because the transaction cost vector depends on the weight vector. Therefore, conventional quadratic optimization techniques cannot be used to solve this problem.
# 
# # The Tracking Portfolio with Transactions Costs
# To minimize tracking error instead of overall risk, a portfolio manager should aim to maximize the effective tracking-error-adjusted return rather than the effective risk-adjusted return.
# 
# The tracking error (TE) of a portfolio is defined as the standard deviation of the difference between the portfolio return $r_P$ and the benchmark return $r_B$. The TE can be expressed as:
# 
# $$
# \begin{aligned}
# \text{TE}^2 &= V(r_P)-2C(r_P,r_B)+V(r_B)\\
# &= w^T\Sigma w-2w^T\gamma+V(r_B)\\
# \end{aligned}
# $$
# 
# Here, $\gamma=C(r,r_B)$, and the last term is constant and does not depend on the weight vector, so only the first two terms are considered in the optimization problem.
# 
# The tracking-error-aversion parameter $A$ measures the manager's aversion to squared tracking error in the portfolio. The effective tracking-error-adjusted return is given by:
# 
# $$
# \text{effective TE-adjusted return} = (w^a)^T(\mu-c)+(w^b)^Tc-A[(w^a)^T\Sigma w^a-2(w^a)^T\gamma+V(r_B)]
# $$
# 
# To find the optimal tracking-error portfolio, we need to maximize the effective tracking-error-adjusted return with certain constraints. For this optimization problem, we can ignore the terms that do not include $w^a$ or $c$. Thus, we solve:
# 
# $$
# \max\limits_{w^a} (w^a)^T(\mu-c+2A\gamma)+(w^b)^Tc-A(w^a)^T\Sigma w^a
# $$
# 
# subject to the constraint that the sum of weights should be 1 and any other constraints. However, conventional quadratic optimization techniques cannot be used to solve this problem because $c$ is a function of $w$.
# 
# # Dealing with Cash Flow
# This section discusses strategies that portfolio managers can implement to minimize transaction costs when dealing with cash inflows or outflows. One such approach is to invest cash temporarily in index futures or ETFs until a more suitable time arises to return it to the portfolio. This method can help managers avoid making rushed investment decisions in response to cash movements.
# 
# Another strategy is to purchase specific stocks that are more liquid, enabling the manager to achieve target portfolio weights with fewer transactions. This approach can help reduce transaction costs and minimize the impact of cash flows on the portfolio's performance.
# 
# ## Reducing Transaction Costs with Futures and ETFs
# When managing a portfolio with daily cash inflows and outflows, adjusting the portfolio with every cash movement can be impractical. For small daily flows, managers can temporarily invest net inflows in cash or rely on a cash buffer to handle small redemptions without significantly impacting portfolio returns. However, for funds with large daily net flows, a large cash reserve can negatively affect portfolio returns, particularly in a low interest rate environment. In such cases, managers may need to adjust their exposure using either index futures or ETFs that invest in the same sector or a highly correlated sector.
# 
# ETFs that focus on specific sectors are widely available, but futures offer several advantages over ETFs. Futures are more liquid during normal trading hours, can be traded after hours on GLOBEX, and gains are treated as partly long-term and partly short-term for tax purposes. However, managers may face challenges rolling over futures contracts if the horizon for using futures is longer than a few days. Therefore, portfolio managers should carefully consider their options and choose the method that best suits their needs.
# 
# ## Rebalancing toward Optimal Target Weights
# To maintain an optimal mix of stock weights, portfolio managers may need to rebalance the portfolio during periods of cash flows or at regular rebalancing periods. For instance, if a portfolio is rebalanced monthly and experiences cash flows at the end of the month, the manager can adjust the portfolio to maintain the original optimal portfolio weights or update the model to achieve new optimal weights. When faced with end-of-month cash flows, the manager can trade to redirect the portfolio towards the original or new optimal target weights.
# 
# To facilitate optimal trades, we outline the algorithm in the following subsections. While our analysis does not incorporate trading costs, we demonstrate that reducing the amount of trading can help minimize tax and direct trading costs.
# 
# 
# ## Standard Rebalancing
# Standard rebalancing is a crucial process for portfolio managers to maintain the desired asset allocation in their portfolios. This involves adjusting the weights of stocks in the portfolio back to a target set of weights, which are typically the same as those in the benchmark index that the portfolio tracks. The current weight of stock $i$ in the portfolio before rebalancing is denoted by $w^b_i$, and the target weight is denoted by $w^a_i$. The price per share of stock $i$ is denoted by $p_i$, and the number of shares held in stock $i$ before rebalancing is denoted by $s^b_i$. The optimal number of shares to hold in stock $i$ is denoted by $s^a_i$.
# 
# To rebalance the portfolio, the difference between the target weights and the current weights is calculated. This difference is then used to determine the number of shares to buy or sell at time $t+1$. The weights of the target and current portfolios at time $t+1$ are given by:
# 
# $$
# w^b_{i,t} = p_{i,t}s^b_{i,t}/V_{t}
# $$ 
# 
# and 
# 
# $$
# w^a_{i,t+1} = p_{i,t+1}s^a_{i,t+1}/V_{t+1}
# $$
# 
# respectively, where $V_{t}$ and $V_{t+1}$ are the total portfolio values at times $t$ and $t+1$, respectively.
# 
# The number of shares of each stock that must be bought or sold is given by:
# 
# $$
# \begin{aligned}
# x_{i,t+1}=s^a_{i,t+1}-s^b_{i,t+1}=\frac{w^a_{i,t}}{p_{i,t+1}}(V_{t+1}+C_{t+1})-s^b_{i,t+1}
# \end{aligned}
# $$
# 
# Here, $C_{t+1}$ represents any monetary contribution to or withdrawal from the portfolio at time $t+1$. The excess shares $x_{i,t+1}$ are negative if shares need to be sold and positive if shares need to be bought. It's important to note that these formulas do not account for bid-ask spreads or price impact, which can introduce additional costs to the rebalancing process.
# 
# # Using Cash Flows to Rebalance without Selling
# To reduce costs associated with rebalancing a portfolio, portfolio managers can use cash inflows to bring the portfolio closer to its target weights without selling securities. Selling securities to rebalance can result in tax costs and transaction costs, so buying more shares of securities whose weights have fallen below target can be a more cost-effective approach.
# 
# One simple method is to invest cash inflows proportionally to the target weights of all the securities in the portfolio. A more sophisticated algorithm can be used to invest the cash inflows in a way that brings the portfolio closer to its optimal weights more quickly. If the portfolio receives a cash inflow of $C_{t+1}$ at time $t+1$, the manager can buy $x_{i,t+1}$ shares of each security, where:
# 
# $$
# x_{i,t+1}=C_{t+1}w^a_{i,t+1}/p_{i,t+1}
# $$
# 
# Here, $w^a_{i,t+1}$ is the target weight for security $i$ at time $t+1$, and $p_{i,t+1}$ is the price per share of security $i$ at time $t+1$. The resulting weights of the portfolio will fall between the original weights and the optimal target weights, and the proximity to the target weights will depend on the ratio of $C_{t+1}$ to $V_{t+1}$, where $V_{t+1}$ is the total value of the portfolio at time $t+1$.
# 
# # Rebalancing by Purchasing Only Deficient Stocks
# A way to quickly align a portfolio with its benchmark weights is by investing new cash only in stocks that are below their target weights. The portfolio is divided into two groups: those that exceed their target weights and those that fall short. To determine these weights, the symbol $\tilde w^b$ is used to represent the portfolio's weights considering the current value of the portfolio and the cash inflow. The weight of each stock with the cash inflow is calculated using the formula:
# 
# $$\tilde w^b_{i,t+1}=\frac{s^b_{i,t+1}p_{i,t+1}}{V_{t+1}+C_{t+1}}$$
# 
# These portfolio weights are then compared to their corresponding target weights $w^a_{i,t+1}$. To allocate cash to stocks that are below their target weight, the cash allocated to stock $i$ is determined using the formula:
# 
# $$c_{i,t+1}=w^a_{i,t+1}(V_{t+1}+C_{t+1}-s^b_{i,t+1}p_{i,t+1})$$
# 
# The sum of all cash allocated to these stocks is then calculated and subtracted from $C_{t+1}$ to determine the amount of slack funds. If there are not enough funds to restore deficient stocks to their required weights, the cash distributed to each stock is scaled down proportionally. The number of shares that need to be purchased for each stock is calculated using the formula:
# 
# $$w_{i,t+1}=\frac{c_{i,t+1}}{p_{i,t+1}}\frac{C_{t+1}}{\sum\limits_{j=1}^{n_u}c_{j,t+1}}$$
# 
# This "buy" system for rebalancing helps the portfolio converge toward the optimal target weights at a faster rate than if new cash were invested in stocks in proportion to their target weights. To calculate the minimum amount of cash inflow required to perfectly rebalance the portfolio without selling, the ratio of the weight of each stock before rebalancing and before new money has been added to the target weight minus one is calculated for each stock. The maximum of these values is then multiplied by the total value of the portfolio $V_{t+1}$ at time $t+1$.
# 
# # Approximate Solution to the Optimal Portfolio Problem
# 
# The optimal portfolio problem to maximize the effective risk-adjusted return or effective tracking-error-adjusted return is not quadratic in $w^a$, which makes it difficult to solve with conventional quadratic optimizers. To address this issue, we present an approximate solution that works well for most situations.
# 
# Nonlinearity arises because we do not know beforehand which stock to sell and which stock to buy. To avoid nonlinearity, we need to determine which stocks to buy and sell before solving the optimization problem. Here's how it works:
# 
# First, we solve the problem ignoring transaction costs, i.e., we maximize $w^a\mu - A(w^a)^T\Sigma w^a$ subject to $(w^a)^TI = 1$ and any other relevant constraints. Let the solution to this problem be denoted as $w^*=(w^*_1,\cdots, w^*_N)$.
# 
# Next, we determine which stocks to buy and sell based on the optimization without considering transaction costs. To do this, we define the transaction cost vector $c = (c_1,\cdots, c_N)$ using the weights $w^*$ as follows:
# 
# $$
# \begin{aligned}
# c_i=
# \begin{cases}
# c  \quad &\text{if}\quad w^*_i>w^b_i\\
# -c \quad &\text{if}\quad w^*_i<w^b_i
# \end{cases}
# \end{aligned}
# $$
# 
# where $c$ is the transaction cost and $w^b$ is the benchmark weight vector.
# 
# Having determined which stocks to buy and sell, we can now impose this as a constraint to the optimization problem. Specifically, we solve the problem:
# 
# $$
# \begin{aligned}
# \max_{\mathbf{w}^a}⁡ (\mathbf{w}^a)'\boldsymbol\mu-(\mathbf{w}^a-\mathbf{w}^b)'\mathbf{c} - A(\mathbf{w}^a)'\mathbf{\Sigma} \mathbf{w}^a
# \end{aligned}
# $$
# 
# subject to $(w^a)^TI=1$, any other relevant constraints, and the constraint that $w^a$ satisfies the transactions costs determined by $c$.
# Since $c$ is a fixed constraint and does not depend on the value of $w^a$ (as long as the additional constraints we imposed are satisfied), we can solve this problem using a conventional quadratic optimizer.
