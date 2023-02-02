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

# Stock Screening and Ranking
The goal of systematic teams is to make investing more reliable, repeatable, and quantitative by avoiding the biases and errors of traditional stock picking. There are two types of stock screening methods: sequential and simultaneous. In sequential screening, criteria are applied one after the other to eliminate stocks from the investment universe. In simultaneous screening, all criteria are applied at once, and all stocks receive a ranking based on their overall scores. The most popular simultaneous screening method is the z-score approach, which involves choosing factors that explain stock returns and aggregating them into one score to rank stocks. The z-score ranking can be used as the basis for a stock returns model or added to an existing model.

# Sequential Screening

Sequential Stock Screening is a simple and straightforward method for portfolio managers to select stocks for investment. It involves ranking stocks according to their favorable and unfavorable attributes and eliminating those that don't meet the criteria set by the portfolio manager. The process starts by defining the investment goals and selecting relevant factors, such as P/B ratio or profit margins, to screen the stocks. The screens are then applied in order of importance, starting with the most critical factor. An example of a sequential stock screening process would be selecting the top 25% of stocks with the highest profit margins and then selecting the top 10 of those with the highest B/P ratios. A good stock screen should be easy to automate, replicate, and accurately reflect the portfolio manager's preferences.

The key to a portfolio manager's success is the ability to determine factors that drive exceptional stock returns. Managers often have a guiding investment style or philosophy, but it can be quantified through stock screening methods. Here, we specify three successful equity managers' strategies, which can be qualitative or fundamental, and translates them into quantifiable screens.

- Lynch Screen: This is a combination of growth-and-value strategy that seeks a P/E ratio below the industry average but also a PEG ratio below 1.0. Other criteria include a P/E to dividend yield ratio less than 4.0, earnings growth between 0% and 50%, insider buying-to-selling ratio greater than 1.5, long-term debt ratio below industry median, market capitalization less than $5 billion, and institutional ownership less than 50%.

- Buffett Screen: This screen is based on Warren Buffett's buy-and-hold strategy and focuses on companies with a strong competitive advantage, efficient management, high free cash flow, return on equity greater than or equal to 15%, net profit margins exceeding industry averages, D/E ratio in line with or lower than industry median, and forecasted free cash flow for the next five years greater than the current market price of the stock when discounted back to the present. The screen restricts investments to the top 30% market capitalization of listed equities on the NYSE, AMEX, and NASDAQ.

- Lakonishok Screen: This is a value screen based on the work of Josef Lakonishok, CEO and founder of LSV Asset Management. The screen focuses on identifying undervalued companies with market capitalizations in the top 30% of the NYSE, AMEX, and NASDAQ. The screen seeks companies with a P/E ratio and P/B ratio below their respective industry median values, consensus earnings estimate for the next fiscal year greater than the current year's estimate, and a forecasted earnings growth rate greater than 5%.

# Simultaneous Screening
In simultaneous screening, a portfolio manager evaluates all stocks based on a set of criteria, considering all the factors at once instead of one at a time. This eliminates the risk of eliminating a good stock due to its poor performance in an early round of screening and ensures a larger pool of stocks to choose from. To aggregate the factors, the portfolio manager needs to standardize or normalize them by transforming them into a standard unit of measurement, such as the z-score method. This ensures that the variables are comparable and prevents any single factor from dominating the stock ranking.

# Z-score
The z-score is a statistical method used to standardize the values of a variable within a population of data. It measures how far away a particular observation is from the population mean. To calculate the z-score, the difference between the observed value and the mean of the population is divided by the standard deviation of the population. This results in a normalized score that shows how far the observation is from the norm in terms of standard deviations. Z-scores allow comparison of two different variables, as they are expressed in the same units. If the original data distribution is normal, the z-score can be used to make statements about the rarity or probability of a particular observation. To assign z-scores, the mean and standard deviation of the factor must be calculated for all stocks in the investment universe, and the z-score calculation must be performed for each stock. It is important to make sure that the factors being used are expressed such that high values are good and low values are bad, as the z-scores must match the underlying factor values.

# Simple Z-score Combination
When dealing with multiple factors, we can aggregate z-scores by combining the z-scores for each factor of a stock into a single screening value. The aggregate z-score is calculated by adding the z-scores for each factor of a stock, as z-scores are scale independent. The weighting of each factor in the aggregate z-score can be equal or determined through a sophisticated weighting scheme, with equal weighting being a common method used by portfolio managers due to its stable results. Extreme values in individual factors or stock aggregate z-scores can be handled through winsorizing or throwing out stocks with extreme values, but this may result in the loss of important information.

