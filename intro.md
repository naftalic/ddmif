# Data-Driven Methods in Finance (DDMIF)

## Introduction:

There are two major categories of quantitative equity portfolio management: active and passive. Passive approach, also known as indexing, aims to track a well-known index, such as the S&P 500, and minimize the tracking error. Active approach aims to outperform a benchmark or provide an absolute return without any reference to an index.

Investors can access active or passive portfolios through mutual funds, ETFs, or building their own portfolios. Major equity benchmarks for portfolio managers include S&P 500, Russell 3000, Wilshire 5000, NASDAQ-100, and MSCI USA.

Qualitative portfolio managers focus on intangibles and study company fundamentals, while quantitative portfolio managers use mathematical models to predict security returns. Famous qualitative portfolio managers include Peter Lynch and Warren Buffett. Quantitative portfolio management is usually associated with large institutions or hedge funds, such as Barclays Global Investors, Goldman Sachs Asset Management, and Parametric Associates.


## Fundamentals

Alpha refers, generaly, to two types of returns:
- Benchmark Alpha: Return of a portfolio not linked to its benchmark's risk or market portfolio's risk. Formula: $r_P = α + βr_B + ϵ$.
- Multi-Factor Alpha: Return of a portfolio not linked to multi-factors' risk. Formula: $r_P = α + β_1f_1 +...+β_Kf_K +ϵ$.

A few remarks: 
- $βr_B$ is the expected or consensus return, which is the part of the portfolio’s return related to the benchmark
- $α + ϵ$ is the residual return
- The residual return is all that matters to the quantitative portfolio manager
- If the benchmark return is positive, it is easy enough to generate higher returns simply by increasing the portfolio’s exposure to the benchmark, but the portfolio manager has not added value. 
- The residual return is the part that represents an increase in return independent of increased direct benchmark exposure. 
- $α$ is the expected value of the residual return
- $ϵ$, is the deviation of the residual return from its mean (it is assumed that $ϵ$ averages zero). 

Ex-ante Alpha is the expected alpha, and ex-post Alpha is the realized one, obtained through regression of portfolio and benchmark returns.

Ex-Post Information Ratio is the excess performance of a portfolio manager in terms of risk units, calculated as $IR = α_B / 𝜔$, where 𝜔 is the residual risk or excess risk.

An active portfolio manager aims for high alpha and high information ratio.

### The Market Rules:

- Efficiency prevails in markets with profits only possible through taking risk.
- Risk-free arbitrage does not exist.
- Quantitative Analysis (QA) seeks profit through statistical arbitrage by using all available information.
- QA must be based on solid economic theories and reflect persistent patterns.
- Deviations from the benchmark are acceptable only if they come with manageable uncertainty.

## Market efficiency:

- Weak form - security prices fully reflect all past market information. Hence, technical analysis is not expected to produce superior stock picks.
- Semi-strong form - security prices reflect all publicly available information, including macroeconomic fundamentals and analyst reports. Hence, relying on publicly available information for stock picking is not likely to be effective.
- Strong form - security prices reflect all publicly and privately held information, including inside information. Hence, using any form of privileged information is not expected to result in superior stock selection.

Can we test for market efficiency?

- Weak-Form Efficiency: This can be tested by examining the autocorrelation of stock returns and the presence of momentum and reversal effects.
- Semi-Strong Form Efficiency: This can be tested by looking for anomalies such as earnings surprise persistence, January effect, low P/B, P/E ratios, and neglected firm effects (e.g. small cap stocks).
- Strong Form Efficiency: This is challenging to test, but one way is to analyze insider trading transactions, limit order book data, and employee stock grants.


## Market Anomalies:

- Defining "Normal" Returns: To determine if a strategy violates market efficiency, it's necessary to define what is considered a "normal" or "expected" return. This can be done by using a zero-investment portfolio or a security pricing model (e.g. CAPM).

- Testing Strategy Returns: Using historical data, a strategy can be created and tested for excess returns that are statistically significant. For example, creating an equal-weight portfolio of stocks whose analyst ratings improved in the last month and running a regression analysis.

When testing for anomalies, it's important to be aware of data limitations and to ensure good organization of the data. A good knowledge of statistics and attention to detail is also critical to avoid mistakes in the analysis.

## Documented Market Anomalies and Features:

- Value Effect: Low P/E stocks outperform high P/E stocks, as well as P/B, P/S, and P/D ratio stocks.
- Features: P/E, P/B, P/S, and P/D ratio.

- Size Effect: Small-cap stocks outperform large-cap stocks.
- Feature: Market capitalization.

