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

# Factors

factors are crucial for financial modeling, and selecting the right ones is important for achieving outperformance. Good factors have a persistent and stable relationship with stock returns that can be explained by economic theory. The best way to find good factors is by using well-reasoned quantitative techniques rather than relying on superficial correlations produced by data mining. 

A factor in stock market analysis refers to any variable that has the ability to impact or predict stock returns. We can identify four broad types of factors:

- Fundamental Factors: Fundamental factors describe a company's financial condition and are calculated using data from the company's financial statements, such as the balance sheet, income statement, and cash flow statement. These factors are considered the most common in predicting stock returns and may include financial ratios, such as the price-to-earnings ratio, debt-to-equity ratio, or the return on assets ratio, among others. By analyzing these financial metrics, investors can gain insight into a company's financial health, earnings potential, and growth prospects.

- Technical Factors: Technical factors, on the other hand, are based on technical analysis and focus on the historical price and volume data of a stock. Technical analysts believe that patterns in the stock's price and volume movements can be used to predict future price movements. Technical factors include chart patterns, moving averages, trend lines, and momentum indicators, among others. These factors are used to make predictions about future price movements and to identify potential buying or selling opportunities.

- Economic Factors: Economic factors refer to broad macroeconomic trends and events that impact the stock market as a whole. For example, interest rates, inflation, gross domestic product (GDP), and unemployment are some of the most significant economic factors that can impact stock prices. Economic factors can have a direct effect on companies' earnings and can therefore affect the stock prices of individual companies and the overall stock market.

- Alternative Factors: Alternative factors refer to any factors that don't fall into the three categories mentioned above. They include a wide range of variables, such as sentiment indicators, news events, and company-specific events, among others. Alternative factors can be difficult to quantify and measure, but they can have a significant impact on stock prices, particularly in the short term. Alternative factors can help investors better understand the market sentiment and provide a complementary perspective to traditional fundamental and technical analysis.

## Fundamental Factors
The fundamental factors can be grouped into seven subcategories: valuation, size, operational efficiency, operating profitability, solvency, financial risk, and corporate activity. Valuation factors, such as the price-to-book (P/B) ratio and the price-to-earnings (P/E) ratio, help determine whether a stock is relatively cheap or expensive. Size factors, like market capitalization, attempt to categorize companies based on their size and examine the effect of size on stock return behavior. Operational efficiency factors, like inventory turnover, and operating profitability factors, like gross profit margin, offer insight into how well the company is being run by management. Solvency factors assess a company's ability to fulfill its short-term obligations in the future, with indicators such as the current ratio and the cash ratio. Financial risk factors, such as debt-to-equity and interest coverage ratios, gauge the financial stability of a company. Lastly, corporate activity factors pertain to decisions made by corporate executives or factors that do not fit into any of the other categories.

## Technical Factors
Technical factors are variables that are constructed from historical price and volume data, such as open prices, high prices, low prices, closing prices, volume, open interest, and bid and ask prices. Technical factors update themselves more frequently than fundamental factors and can be used to capture short-term changes in the relative value of stocks. Technical factors are categorized into four subcategories: liquidity risk factors, price-based factors, volume-based factors, and overall market movement factors.

Liquidity risk factors help assess the consequences of trading a stock. Price-based factors are generated mainly from stock prices or returns and are used to predict potential future price movements. Volume-based factors are created from past trading or volume data that may signal changing market participant behavior. Overall market movement factors are aggregate technical indicators that can provide insight into the stock market's overall movements and their implications for the near future.

## Economic Factors
Economic factors refer to variables that impact the overall macroeconomy and can have an effect on stock returns. These factors include popular indicators such as Gross Domestic Product (GDP) growth, yield-curve slope, unemployment, and inflation. These variables are usually considered in macroeconomic models of stock returns because they have the potential to influence a significant portion of the market. It is important for portfolio managers to be cautious while using macroeconomic data in their models because these data have a lag and might not be the latest available. They should also account for these delays when using the data in their models.

## Alternative Factors
Alternative factors are a group of factors used in financial analysis and modeling that do not fit into the traditional categories of fundamental, technical, and economic factors. There are three subcategories of alternative factors: analyst factors, captivus factors, and social responsibility factors. Analyst factors include information from Wall Street analysts such as earnings forecasts, buy-sell recommendations, and other relevant information that can be used to predict stock returns. Captivus factors include data captured through GPS, satellite, social media, or news feeds, often captured through sophisticated programs and with a higher frequency than traditional data sources, making it available earlier. Web scraping is a common method of obtaining captivus data. Lastly, social responsibility factors involve quantifying the relationships between management and employees, corporate governance, and issues related to diversity, including the composition of the board and discrimination practices.

