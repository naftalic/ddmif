#!/usr/bin/env python
# coding: utf-8

# # 8) Rebalancing and transactions costs
# In April 2020, Invesco made a costly rebalancing error with its Equally-Weighted S&P 500 Fund, which resulted in a loss of $105 million over five days. Even without such errors, transaction costs associated with rebalancing can significantly affect a fund's returns. For instance, small-cap growth managers who traded frequently in 2019 incurred annual trading costs of over 2.5%, while those who traded more cautiously had trading costs below 1%, ultimately affecting their net returns. This illustrates the importance of rebalancing decisions and the need to consider transaction costs when adjusting portfolios.
# 
# Rebalancing decisions may be triggered by cash inflows, outflows, or changes in underlying stock-return model parameters. While cash inflows and outflows require adjustments to the portfolio's positions, changes in parameters do not necessarily require rebalancing. When the decision to rebalance is made, transactions costs become a significant consideration in determining the optimal portfolio composition. However, transactions costs are often ignored during the initial creation of the portfolio, as they do not have a significant impact.
# 
# In this chapter, we discuss the rebalancing decision, how transactions costs affect the optimal portfolio, and ways to control these costs. We also highlight the impact of transactions costs on individual stocks within a portfolio, which can significantly affect their expected returns. Understanding and managing transactions costs is crucial for portfolio managers in ensuring investment success.
# 
# # When and how to make the right decisions
# The decision to rebalance a portfolio involves two key considerations: when to rebalance and how to do it. Determining the optimal rebalancing period is relatively straightforward from an econometric perspective. The factor model used to select stocks specifies a particular rebalancing frequency. For example, if the model was estimated using monthly returns, then the optimal portfolio is only valid for one month. If quarterly returns were used, then the portfolio would be optimal for one quarter. The rebalancing period is simply the model's periodicity, which is discussed in the first part of this section.
# 
# The more complex aspect of rebalancing involves deciding how to adjust the model's parameters, such as α, to update the portfolio. This can be a challenging task, as it requires balancing the potential benefits of improving the portfolio's performance against the costs associated with incurring transactions costs. In the second part of this section, we will explore different strategies for adjusting the portfolio's parameters to effectively rebalance the portfolio while minimizing costs.
# 
# ## Rebalancing and the importance of model periodicity in financial markets
# 
# Financial experts have long acknowledged that models of stock returns are limited in their ability to predict daily returns accurately. While models can capture patterns that emerge over time, daily returns are heavily influenced by specific news and events that models often fail to consider. In the case of hourly returns, a model's predictive power is close to zero. Though some researchers have found moderate success in applying their models to weekly returns, such returns remain too susceptible to the influence of specific events.
# 
# The majority of financial research is thus conducted using monthly returns. While longer periods such as annual or quarterly returns offer a larger sample size, the risk of unstable parameters and changing market conditions make monthly returns a viable middle-of-the-road solution to the tradeoff between predictive power and parameter stability.
# 
# The decision to rebalance a portfolio hinges on several factors, including market stability and external restrictions on the portfolio manager. The common recommendation is to update the estimation of models at least once a month to ensure the most current information is available, and from there, decide whether to rebalance. Model periodicity is crucial to understanding when to rebalance and how to go about it. The first question of when to rebalance is relatively straightforward, while the second question of how to adjust parameters to update the portfolio requires more careful consideration. We will discuss the latter in the following section.
# 
# 
# ## Adjusting α and other parameters
# Modifications to the parameters of a stock-return model may trigger rebalancing. As previously discussed in the factor model, the stock return can be represented as:
# 
# $$
# r_i = \alpha_i+\beta_{i,1}f_1+\cdots+\beta_{i,K}f_K+\epsilon_i
# $$
# 
# If we employed an economic factor model to anticipate stock returns, we should be alert for changes in α and the factor exposures ($\beta_{i,1}, \cdots, \beta_{i,K}$). If the model is the fundamental factor model, then we should be mindful of α and the factor premiums ($f_1, \cdots, f_K$).
# Parameters can shift anytime, and corporate actions and significant alterations in the business environment all impact a model's parameters. For example, if Firm A merges with Firm B, the α and other parameters of Firm A will most likely change. If the government imposes a new restriction on the activity of Firm A, its α and other parameters will also most likely change. Even the retirement of a CEO can affect a stock's parameters. Additionally, there are changes that are not publicly disclosed. If the portfolio manager bases α on private information, α could react to new private information.
# Quantitative portfolio managers must always keep the model in mind. If a manager comes across negative news about a stock, they should take some time to consider whether the news lowers the value of α or another parameter.
# 
# When the portfolio manager suspects that a parameter has changed, it is necessary to re-estimate the model. Updating the parameter values updates the expected return and risk of each stock, and it alters the optimal portfolio. After determining the new optimal portfolio, the manager can decide whether to rebalance the portfolio by weighing the benefits of rebalancing against the transaction costs.
# 
# # Understanding transactions costs
# Transaction costs refer to the expenses incurred when buying or selling financial assets. In addition to the commission charged by the broker, there are other hidden costs associated with trading that investors should be aware of.
# 
# * One such cost is the **bid-ask spread**, which is the difference between the highest price a buyer is willing to pay (the bid price) and the lowest price a seller is willing to accept (the ask price). This spread can vary depending on the liquidity of the asset, with less liquid assets having a wider spread. For example, a small-cap stock with low trading volume may have a wider bid-ask spread than a large-cap stock with high trading volume.
# 
# * Another hidden cost is the **price impact**, which is the effect of a large buy or sell order on the market price of the asset. When a large order is placed, it can move the market price, causing the investor to pay more when buying or receive less when selling than the price quoted before the trade. The size of the price impact depends on the size of the order relative to the market size or daily trading volume of the asset.
# 
# While broker commissions are generally straightforward, bid-ask spreads and price impacts are harder to estimate. These costs can vary over time and depend on a variety of factors, making it difficult to predict the exact cost of a trade. However, investors can estimate these costs using historical data and by consulting with their broker or financial advisor.
# 
# For example, let's say an investor wants to buy shares of a newly-listed company. Due to the lack of trading history and low liquidity, the bid-ask spread is wide, at 5% of the share price. Additionally, the investor's order is large relative to the trading volume, resulting in a price impact of 2%. Including the commission charged by the broker, the total transaction cost for this trade would be around 7%. In contrast, if the investor wanted to buy shares of a well-established company with high trading volume, the bid-ask spread may only be 0.1% and the price impact negligible, resulting in a much lower transaction cost of around 0.5%.
# 
# Overall, understanding transaction costs is an important aspect of investing, as it can have a significant impact on investment returns over time. By estimating and minimizing these costs, investors can increase their chances of achieving their financial goals.
# 
# 
# # Modeling transaction costs
# Modeling transaction costs can be a challenging task due to their complex and unpredictable nature. Conventionally, a fixed proportion of the total transaction value is used to approximate transaction costs, represented by a constant denoted as $c$. For example, if $c$ is set to 5 or 10 basis points, then the transaction cost per dollar transaction would be $10 \times c$ for a transaction value of $10.
# 
# Calculating the total transaction value (TV) is a straightforward process. To determine the current portfolio's dollar value ($V_t$), the weights of stocks in the current portfolio ($w_1^b,\cdots,w_N^b$) and the weights of stocks in the future portfolio ($w_1^a,\cdots,w_N^a$) are used. The superscripts 'b' and 'a' denote 'before' and 'after', respectively. The current holding of stock $i$ in dollar terms is represented by $V_tw_i^b$, and the future holding of stock $i$ in dollar terms is represented by $V_tw_i^a$. If $V_tw_i^a$ is greater than $V_tw_i^b$, buying stock $i$ is suggested. On the other hand, if $V_tw_i^a$ is smaller than $V_tw_i^b$, selling stock $i$ is suggested. The difference between $V_tw_i^a$ and $V_tw_i^b$, represented as $V_tw_i^a-V_tw_i^b$, indicates the amount to buy or sell, in dollar terms. Therefore, the transaction value is the sum of this difference across all stocks, which is given by 
# 
# $$
# \text{TV} = \sum\limits_{i=1}^N|V_tw_i^a-V_tw_i^b|
# $$
# 
# The transaction cost (TC) is a constant fraction of the transaction value, represented by $cV_t\sum\limits_{i=1}^N|w_i^a-w_i^b|$. To include the transaction cost formula in an optimization problem, it is useful to express TC as a linear function, which is given by 
# 
# $$
# \text{TC} = V_t\sum\limits_{i=1}^Nc_i(w_i^a-w_i^b)
# $$ 
# 
# The values of $c_i$ depend on the values of $w_a$ and $w_b$. If $w_i^a>w_i^b$, then $c_i$ is set to $c$. Conversely, if $w_i^a<w_i^b$, then $c_i$ is set to $-c$. By defining the vector of current weights as $w_b$, the vector of future weights as $w_a$, and the vector of transactions costs as $c$, the transaction cost can be expressed as a vector product of the weight vector and the transactions cost vector. Therefore, 
# 
# $$
# \text{TC} = V_t(w^a-w^b)^\top c
# $$
# 
# To account for different stocks having different transaction costs, transaction costs can be modeled as proportional to the liquidity of each stock, considering the bid-ask spread and the price impact. The trading cost can be assumed to be inversely proportional to the average trading volume of each stock. In this case, elements of $c$ would have different signs and absolute values.
# 
# # Portfolio Construction
# Portfolio construction always adheres to the principle of selecting a portfolio with the optimal combination of expected return and risk, regardless of any constraints or costs that may arise. When managing against a benchmark, the goal is to find the best combination of expected excess return and tracking error. Transactions costs are a new factor to consider when determining the optimal portfolio or tracking portfolio, but they do not change the selection principle itself.
# 
# ## The Optimal Portfolio with Transactions Costs
# When optimizing a portfolio with transactions costs, we can frame the problem as minimizing risk for a given expected return, or as maximizing the risk-adjusted return, which is defined as the expected return minus the variance. To account for transactions costs, we must recalculate the expected return of the portfolio, which now includes subtracting the cost from the ending portfolio value and the expected return. The effective expected return has three components: the gross expected return, the transactions cost expressed as a fraction of the portfolio value, and the time value of the transactions cost. However, for realistic values of transactions cost and expected return, the time value is negligible, so we can ignore it.
# 
# To express the risk-adjusted return, we use additional notation, such as the expected return vector $μ$ and the variance-covariance matrix of stock returns $\Sigma$. The risk-aversion parameter is denoted as $A$, where a value of 2 means that the portfolio manager would tolerate a 1% increase in variance if the expected return increased by 2%. The risk-adjusted return is then calculated as the expected return minus $A$ times the variance of the prospective portfolio return.
# 
# Considering transactions costs, the effective risk-adjusted return is expressed as the expected return of the prospective portfolio minus the transactions costs, minus $A$ times the variance of the prospective portfolio return. 
# 
# $$
# \text{effective risk-adjusted return} = \mu_P-(w^a-w^b)^Tc-A\sigma^2_P
# $$
# 
# Maximizing the effective risk-adjusted return subject to relevant constraints gives us the optimal portfolio. However, the effective risk-adjusted return is highly nonlinear since the transactions cost vector depends on the weight vector, so conventional quadratic optimization techniques cannot be used to solve this problem.
# 
# # The Tracking Portfolio with Transactions Costs
# If a portfolio manager is more concerned about minimizing tracking error than overall risk, they should aim to maximize the effective tracking-error-adjusted return instead of the effective risk-adjusted return.
# 
# Recall that the portfolio's tracking error (TE) is defined as the standard deviation of the difference between the portfolio return $r_P$ and the benchmark return $r_B$:
# 
# $$
# \begin{aligned}
# \text{TE}^2 &= V(r_P)-2C(r_P,r_B)+V(r_B)\\
# &= w^T\Sigma w-2w^T\gamma+V(r_B)\\
# \end{aligned}
# $$
# 
# where $\gamma=C(r,r_B)$.
# Note that the last term is constant and does not depend on the weight vector, so only the first two terms will be used in the optimization problem.
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
# subject to the constraint that the sum of weights should be 1 and any other constraints. However, this problem cannot be solved using conventional quadratic optimization techniques because $c$ is a function of $w$.
# 
# # Dealing with Cash Flow
# In this section, we explore strategies that portfolio managers can use to minimize transaction costs when dealing with cash inflows or outflows. One approach is to invest cash temporarily in index futures or ETFs until a more suitable time arises to return it to the portfolio. This can help the manager avoid making rushed investment decisions in response to cash movements.
# 
# Another method is to purchase specific stocks that are more liquid, enabling the manager to achieve target portfolio weights with fewer transactions. By doing so, transaction costs can be reduced, and the impact of cash flows on the portfolio's performance can be minimized.
# 
# ## Reducing Transaction Costs with Futures and ETFs
# When managing a portfolio with daily cash inflows and outflows, it may be impractical to adjust the portfolio with every cash movement. For small daily flows, managers can invest net inflows temporarily in cash or rely on a cash buffer to handle small redemptions without significantly impacting portfolio returns. However, for funds with large daily net flows, a large cash reserve can negatively affect portfolio returns, especially in a low interest rate environment. In such cases, managers may need to adjust their exposure using either index futures or ETFs that invest in the same sector or a highly correlated sector.
# 
# ETFs that focus on specific sectors are widely available, but futures offer several advantages over ETFs. Futures are more liquid during normal trading hours, can be traded after hours on GLOBEX, and gains are treated as partly long-term and partly short-term for tax purposes. However, managers may face challenges rolling over futures contracts if the horizon for using futures is longer than a few days. Therefore, portfolio managers should carefully consider their options and choose the method that best fits their needs.
# 
# ## Rebalancing toward Optimal Target Weights
# In order to maintain an optimal mix of stock weights, portfolio managers may need to rebalance the portfolio during periods of cash flows or at the regular rebalancing period. For example, if a portfolio is rebalanced monthly and experiences cash flows at the end of the month, the manager can adjust the portfolio to maintain the original optimal portfolio weights or update the model to achieve new optimal weights. When faced with cash flows at the end of the month, the manager can trade in a way that redirects the portfolio towards the original or new optimal target weights.
# 
# To enable the manager to conduct optimal trades, we discuss the algorithm in the following subsections. Although we do not include trading costs in our analysis, we demonstrate that reducing the amount of trading can help to minimize tax costs and direct trading costs.
# 
# 
# ## Standard Rebalancing
# Standard rebalancing involves a portfolio manager aiming to rebalance the portfolio to a target set of stock weights. If the portfolio tracks a benchmark, the target weights will match those of the benchmark. The process involves selling the outperforming stocks and buying the underperforming ones since the last rebalancing date. This is done to ensure that the weights of stocks within the portfolio are restored to their target levels. The weight of stock $i$ in the portfolio before rebalancing is denoted as $w^b_i$, the target weight of each stock $i$ is denoted as $w^a_{i,t+1}$. Other notations include $p_i$ as the price per share of stock $i$, $s^b_i$ as the number of shares held in stock $i$ of the portfolio before rebalancing, and $s^a_{i,t+1}$ as the number of shares implicitly held in the optimal portfolio. The weights of the target portfolio and the current portfolio at any time $t+1$ are given by 
# 
# $$
# w^b_{i,t+1} = p_{i,t+1}s^b_{i,t+1}/V_{t+1}
# $$ 
# 
# and 
# 
# $$
# w^a_{i,t+1} = p_{i,t+1}s^a_{i,t+1}/V_{t+1}
# $$
# 
# respectively.
# 
# To rebalance the portfolio, one calculates the difference between the target weights and the current portfolio weights and uses this difference to determine the number of shares to buy or sell at time $t+1$. The number of shares of each stock that must be bought or sold is given by $x_{i,t+1}=s^a_{i,t+1}-s^b_{i,t+1}=\frac{w^a_{i,t+1}}{p_{i,t+1}}(V_{t+1}+C_{t+1})-s^b_{i,t+1}$, where $C_{t+1}$ represents any monetary contribution to or withdrawal from the portfolio at time $t+1$. The excess shares $x_{i,t+1}$ are negative if shares need to be sold and positive if shares need to be bought. It's worth noting that these formulas don't account for bid-ask spreads or price impact, both of which can distort the rebalancing process and create additional costs for the portfolio.
# 
# # Using Cash Flows to Rebalance without Selling
# To minimize costs associated with rebalancing a portfolio, it can be more advantageous to allow the portfolio to drift towards the optimal target portfolio, rather than making trades to exactly match it. There are tax costs associated with rebalancing, as selling securities with capital gains incurs taxes. Additionally, transaction costs are incurred with each purchase or sale of a security. Instead of selling securities, the portfolio manager can opt to buy more shares of the securities whose weights have fallen below target, which provides a push in the right direction towards the target.
# 
# To give the portfolio a push, the manager can use any cash inflows to add, proportionally to the optimal target weights, to all the portfolio's existing positions. A slightly more involved approach is to use an algorithm to invest cash inflows, which will bring the portfolio closer to its optimal weights at a faster pace. The easiest method is to divide the cash inflows among all of the portfolio's securities in amounts proportional to their target weights. For instance, if the portfolio has $C_{t+1}$ in cash to inject at time $t+1$, the manager will purchase $x_{i,t+1}$ of each security, where:
# 
# $$
# x_{i,t+1}=C_{t+1}w^a_{i,t+1}/p_{i,t+1}
# $$
# 
# The resulting new weights will fall between the weights before adjustment and the optimal target weights, and the proximity to the target weights will depend on the ratio of $C_{t+1}$ to $V_{t+1}$.
# 
# # Rebalancing by Purchasing Only Deficient Stocks
# One method for quickly aligning a portfolio with its benchmark weights is to invest new cash only in stocks that are below their target weights. The portfolio is divided into two groups: those stocks that exceed their target weights and those that fall short. To calculate these weights, the symbol $\tilde w^b$ is used to represent the portfolio's weights considering the current value of the portfolio and the cash inflow. The weight of each stock with the cash inflow is determined using the formula $\tilde w^b_{i,t+1}=s^b_{i,t+1}p_{i,t+1}/(V_{t+1+C_{t+1})}$. These portfolio weights are then compared to their corresponding target weights $w^a_{i,t+1}$.
# 
# To allocate cash to stocks that are below their target weight, the cash allocated to stock $i$ is determined using the formula $c_{i,t+1}=w^a_{i,t+1}(V_{t+1+C_{t+1}}-s^b_{i,t+1}p_{i,t+1})$. The sum of all cash allocated to these stocks is then calculated and subtracted from $C_{t+1}$ to determine the amount of slack funds. If there are not enough funds to restore deficient stocks to their required weights, the cash distributed to each stock is scaled down proportionally. The number of shares that need to be purchased for each stock is calculated using the formula $w_{i,t+1}=\frac{c_{i,t+1}}{p_{i,t+1}}\frac{C_{t+1}}{\sum\limits_{j=1}^{n_u}c_{j,t+1}}$.
# 
# This "buy" system for rebalancing helps the portfolio converge toward the optimal target weights at a faster rate than if new cash were invested in stocks in proportion to their target weights. To calculate the minimum amount of cash inflow required to perfectly rebalance the portfolio without selling, the ratio of the weight of each stock before rebalancing and before new money has been added to the target weight minus one is calculated for each stock. The maximum of these values is then multiplied by the total value of the portfolio $V_{t+1}$ at time $t+1$.
# 
# # Approximate Solution to the Optimal Portfolio Problem
# 
# Problems specified above to maximize the effective risk-adjusted return or effective tracking-error-adjusted return are not quadratic in $w^a$ and are difficult to solve with conventional quadratic optimizers. In this section we present a simple approximate solution that works very well for most situations.
# Nonlinearity arises because we do not know, before solving the problem, which stock to sell and which stock to buy. If we knew, the problem would be quadratic as usual. Thus, to avoid nonlinearity, we need to determine which stocks to buy and which stocks to sell **before** solving the optimization problem.
# We suggest the following shortcut. First, we can solve the problem **ignoring** the transactions costs. That is, solve
# 
# $$
# \max\limits_{w^a} w^a\mu-A(w^a)^T\Sigma w^a
# $$
# 
# subject to
# 
# $$
# (w^a)^TI=1
# $$
# 
# and any other relevant constraints. Call the solution to this problem $w^*=(w^*_1,\cdots, w^*_N)$. Then define the transactions cost vector $c = (c_1,\cdots, c_N)$ using these weights:
# 
# $$
# \begin{aligned}
# c_i=
# \begin{cases}
# c\quad &\text{if}\quad w^*_i>w^b_i\\
# -c\quad &\text{if}\quad w^*_i<w^b_i
# \end{cases}
# \end{aligned}
# $$
# 
# That is, we determine which stocks to buy and which stocks to sell based on the optimization without considering transactions costs. Once we have determined which stocks to buy and which stocks to sell, we can impose this as a constraint to the optimization problem. 
# 
# For example, In the case of Eq. (10.9), the problem to be solved becomes
# subject to
# and any other relevant constraints. Now c is a fixed constraint and does not depend on the value of wa (as long as the additional constraints we imposed are satisfied), and we can solve this problem using a conventional quadratic optimizer.