- January Effect: Small-cap and poor-performing stocks tend to outperform in January.
- Features: Low market capitalization and low returns in previous year.

- Calendar Effect: Outperformance is observed on specific days of the week, Halloween, weather events, etc.
- Features: Day of the week, Halloween, weather, daylight savings, etc.

- Neglected-Firm Effect: Low analyst coverage stocks have risk-adjusted excess returns.
- Features: Number of analysts following the stock.

- PEG Ratio Effect: Inverse relationship between PEG ratio and stock performance.
- Feature: PEG ratio.

- IPO Effect: IPOs underperform on a risk-adjusted basis in first 3-5 years.
- Feature: IPO status.

- Index-Change Effect: Stocks included in an index have positive returns, while those dropped have negative returns.
- Feature: Index-inclusion status.

- Momentum: Stocks that perform well in one period tend to continue performing well.
- Feature: Prior period return.

- Technical Indicators: Certain technical indicators provide excess returns.
- Features: Volume, RSI, Bollinger Bands, moving average, etc.

- Analyst Forecasts: Stocks with buy ratings outperform, though effect has weakened. Changes in ratings and earnings surprises predict returns.
- Features: Analyst recommendations.

- Insider Trading: Recent insider-bought stocks have excess returns and recent insider-sold stocks have negative returns.
- Features: Insider trades.

- Overreaction: Investors overreact to both good and bad news. Loser stocks tend to outperform winners over 3-5 years.
- Features: Returns based on news events.

- Stock Buybacks: Companies that buy back stock have positive risk-adjusted returns.
- Feature: Change in treasury stock.

- Stock Splits and Reverse Splits: Stock splits are followed by positive returns.
- Feature: Signals of a stock split.

- Spin-offs: Parent companies have excess returns after spin-off of subsidiary.
- Feature: Signals of spin-off.

- Accruals: Low accrual companies perform better than high accrual companies.
- Feature: Accruals in prior period.

- Low Volatility: Low historical volatility stocks outperform high volatility stocks.
- Feature: Historical volatility.

- Low Beta: Low beta stocks outperform high beta stocks on a risk-adjusted basis.
- Feature: Historical beta.

- Liquidity: Less liquid stocks have higher returns than more liquid stocks.
- Features: Share turnover and Amihud liquidity.

- Crowding: Stocks invested in by many money managers underperform less invested-in stocks.
- Features: Holdings-based measure and return-based measure of saturation by managers.

## Behavioral Anomalies 

Behavioral finance is a branch of finance that considers psychological and behavioral factors in investment decisions, leading to outcomes that differ from those predicted by rational decision-making theories. It recognizes profitable opportunities from investors' behavior.

Anomalies:

- Anchoring: Over-reliance on past reference or single piece of information in decision making.
- Ambiguity Aversion: Avoidance of unfamiliar stocks, preference for familiar ones.
- Availability Bias: Over-estimation of likelihood of future event due to a distorted memory.
- Confirmation Bias: Overweighting information that confirms beliefs, underweighting that contradicts.
- Disposition Effect: Holding on to losers too long, selling winners too soon.
- Endowment Effect: Demanding more to give up an object than willing to pay to acquire it.
- Escalation Bias: Compounding losses by putting more money into a bad investment.
- Herding Mentality: Following others even in investing.
- Illusion of Knowledge: Overreliance on data to understand a stock.
- Narrow Framing: Considering individual investments in isolation.
- Overconfidence: Over-estimation of abilities, leading to frequent trades and transaction costs.


# Why is market efficiency imperfect?

- Information is costly to obtain, not everyone can afford or wants to pay for it.
- Public information takes time to spread through the market.
- Not all investors have the capacity to process large amounts of information.
- Filtering public information creates private information.
- Investors may make decisions based on emotions rather than data.
- Efforts to exploit irrationality can cause inefficiencies.
- Economic conditions, including technology, constantly change and take time to adjust to.
- Transactions costs can diverge from economic models.
- Taxes affect market performance.
- Government regulations create deviations from ideal economic models.


## Brief history of financial theory

The modern financial theory has a history of over 100 years, starting from Bachelier's work in 1900 to today's portfolio risk measurement. The growth of quantitative equity portfolio management was accelerated by technological and theoretical advances in the late 20th century, but it's based on a vast literature of modern portfolio theory. Despite being widely used, many practitioners may not be aware of its origin. Here's a brief overview of the progress in investment philosophy. Knowledge of modern portfolio theory is valuable for both practitioners and students of finance, even if they later question its parts.