# Factor choices
The building of investment models is a combination of science and art. However, in quantitative portfolio management, the manager must have a deep understanding of financial and economic theory to choose and combine factors appropriately. There are two types of quantitative stock return models: the fundamental factor model and the economic factor model. To choose factors for the former, univariate and multiple regression techniques can be used, while for the latter, unidimensional and multidimensional zero-investment portfolio techniques are suggested. Additionally, a simple correlation statistic or rank-correlation statistic can be used to determine the correlation among factor choices, helping in combining and grouping factors.

## Univariate Regression Tests
Portfolio managers often use simple regressions as a way to simplify the process of searching for relevant factors in stock returns. They start by identifying a group of factors ($\beta_{i,t}$) that they believe could explain stock returns ($r_{i,t}$) and then run *panel* regressions on each factor versus the stock returns in the universe. The panel regression provides an estimate of the relationship between the factor and stock returns, and if a factor ($f$) has (i) a significant value and (ii) theoretically correct sign, it is considered useful in explaining stock returns.
For example, 

$$r_{i,t}=\alpha +f\beta_{i,t}+\epsilon_{i,t}$$,

where $\beta_{i,t}$ is the factor exposure of stock $i$ at time $t$, and the estimate of $f$ from this panel regression will show the relationship between the factor and stock returns.

However, univariate regressions have a drawback in that they may lead to finding many variables that are significant in explaining stock returns but are actually surrogates for each other. For example, the P/E and P/B ratios may both explain stock returns, but they represent the same idea, so only one of them may be needed in the model. The ideal situation is to find factors that explain stock returns without being highly correlated with each other.

Despite these limitations, simple regressions are still used by many portfolio managers because they are easy to perform and provide an early idea of what might be relevant and what might not be. If there are too many potential factors, simple regressions can be used to make the first round of cuts. 

## Multiple Regression Tests
Multiple regression is a statistical method used to analyze the relationship between multiple explanatory factors and a response variable. It helps determine which factors impact the return and how significant that impact is. In this context, the portfolio manager is using multiple regression to identify the factors that impact stock returns.

The method starts with a reasonable number of factors, typically less than 10, and estimates a multivariate panel regression where each factor is analyzed for its exposure to the stock over time. Any factors that are found to be insignificant are dropped, while the significant factors are included in the final factor model.

However, there are several dangers associated with this method, including misspecification bias, data mining, and sequential specification search. Misspecification bias occurs when too many factors are included in the regression, leading to misleading statistical inference. Data mining is the process of searching for the best model that explains past stock returns, but it provides no guarantee that these factors will work in the future and does not provide any theoretical explanation for why these factors were chosen. Sequential specification search is the process of starting with a list of factors, dropping and adding variables based on significance, and eventually obtaining a desired level of significance in explaining stock returns. This can also lead to exaggerated statistical significance and make it difficult for the investment committee to evaluate the truth of the final model.

To avoid these dangers, the best advice is to start with a strong theoretical explanation for why a certain model with certain factors will work. The model should be tested over a variety of time periods for robustness and the portfolio manager should be cautious about adding and dropping variables.

## Unidimensional Zero-Investment Portfolio
The Unidimensional Zero-Investment Portfolio method is a technique used by portfolio managers to assess the impact of a specific factor on stock returns. The objective is to determine whether the factor has a significant effect on the returns of a portfolio and to measure the benefits of using this factor for stock selection.

The method involves dividing the universe of stocks based on a specific factor exposure, such as the P/B ratio, into equal portions, such as quintiles. A portfolio is then constructed from the first quintile and another from the fifth quintile. The returns of the first quintile are subtracted from those of the fifth quintile to obtain the returns of the hypothetical zero-investment portfolio. The term "zero investment" refers to the fact that theoretically no capital is required to create the portfolio.

The procedure involves ranking the stocks based on the factor exposure, constructing portfolios from the first and fifth quintile, computing the returns of the portfolios, and then calculating statistics on the historical returns of the first-quintile portfolio minus the fifth-quintile portfolio.

To determine the significance of the results, a statistical test is performed using the t-statistic. The t-statistic is calculated as the ratio of the sample average of the portfolio returns to the standard error of the mean. If the absolute value of the t-statistic is greater than 2, the average portfolio return is considered to be significantly different from zero and the factor is considered to be statistically significant.