# Ad Hoc Z-Score Combination
Ad Hoc Aggregate Z-Score is a method of weighting the individual factor z-scores within the aggregate z-score. Portfolio managers use their own judgement and personal preferences to assign weights to the factors. This method can be influenced by past research or past reading and may not be entirely based on a systematic and quantitative approach. There are several variations of this method, including weighting factors according to their perceived importance, weighting based on the factors' information ratios, and weighting based on the portfolio manager's own investing style. The latter is done by amplifying the importance of the factor that is preferred over others. The method of weighting based on information ratios involves computing the historical information ratio of each factor by creating decile or quintile portfolios. Factors with higher information ratios are assigned more weight. However, this method also fails to take into account the correlation between factors.

# Optimized Z-Score Combination
The traditional approach of equally weighting the z-scores is simple, but it ignores important information contained in the data and fails to account for the correlation between factors. On the other hand, ad hoc methods of weighting, which assign weights based on the perceived importance of the factors, are highly subjective.

An alternative approach is to use econometrics to estimate the optimal exposures using a historical sample data set. The portfolio manager takes a series of monthly returns on all the stocks in the universe, combined with the factor z-score values for each stock at the beginning of the month, and runs a set of cross-sectional regressions to find the optimal Z-score weights.

The optimal combination of z-scores can be estimated through regression analysis using the historical data. This regression uses the variance-covariance matrix of z-scores and returns to estimate the parameter exposures of each factor. The portfolio manager can run this regression over different time periods and horizons to ensure the robustness of the results.

Another variation on the optimal weighting scheme is to determine the optimal weights for various economic scenarios. The portfolio manager creates several hypothetical economic environments and calculates a set of optimal z-score weights for each. This method is more subjective as it involves more judgment, but it allows the manager to consider the direction of the economic winds and weight the factors accordingly.

# Combination by Factor Groups
Quantitative portfolio managers may divide their K factors into M factor groups to organize and simplify the screening process. By creating factor groups that represent different aspects of stock returns, the manager can change the relative importance of each factor group according to changing economic conditions. The procedure for computing aggregate z-scores using factor groups is almost identical to the procedure for computing aggregate z-scores. The only difference is that the individual factors are classified into specific factor groups. To compute the aggregate z-score, the z-scores of each factor group are weighted and summed, and the resulting sum represents the aggregate z-score for each stock in the investment universe. The weighting scheme for the factors within and across groups can be determined using similar methods as the normal z-score aggregation without groups.

# Expected Return Implied by the Z-Scores

The expected return of a stock can be estimated by regressing actual stock returns on the aggregate z-scores. This can be done using a panel series regression of stock returns on the z-score of the prior periods (e.g., of the previous months)
The regression takes the form of
$$r_{i,t+1}=a+bz_{i,t}+\epsilon_{i,t+1}$$
where $a$ is a constant term, $b$ is the coefficient that relates the aggregate z-score to the stock return, and $\epsilon$ is the error term. With the estimated values of $a$ and $b$, the expected return of the stock for the next period can be calculated. However, this methodology has some limitations. Firstly, the z-scores may not change much over time but factor premiums ($b$) may change, leading to unstable or unreliable coefficients. Secondly, there may be a weak correlation between the z-score and subsequent returns, as the equation is not based on a rigorous theory. Lastly, this method adds complexity to the process, which is a drawback as the biggest advantage of the aggregate z-score model is its simplicity.

# Forecasting Rule of Thumb: derivation

Assuming a simple linear regression of the form $y=a+bx$, the equation can be expressed as follows:

$$
\begin{align}
E(y|x)-E(y)& =(a+bx)-[a+bE(x)] \newline
& =b(x-E(x)) \newline
& =\frac{C(y,x)}{V(x)}(x-E(x)) \newline
& =\frac{C(y,x)}{S(x)}\frac{x-E(x)}{S(x)} \newline
& =\frac{\rho(y,x)S(x)S(y)}{S(x)}z \newline
& =\rho(y,x) S(y) z \newline
& =\text{IC}\times \text{Volatility}\times \text{score}. 
\end{align}
$$

In the equation, $E$ represents the expected value, $\rho$ represents the Pearson correlation, $C$ represents the covariance, $V$ represents the variance, and $S$ represents the standard deviation.

$E(y|x)$ is the expected value of $y$ given a specific value of $x$, while $E(y)$ is the expected value of $y$ over all possible values of $x$.

$E(y|x)$ represents the average or expected value of $y$ for a given value of $x$, taking into account the uncertainty in the estimates of the regression coefficients $a$ and $b$. Mathematically, $E(y|x) = a + bx$, where $a$ and $b$ are the estimated intercept and slope coefficients, respectively, and $x$ is a specific value of the predictor variable.