Louis Bachelier, a French mathematician, wrote "The Theory of Speculation" in 1900 and laid the foundation for dynamic security pricing. He showed that prices fluctuate randomly, making predictions impossible. In the 1930s, Alfred Cowles III found no evidence of professionals' ability to outperform the market after examining thousands of stock selections. This supports the notion that trying to predict the market was no better than flipping a coin.

In 1949, Benjamin Graham published "The Intelligent Investor" and introduced value investing. He believed that investors could pick stocks and beat the market by following certain rules, and his student, Warren Buffett, was successful in outperforming the S&P 500 Index. The concept of security analysis still exists today, although it was more prevalent in the past. John Maynard Keynes also managed the Cambridge Trust fund with a small portfolio of stocks he knew, reflecting the world of investing before modern portfolio theory.

Before Warren Buffett started his first investment fund, Harry Markowitz, a PhD student in economics from Chicago, published "Portfolio Selection" in 1952 in the Journal of Finance. The paper discussed combining different assets to reduce risk without lowering return. The idea was initially overlooked, with Markowitz's advisor, Nobel Prize winner Milton Friedman, even jokingly suggesting the University of Chicago wouldn't award Markowitz a PhD in economics for his topic. A similar article by A.D. Roy, "Safety First and the Holding of Assets," received even less attention. This marked the start of modern portfolio theory, where Markowitz emphasized the importance of considering risk in addition to return and showed that holding many stocks instead of just a few could reduce risk while maintaining expected return.

In the early 1960s, the first theory of asset prices, the Capital Asset Pricing Model (CAPM), emerged. William F. Sharpe, who would later win a Nobel Prize for his work, was the most well-known name associated with the CAPM's development, but other authors including Jan Mossin, Jack Treynor, and John Linter also wrote about asset pricing during this time. The CAPM concluded that all investors should invest in the market portfolio, consisting of all existing securities in proportion to their market capitalization. Investors seeking more or less risk should place part of their wealth in money market or risk-free instruments and the rest in the market portfolio or borrow money at the risk-free rate and invest more in the market portfolio.

The concept of beta (β) was introduced in 1964, which relates the expected return and risk of a security or portfolio to the entire stock market. A stock with a high beta will outperform the market when it does well, but underperform when the market does poorly. The CAPM provided a simple way to understand investment behavior, but there was the issue of stock-specific risk that could alter the relationship between the security and the market. The solution was to hold a group of securities in a portfolio, eliminating company-specific risk and leaving only market-related risk, allowing the investor to have a portfolio of desired risk level with respect to the market and a higher return than any individual stock.

The CAPM theory claimed that stock returns could be predicted based on market risk exposure, but Paul Samuelson's "Proof that Properly Anticipated Prices Fluctuate Randomly" (1965) showed that prices couldn't be forecasted if properly anticipated. Michael Jensen's 1968 study found that actively managed mutual funds underperformed the market, and past performance didn't predict future performance. Eugene Fama defined and found evidence for market efficiency in 1970, with weak form efficiency meaning past prices can't predict future prices, semistrong meaning publicly available information can't forecast stock prices, and strong meaning even private information can't predict stock prices. Fama found extensive evidence for the semistrong and strong forms of market efficiency, but recent evidence suggests deviations from efficiency exist (market anomalies).

The greatest invention in financial theory was the Black-Scholes options pricing model, developed by Fischer Black and Myron Scholes in the 1960s. They based the formula on the Capital Asset Pricing Model (CAPM), but found that the price of an option didn't depend on the expected return of a stock. Robert Merton provided a more elegant derivation of Black-Scholes, which is now widely used to value options. The Arbitrage Theory of Capital Asset Pricing (APT) proposed by Stephen Ross in 1976 was an alternative to the CAPM that allowed for multiple factors instead of one and took into account non-diversifiable risk. In 1992, Eugene Fama and Kenneth French published a three-factor APT model for stock returns that explained 95% of the variability in stock returns (market risk, company size, and book-to-market ratio). Researchers later added a fourth factor, momentum, to the Fama-French model. Today, many academics and practitioners use either a three- or four-factor APT model to explain stock returns.

The growth of QEPM since the 1990s is due to advancements in technology and the development of financial theory. The multifactor model of stock returns is widely used by quantitative managers to forecast returns and manage portfolio risk, and it's becoming a more influential tool in performance measurement. However, financial theory also defines the limits of QEPM's use and raises questions about its effectiveness. For example, if the market is weak-form efficient, QEPM's arbitrage opportunities may be limited. Financial theory provides valuable insights, but investors must understand its implications to make informed decisions.