## Multidimensional Zero-Investment Portfolio

Multidimensional Zero-Investment Portfolio is a method of constructing portfolios that examines the joint impact of multiple factors on stock returns. It is a more rigorous approach than the unidimensional approach, which only looks at the effect of one factor at a time.

To create a multidimensional zero-investment portfolio, the portfolio manager first ranks all stocks based on each factor of interest, such as size and price-to-book ratio. The stocks are then grouped into joint quintiles or deciles based on these rankings. For example, if the portfolio manager wants to create 10 groups out of each factor, there will be 100 groups in total (10 portfolios based on size and 10 portfolios based on P/B ratio). The portfolio manager can obtain these 100 portfolios by taking the intersections of these portfolios.

The method of creating the zero-investment portfolios depends on the objective of the portfolio manager. If the manager is interested in the joint impact of small size and low P/B ratio on stock returns, they can construct a zero-investment portfolio by taking a long position on the small-low portfolio and a short position on the large-high portfolio. T-statistics can then be calculated to determine the significance of the joint effect of the factors.

Alternatively, the manager can apply a multiple regression analysis. For each factor considered, an indicator variable is defined that takes the value of 1 if the stock belongs to the top division (e.g., quintile), −1 if the stock belongs to the bottom division, and 0 otherwise. Running a regression of stock returns on these indicator variables will result in coefficients that can be interpreted as the returns to suitably constructed zero-investment portfolios. The significance of the multiple regression can then be taken as an indicator of the joint significance of the selected factors.

## Reducing the Number of Factors
The main techniques to reduce the number of factors are based on the correlation among factors, and the three most commonly used statistics to determine this correlation are the Pearson correlation coefficient, the Spearman rank correlation coefficient, and Kendall’s τ. It is important to note that all three methods need to be adjusted for the panel structure of the data to provide accurate results.

The Pearson correlation coefficient measures the linear relationship between two variables. It ranges from -1 to 1, with -1 indicating a strong negative linear relationship, 1 indicating a strong positive linear relationship, and 0 indicating no linear relationship. The Pearson correlation coefficient is calculated by subtracting the mean from each variable, and calculating the sample covariance and standard deviation.

The Spearman rank correlation coefficient is a non-parametric measure of the monotonic relationship between two variables. Unlike the Pearson coefficient, which measures the linear relationship, the Spearman coefficient measures the strength and direction of the relationship between two variables while taking into account the ordering of their values, rather than the actual values themselves. The Spearman coefficient also ranges from -1 to 1, with -1 indicating a strong negative monotonic relationship, 1 indicating a strong positive monotonic relationship, and 0 indicating no monotonic relationship.

Kendall’s τ is a measure of rank correlation that determines the probability that the ranking by one variable is identical to the ranking by another. It ranges from -1 to 1, with -1 indicating a strong negative rank correlation, 1 indicating a strong positive rank correlation, and 0 indicating no rank correlation. Kendall’s τ is calculated by aggregating the number of pairs for which the rankings by two variables are the same minus the number of pairs for which the rankings by two variables are opposite, over the total number of pairs, for each period.

# Adjusting the Significance of Factors
Data mining can be dangerous as it may result in overstating the statistical evidence. This occurs when a factor is considered statistically significant based solely on a large t-statistic compared to the conventional critical value of 1.96. However, this approach can lead to a high probability of false discovery as it does not take into account other factors that may have been considered. To mitigate these risks, two approaches have been proposed in the academic literature. The first, the Bonferroni-type adjustment, is a frequentist statistical approach that considers the distribution of all possible t-statistics under the assumption of the null hypothesis. The second approach is based on Bayesian statistical theory, which incorporates both data and personal beliefs to determine the subjective probability of the null hypothesis being true. Both methods can help reduce the danger of data mining, but cannot completely eliminate it.

## Bonferroni adjustment 
The Bonferroni adjustment is a statistical method used to control the false discovery rate when considering multiple factors. It involves adjusting the significance level based on the total number of factors being tested. The critical p-value is calculated as the significance level divided by the number of factors (α/M). The critical t-value is then determined from the critical p-value using the standard normal distribution function. A variation of the Bonferroni adjustment is the Holm adjustment, which involves ordering the factors based on their t-values and determining the number of significant factors based on the entire set of p-values. However, the challenge with both the Bonferroni and Holm adjustments is determining the number of factors being considered. Some researchers have suggested using the number of published and unpublished research articles, but this number is constantly changing and is not always easily accessible.