$E(y)$ is the overall average or expected value of $y$ over all possible values of $x$ and can be calculated as the weighted average of $E(y|x)$ for all possible $x$ values, weighted by the probability distribution of $x$. Mathematically, $E(y) = ∫ E(y|x) p(x) dx$, where $p(x)$ is the probability distribution of $x$.

The term $E(y|x)-E(y)$ is the called the alpha or refined forecast as it represents the change in the expected value of y due to observing x. $\rho(y,x)$ the information coefficient (IC), $S(y)$ is the volatility, and $z$ the score. 

# Forecasting Rule of Thumb: interpretation
The forecasting rule of thumb is a formula derived from a regression equation used to predict stock returns based on aggregate (cross-sectional) z-scores

$$r_{i,t} = a+bz_{i,t−1} + ε_{i,t}.$$

The equation manipulates the correlation (IC) between the aggregate Z-score and the actual security returns and the cross-sectional volatility of the returns of the securities.

Specifically, the expected return of a stock conditional on the z-score is given by 

$$
\begin{align}
E[r_{i,t}|z_{i,t−1}] &= E[r_t] + b [z_{i,t−1} − E(z_{t−1})]\newline
&= E[r_t] + ρ(r_t, z_{t−1})S(r_t)z_{i,t−1}. 
\end{align}
$$

When estimated as a cross-sectional regression (or a panel regression), the estimates will be the best predictor of the realized return, that is,

$$
\begin{align}
\hat r_{i,t}=\hat{\bar{r}_t}+\hat\rho(r_t,z_{t-1})\hat S(r_t)z_{i,t-1}.
\end{align}
$$

# Forecasting Rule of Thumb: examples
The forecasting rule of thumb says that the difference between the expected return of a stock based on its previous z-score and its unconditional return is equal to the product of Information Coefficient (IC), volatility, and score. IC represents the correlation between a stock's return and its previous z-score, while volatility refers to the variability of returns across stocks. The score, in this context, refers to the value of the stock's z-score in the previous period.

- If IC is equal to 0, it means that there is no correlation between a stock's return and its previous z-score. This results in a conditional expected return of 0, implying that the regression coefficient, $\hat{b}$, would also be equal to 0.

- If volatility is equal to 0, it indicates that there is no variation in stock returns across stocks. In this case, there would be no way to forecast stock returns based on the variation in z-scores, which would result in a conditional expected return of 0 and a regression coefficient of 0.

- When the score is 0, it implies that the previous period's z-score value of the stock is 0. This would result in a conditional expected return of 0, as the conditioning variable, the z-score, has no signal. The regression coefficient, $\hat{b}$, could take on various values depending on the relationship between z-scores and stock returns.

# Practical comments
## Ranking
The aggregate Z-score ranks the expected returns or risks of various stocks, but it cannot be relied on solely to manage a portfolio's risk and return in comparison to a benchmark, except through basic techniques.

## Alpha
There are three methods to convert an aggregate Z-score of a stock into an expected return or alpha for portfolio construction, each with their own strengths and weaknesses. 
- The first method involves using the Z-score as the alpha value, which can then be combined with the expected returns calculated by another stock return model. This approach is simple for portfolio managers to implement, but the Z-score doesn't reflect the expected excess returns or relative risks of stocks.

- The second method is to perform a regression analysis of the aggregate Z-score against the cross-section of stock returns. This will provide estimates of expected stock returns, as well as relative risk, but does not give a direct estimate of alpha.

- The third method involves running a regression of excess stock returns not explained by another stock return model against the Z-scores. This approach focuses on a form of alpha, but is more complex to calculate and combines information from two different stock return models, potentially violating the information criterion.

## Outliers
To mitigate the risk of including data outliers in a portfolio, portfolio managers may choose to remove stocks with z-scores greater than 3. These z-scores may represent data points that are significantly different from the rest of the data and could have resulted from data errors or a true deviation of the stock from typical stocks. To prevent the distortion of the portfolio, portfolio managers will often exclude z-scores greater than 3.

Another approach to managing extreme z-scores is to round them off. This technique, known as windsorization, involves rounding values greater than 3 to 3 and values less than -3 to -3. This method can be useful when the data is not faulty but the portfolio manager wants to place limits on the extreme values.

A third option is to trim the z-scores. This involves eliminating a certain number of z-scores or stocks, with half of them being removed from the high side and half from the low side. The remaining z-scores are then recalculated and used in portfolio construction.

# Some Code
```{code-cell}
---
mystnb:
  figure:
    align: center
    caption_before: true
    caption: This is my table caption, above the table
---
import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,1,100)
sr = (2*w+(1-w))/np.sqrt(20*w**2+10*(1-w)**2)

print( w[np.argmax(sr)], np.max(sr) )
```

```{code-cell}
plt.plot(w,sr)
plt.show()
```

