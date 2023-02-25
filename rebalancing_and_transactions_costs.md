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

# 8) Rebalancing and transactions costs
In April 2020, Invesco made a costly rebalancing error with its Equally-Weighted S&P 500 Fund, which resulted in a loss of $105 million over five days. Even without such errors, transaction costs associated with rebalancing can significantly affect a fund's returns. For instance, small-cap growth managers who traded frequently in 2019 incurred annual trading costs of over 2.5%, while those who traded more cautiously had trading costs below 1%, ultimately affecting their net returns. This illustrates the importance of rebalancing decisions and the need to consider transaction costs when adjusting portfolios.

Rebalancing decisions may be triggered by cash inflows, outflows, or changes in underlying stock-return model parameters. While cash inflows and outflows require adjustments to the portfolio's positions, changes in parameters do not necessarily require rebalancing. When the decision to rebalance is made, transactions costs become a significant consideration in determining the optimal portfolio composition. However, transactions costs are often ignored during the initial creation of the portfolio, as they do not have a significant impact.

In this chapter, we discuss the rebalancing decision, how transactions costs affect the optimal portfolio, and ways to control these costs. We also highlight the impact of transactions costs on individual stocks within a portfolio, which can significantly affect their expected returns. Understanding and managing transactions costs is crucial for portfolio managers in ensuring investment success.

# When and how to make the right decisions
The decision to rebalance a portfolio involves two key considerations: when to rebalance and how to do it. Determining the optimal rebalancing period is relatively straightforward from an econometric perspective. The factor model used to select stocks specifies a particular rebalancing frequency. For example, if the model was estimated using monthly returns, then the optimal portfolio is only valid for one month. If quarterly returns were used, then the portfolio would be optimal for one quarter. The rebalancing period is simply the model's periodicity, which is discussed in the first part of this section.

The more complex aspect of rebalancing involves deciding how to adjust the model's parameters, such as α, to update the portfolio. This can be a challenging task, as it requires balancing the potential benefits of improving the portfolio's performance against the costs associated with incurring transactions costs. In the second part of this section, we will explore different strategies for adjusting the portfolio's parameters to effectively rebalance the portfolio while minimizing costs.

## Rebalancing and the importance of model periodicity in financial markets

Financial experts have long acknowledged that models of stock returns are limited in their ability to predict daily returns accurately. While models can capture patterns that emerge over time, daily returns are heavily influenced by specific news and events that models often fail to consider. In the case of hourly returns, a model's predictive power is close to zero. Though some researchers have found moderate success in applying their models to weekly returns, such returns remain too susceptible to the influence of specific events.

The majority of financial research is thus conducted using monthly returns. While longer periods such as annual or quarterly returns offer a larger sample size, the risk of unstable parameters and changing market conditions make monthly returns a viable middle-of-the-road solution to the tradeoff between predictive power and parameter stability.

The decision to rebalance a portfolio hinges on several factors, including market stability and external restrictions on the portfolio manager. The common recommendation is to update the estimation of models at least once a month to ensure the most current information is available, and from there, decide whether to rebalance. Model periodicity is crucial to understanding when to rebalance and how to go about it. The first question of when to rebalance is relatively straightforward, while the second question of how to adjust parameters to update the portfolio requires more careful consideration. We will discuss the latter in the following section.


## Adjusting α and other parameters
Modifications to the parameters of a stock-return model may trigger rebalancing. As previously discussed in the factor model, the stock return can be represented as:

$$
r_i = \alpha_i+\beta_{i,1}f_1+\cdots+\beta_{i,K}f_K+\epsilon_i
$$

If we employed an economic factor model to anticipate stock returns, we should be alert for changes in α and the factor exposures ($\beta_{i,1}, \cdots, \beta_{i,K}$). If the model is the fundamental factor model, then we should be mindful of α and the factor premiums ($f_1, \cdots, f_K$).
Parameters can shift anytime, and corporate actions and significant alterations in the business environment all impact a model's parameters. For example, if Firm A merges with Firm B, the α and other parameters of Firm A will most likely change. If the government imposes a new restriction on the activity of Firm A, its α and other parameters will also most likely change. Even the retirement of a CEO can affect a stock's parameters. Additionally, there are changes that are not publicly disclosed. If the portfolio manager bases α on private information, α could react to new private information.
Quantitative portfolio managers must always keep the model in mind. If a manager comes across negative news about a stock, they should take some time to consider whether the news lowers the value of α or another parameter.