## Bayesian adjustment
The Bayesian adjustment method uses Bayes' rule to determine the probability of a null hypothesis being true based on prior beliefs and observed data. The critical value of a t-test is then determined using the minimum Bayes factor (MBF), which is the minimum value of the likelihood ratio calculated from all alternative hypotheses. The critical t-value at a significance level of 5% corresponds to the 95% posterior probability of the null hypothesis being true. 

# Outliers
An outlier is a data point in a distribution that is significantly different from the rest of the data and appears to be inconsistent with it. The reason for this discrepancy could be due to errors in data collection or measurement, or it could reflect legitimate new information. In the case of data errors, it is common for the portfolio manager to remove the outlier entirely. If the outlier is accurate and represents novel information, it should be kept. However, in practice, the portfolio manager may not be able to determine the cause of the outlier and may choose to modify its value for safety. This does not diminish its significance compared to other stocks.

There are two possibilities in the theoretical framework for outliers. 
- The first (null hypothesis) assumes that all observations come from distribution A and there are no outliers. 
- The second (alternative hypothesis) assumes that most observations come from distribution A, but some come from distribution B, and these are considered outliers. 
To apply this categorization in real-life data, we need to know or make assumptions about distribution A. If we are uncertain about distribution A, detecting outliers becomes challenging and excluding these observations from the analysis may not be justified.

Common techniques for outlier detection assume that the underlying distribution is normal, but there are also methods for non-normal distributions.
Handling outliers involves two steps. 
- In the first step, outliers are identified and labeled. 
- In the second step, a decision is made on how to deal with the outliers. This could include removing them (trimming or truncation), replacing their values with a less extreme value (winsorization), or using a different approach.

## The Z-Score Approach
To address potential outliers, one approach is to label stocks with Z-scores greater than 3 in absolute value as outliers. However, this method is not reliable as it relies on the extreme values used to calculate means and standard deviations. 
A more robust method is the modified Z-score method, where the median, instead of the standard deviation, is used to calculate the Z-score. Any observations with a modified Z-score greater than or equal to 3 are considered outliers. After identifying the outliers, they can be removed or their values can be modified.

Winsorization involves replacing outliers with alternative values to prevent them from having a disproportionate impact on the results. One form of winsorization is to replace Z-scores greater than 3 with the value 3 and Z-scores less than -3 with -3.

Trimming is the process of removing n/2 of the largest and n/2 of the smallest values, and then recalculating the Z-scores for the remaining data. Another variation of trimming involves simply removing Z-scores with absolute values greater than a certain value, such as 3, 4, or 5.

## The Interquartile Approach
The interquartile method is a useful technique for handling outliers when developing qunatitative models. To apply this method, calculate the interquartile range (IQR) of each factor across the stock universe. This value represents the middle 50% of factor values and is determined by subtracting the first-quartile (Q1) from the third-quartile (Q3) of each factor. Next, a decision must be made on what deviation from the 75th and 25th percentiles constitutes an outlier, which is known as the IQR coefficient. For instance, if the IQR coefficient is set at 3, the upper and lower bounds of the factor can be calculated as:

$$
UB = Q3+3IQR,\quad and\quad LB = Q1-3IQR
$$

All stocks with factor values above the upper bound (UB) or below the lower bound (LB) are considered outliers and their values are set to missing. The Z-scores for the remaining stocks are then calculated. The Z-scores for the outlier stocks are fixed at the minimum and maximum of the non-outlier stocks' Z-scores.

## The Ranking Approach
A different approach to addressing outliers is by using a ranking method. Instead of using Z-scores based on the individual factors, the portfolio manager can use cross-sectional rankings. To do this, they would order the stocks by their factor value at each evaluation period and assign them a rank based on the value, with the highest value getting a rank of 1 and the lowest a rank of n (where n is the number of stocks). The Z-scores are then calculated using these ranks instead of the factor values. This eliminates the issue of outliers, but it also means that information about the difference in values between the stocks is lost and only the relative Z-score value between the stocks is retained. The Z-score for each stock in a given month can be determined using the following formula:

$$
z_{i,t}^{rank} = \frac{rank(f_{i,j}-\sum_{i=1}^{N} rank(f_{i,j})/N }{\sigma_{rank}(f_{i,j}}
$$

where rank represents the numerical rank of each stock in the universe, from highest to lowest, based on the factor value.

## The Percentile Ranking Method


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