When the portfolio manager suspects that a parameter has changed, it is necessary to re-estimate the model. Updating the parameter values updates the expected return and risk of each stock, and it alters the optimal portfolio. After determining the new optimal portfolio, the manager can decide whether to rebalance the portfolio by weighing the benefits of rebalancing against the transaction costs.

# Understanding transactions costs
Transaction costs refer to the expenses incurred when buying or selling financial assets. In addition to the commission charged by the broker, there are other hidden costs associated with trading that investors should be aware of.

* One such cost is the **bid-ask spread**, which is the difference between the highest price a buyer is willing to pay (the bid price) and the lowest price a seller is willing to accept (the ask price). This spread can vary depending on the liquidity of the asset, with less liquid assets having a wider spread. For example, a small-cap stock with low trading volume may have a wider bid-ask spread than a large-cap stock with high trading volume.

* Another hidden cost is the **price impact**, which is the effect of a large buy or sell order on the market price of the asset. When a large order is placed, it can move the market price, causing the investor to pay more when buying or receive less when selling than the price quoted before the trade. The size of the price impact depends on the size of the order relative to the market size or daily trading volume of the asset.

While broker commissions are generally straightforward, bid-ask spreads and price impacts are harder to estimate. These costs can vary over time and depend on a variety of factors, making it difficult to predict the exact cost of a trade. However, investors can estimate these costs using historical data and by consulting with their broker or financial advisor.

For example, let's say an investor wants to buy shares of a newly-listed company. Due to the lack of trading history and low liquidity, the bid-ask spread is wide, at 5% of the share price. Additionally, the investor's order is large relative to the trading volume, resulting in a price impact of 2%. Including the commission charged by the broker, the total transaction cost for this trade would be around 7%. In contrast, if the investor wanted to buy shares of a well-established company with high trading volume, the bid-ask spread may only be 0.1% and the price impact negligible, resulting in a much lower transaction cost of around 0.5%.

Overall, understanding transaction costs is an important aspect of investing, as it can have a significant impact on investment returns over time. By estimating and minimizing these costs, investors can increase their chances of achieving their financial goals.


# Modeling transaction costs
Modeling transaction costs can be a challenging task due to their complex and unpredictable nature. Conventionally, a fixed proportion of the total transaction value is used to approximate transaction costs, represented by a constant denoted as $c$. For example, if $c$ is set to 5 or 10 basis points, then the transaction cost per dollar transaction would be $10 \times c$ for a transaction value of $10.

Calculating the total transaction value (TV) is a straightforward process. To determine the current portfolio's dollar value ($V_t$), the weights of stocks in the current portfolio ($w_1^b,\cdots,w_N^b$) and the weights of stocks in the future portfolio ($w_1^a,\cdots,w_N^a$) are used. The superscripts 'b' and 'a' denote 'before' and 'after', respectively. The current holding of stock $i$ in dollar terms is represented by $V_tw_i^b$, and the future holding of stock $i$ in dollar terms is represented by $V_tw_i^a$. If $V_tw_i^a$ is greater than $V_tw_i^b$, buying stock $i$ is suggested. On the other hand, if $V_tw_i^a$ is smaller than $V_tw_i^b$, selling stock $i$ is suggested. The difference between $V_tw_i^a$ and $V_tw_i^b$, represented as $V_tw_i^a-V_tw_i^b$, indicates the amount to buy or sell, in dollar terms. Therefore, the transaction value is the sum of this difference across all stocks, which is given by 

$$
\text{TV} = \sum\limits_{i=1}^N|V_tw_i^a-V_tw_i^b|
$$

The transaction cost (TC) is a constant fraction of the transaction value, represented by $cV_t\sum\limits_{i=1}^N|w_i^a-w_i^b|$. To include the transaction cost formula in an optimization problem, it is useful to express TC as a linear function, which is given by 

$$
\text{TC} = V_t\sum\limits_{i=1}^Nc_i(w_i^a-w_i^b)
$$ 

The values of $c_i$ depend on the values of $w_a$ and $w_b$. If $w_i^a>w_i^b$, then $c_i$ is set to $c$. Conversely, if $w_i^a<w_i^b$, then $c_i$ is set to $-c$. By defining the vector of current weights as $w_b$, the vector of future weights as $w_a$, and the vector of transactions costs as $c$, the transaction cost can be expressed as a vector product of the weight vector and the transactions cost vector. Therefore, 

$$
\text{TC} = V_t(w^a-w^b)^\top c
$$

To account for different stocks having different transaction costs, transaction costs can be modeled as proportional to the liquidity of each stock, considering the bid-ask spread and the price impact. The trading cost can be assumed to be inversely proportional to the average trading volume of each stock. In this case, elements of $c$ would have different signs and absolute values.


