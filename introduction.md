# 1) Introduction

There are two primary categories of quantitative equity portfolio management: active and passive. The passive approach, also known as indexing, aims to track a well-known index, such as the S&P 500, and minimize tracking error. In contrast, the active approach aims to outperform a benchmark or provide an absolute return without reference to an index.

Investors can access active or passive portfolios through mutual funds, ETFs, or by constructing their own portfolios. Major equity benchmarks for portfolio managers include [S&P 500](https://en.wikipedia.org/wiki/S%26P_500), [Russell 3000](https://en.wikipedia.org/wiki/Russell_3000_Index), [Wilshire 5000](https://en.wikipedia.org/wiki/Wilshire_5000), [NASDAQ-100](https://en.wikipedia.org/wiki/Nasdaq-100), and MSCI USA.

Qualitative portfolio managers focus on intangible factors and study company fundamentals, while quantitative portfolio managers use mathematical models to predict security returns. Famous qualitative portfolio managers include [Peter Lynch](https://en.wikipedia.org/wiki/Peter_Lynch) and [Warren Buffett](https://en.wikipedia.org/wiki/Warren_Buffett), while quantitative portfolio management is typically associated with large institutions or hedge funds like [Two Sigma](https://www.twosigma.com/), [Citadel](https://www.citadel.com/), and [Schonfeld](https://www.schonfeld.com/).


:::{note}
A qualitative portfolio manager faces challenges in replicating an index portfolio as it can be expensive to purchase all the stocks in the benchmark with the exact weights. Instead, they usually buy a subset of stocks similar to the benchmark, but risk management requires a quantitative risk model. Quantitative tools are essential for indexing, while a quantitative portfolio manager can use these tools to manage risk and replicate an index portfolio more efficiently.
:::

# Fundamentals
Alpha is a crucial measure in quantitative finance used to evaluate the performance of an investment relative to a benchmark index. It represents the excess return of an investment over the benchmark after adjusting for risk, helping investors determine whether the portfolio manager or investment strategy has produced returns through skill or luck.

There are two types of alpha: benchmark alpha and multi-factor alpha. Benchmark alpha measures the return of a portfolio that is not linked to the benchmark's risk, while multi-factor alpha measures the return not linked to multiple factors' risk. The equations for benchmark alpha and multi-factor alpha are: $r_p = α + β_pr_b + ϵ$ and $r_p = α + β\cdot f +ϵ = α + β_1f_1 +...+β_Kf_K +ϵ$, respectively.

In these equations, α is the benchmark or multi-factor alpha, $r_p$ is the portfolio return, $β_p$ is the portfolio beta, $r_b$ is the benchmark return, $f=(f_1,f_2,...,f_K)^T$ is the returns of the K factors, and $β=(β_1,β_2,...,β_K)^T$ is the factor exposures or sensitivities of the portfolio to the K factors.

The key aspect of alpha is the residual return, which represents an increase in return independent of increased benchmark exposure. The residual return is the focus of the quantitative portfolio manager, who aims for high alpha and high information ratio (the excess performance in terms of risk units). The expected or consensus return ($β_pr_b$ or $β\cdot f$) is the part of the portfolio's return related to the benchmark, while the residual return (α + ϵ) represents an increase in return independent of increased direct benchmark exposure. α is the expected value of the residual return, while ϵ is the deviation of the residual return from its mean.

Alpha can be divided into ex-ante (in-sample) and ex-post (out-of-sample) alphas, where ex-ante alpha is the expected alpha, and ex-post alpha is the realized one obtained through regression of portfolio and benchmark returns. The information ratio is the excess performance of a portfolio manager in terms of risk units and is calculated as IR = residual return / residual risk. An active portfolio manager aims for both high ex-post alpha and high ex-post information ratio.

:::{note}
Although the return of the portfolio minus the benchmark return is often used by investors to calculate alpha, this measure is not frequently used in quantitative finance because quantitative managers recognize that when the market is on an upswing, higher returns can be obtained by taking on more risk. Thus, to evaluate a manager's skill in managing a portfolio, it is more relevant to consider risk-adjusted returns. 
:::

# The Market Rules
Investing in financial markets is a complex task that requires a deep understanding of various market rules and principles. The following rules are widely accepted and followed by investors, portfolio managers, and traders around the world. These rules provide a framework for making informed investment decisions and maximizing returns while mitigating risk.

- **Efficiency prevails in markets with profits only possible through taking risk**: This rule states that in markets where investors can only make profits by taking risk, prices reflect all available information and future price movements are unpredictable. The only way to generate returns is to take on greater risk, and therefore profits can only be achieved by making better-informed decisions than others in the market.

- **Risk-free arbitrage does not exist**: The concept of risk-free arbitrage refers to a situation where an investor can take advantage of market inefficiencies to make a profit with zero risk. This is not possible in real-world financial markets, as all investments carry some level of risk.

- **Quantitative analysis seeks profit through statistical arbitrage by using all available information**: Quantitative analysis is a systematic approach to investing that uses mathematical and statistical methods to analyze market data and identify profitable investment opportunities. It seeks to exploit market inefficiencies and generate returns through statistical arbitrage, which is the process of taking advantage of price discrepancies between two or more securities.

- **Quantitative analysis must be based on sound economic theories and reflect persistent patterns**: To be effective, quantitative analysis must be based on sound economic theories and reflect persistent patterns in the data. This means that the investment strategies used must be backed by research and analysis and be able to withstand changing market conditions.

- **Deviations from the benchmark are acceptable only if they come with manageable uncertainty**: Investors often use benchmark portfolios as a reference point for their own investments. Deviations from the benchmark are acceptable only if they are accompanied by manageable levels of uncertainty and the potential for a higher return. This is because investors are willing to take on additional risk if they believe that the reward is worth it.

# Market Efficiencies
Efficiency in financial markets refers to the degree to which prices reflect all available information. There are generally three forms of market efficiency:

- **Weak-form efficiency**: Security prices fully reflect all past market information. Hence, technical analysis is not expected to produce superior stock picks.
- **Semi-strong form efficiency**: Security prices reflect all publicly available information, including macroeconomic fundamentals and analyst reports. Hence, relying solely on publicly available information for stock picking is not likely to be effective.
- **Strong-form efficiency**: Security prices reflect all publicly and privately held information, including inside information. Hence, using any form of privileged information is not expected to result in superior stock selection.
- 
Can we test for market efficiency?

- **Weak-form efficiency**: This can be tested by examining the autocorrelation of stock returns and the presence of momentum and reversal effects.
- **Semi-strong form efficiency**: This can be tested by looking for anomalies such as earnings surprise persistence, the January effect, low P/B and P/E ratios, and neglected firm effects (e.g., small-cap stocks).
- **Strong-form efficiency**: This is challenging to test, but one way is to analyze insider trading transactions, limit order book data, and employee stock grants.

# Market Anomalies
When investigating market anomalies, there are two key steps to follow:

- **Defining "normal" returns**: To determine if a strategy violates market efficiency, it's necessary to define what is considered a "normal" or "expected" return. This can be done by using a benchmark portfolio or a security pricing model, such as the Capital Asset Pricing Model (CAPM).

- **Testing strategy returns**: Historical data can be used to create and test a strategy for excess returns that are statistically significant. For example, creating an equal-weight portfolio of stocks whose analyst ratings improved in the last month and running a regression analysis to determine if it outperforms the benchmark.

When testing for anomalies, it's important to be aware of data limitations and to ensure the data is well-organized. A good understanding of statistics and careful attention to detail are also critical to avoid mistakes in the analysis.

# Documented Market Anomalies
Even though financial markets are largely efficient, some systematic anomalies persist and can lead to profitable investment opportunities. Here are some examples:

- **The value effect** refers to the tendency for stocks with low P/E, P/B, P/S, and P/D ratios to outperform stocks with high ratios over the long term. This anomaly suggests that investors may achieve higher returns by investing in undervalued stocks.
Example: Investing in stocks that have low P/E ratios and high dividend yields.

- **The size effect** refers to the tendency for small-cap stocks to outperform large-cap stocks over time. This anomaly suggests that small companies may offer higher growth potential, but also come with higher risks compared to large established companies.
Example: Investing in small-cap stocks that have solid fundamentals and growth potential.

- **The January effect** refers to the tendency for small-cap and poor-performing stocks to outperform in the month of January. This anomaly may be driven by tax-loss selling at the end of the year and window dressing by fund managers at the start of the new year.
Example: Investing in small-cap stocks that have underperformed in the past and may experience a bounce back in January.

- **The calendar effect** refers to the tendency for specific days of the week or weather events to lead to outperformance. This anomaly may be driven by investor behavior and psychological factors.
Example: Investing in stocks that tend to perform well on Halloween or in response to weather events like hurricanes.

- **The neglected-firm effect** refers to the tendency for stocks with low analyst coverage to have higher risk-adjusted returns compared to stocks with high coverage. This anomaly suggests that stocks with low analyst attention may be overlooked and undervalued, offering potential opportunities for higher returns.
Example: Investing in stocks that are not widely followed by analysts but have solid fundamentals.

- **The PEG ratio effect** refers to the inverse relationship between a stock's PEG ratio and its performance. A low PEG ratio suggests that a stock is undervalued compared to its growth potential, while a high PEG ratio suggests that a stock is overvalued compared to its growth potential. The PEG ratio effect suggests that investing in stocks with low PEG ratios can lead to higher returns.
Example: Investing in stocks that have low PEG ratios and solid growth potential.

- **The IPO effect** refers to the tendency for initial public offerings (IPOs) to underperform on a risk-adjusted basis in the first 3-5 years after going public. This anomaly may be due to several factors, including high underwriter fees, lock-up periods, and a lack of analyst coverage.
Example: Avoiding investing in IPOs in the first few years after they go public.

- **The index-change effect** refers to the tendency for stocks included in an index to have positive returns, while those dropped from an index tend to have negative returns. This anomaly may be driven by passive investing strategies, as investors buy stocks in newly included companies and sell stocks in companies that are dropped from an index.
Example: Investing in stocks that are newly included in an index.

- **The momentum effect** refers to the tendency for stocks that perform well in one period to continue performing well in the next period. This anomaly suggests that investors may achieve higher returns by investing in stocks with high momentum.
Example: Investing in stocks that have shown strong performance over the past few months.

- **The technical indicators effect** refers to the tendency for certain technical indicators to provide excess returns. This anomaly may be driven by investor behavior and technical analysis. However, it's important to note that technical indicators are only one piece of information and should be used in conjunction with other analysis methods for investment decisions.
Example: Using technical indicators like the relative strength







Despite market efficiency, there are systematic anomalies that persist and can be profitable. Some examples include:

- **The value effect** refers to the observation that stocks with low price-to-earnings (P/E), price-to-book (P/B), price-to-sales (P/S), and price-to-dividend (P/D) ratios tend to outperform stocks with high ratios in the long run. This anomaly suggests that investors can potentially achieve higher returns by investing in undervalued stocks.

- **The size effect** refers to the observation that small-cap stocks tend to outperform large-cap stocks over time. This anomaly suggests that small companies may offer higher growth potential, but also come with higher risks compared to large established companies.

- **The January effect** refers to the observation that small-cap and poor-performing stocks tend to outperform in the month of January. This anomaly may be driven by tax-loss selling at the end of the year and window dressing by fund managers at the start of the new year.

- **The calendar effect** refers to the observation of outperformance on specific days of the week, such as Halloween, or in response to weather events. This anomaly may be driven by investor behavior and psychological factors.

- **The neglected-firm effect** refers to the observation that stocks with low analyst coverage tend to have higher risk-adjusted returns compared to stocks with high analyst coverage. This anomaly suggests that stocks with low analyst attention may be overlooked and undervalued, offering potential opportunities for higher returns.

- **The PEG ratio effect** refers to the inverse relationship between a stock's price-to-earnings-to-growth (PEG) ratio and its performance. A low PEG ratio suggests that a stock is undervalued compared to its growth potential, while a high PEG ratio suggests that a stock is overvalued compared to its growth potential. The PEG ratio effect suggests that investing in stocks with low PEG ratios can lead to higher returns.

- **The IPO effect** refers to the observation that initial public offerings (IPOs) underperform on a risk-adjusted basis in the first 3-5 years after going public. This anomaly may be due to several factors, including high underwriter fees, lock-up periods, and a lack of analyst coverage.

- **The index-change effect** refers to the observation that stocks included in an index tend to have positive returns, while those dropped from an index tend to have negative returns. This anomaly may be driven by passive investing strategies, as investors buy stocks in newly included companies and sell stocks in companies that are dropped from an index.

- **The momentum effect** refers to the observation that stocks that perform well in one period tend to continue performing well in the next period. This anomaly suggests that investors may achieve higher returns by investing in stocks with high momentum.

- **The technical indicators effect** refers to the observation that certain technical indicators, such as volume, relative strength index (RSI), Bollinger Bands, and moving average, provide excess returns. This anomaly may be driven by investor behavior and technical analysis. However, it's important to note that technical indicators are only one piece of information and should be used in conjunction with other analysis methods for investment decisions.

- **The Analyst Forecasts Effect** refers to the observation that stocks with "buy" ratings from analysts tend to outperform, though this effect has weakened over time. Changes in analyst ratings and earnings surprises also tend to predict stock returns. This anomaly may be driven by the collective actions of investors following analyst recommendations, as well as by the potential for analyst conflicts of interest.

- **Insider Trading Effect** refers to the observation that recent insider-bought stocks tend to have excess returns, while recent insider-sold stocks tend to have negative returns. The actions of corporate insiders, who have access to information not available to the general public, can drive this effect.

- **Overreaction Effect** refers to the observation that investors tend to overreact to both good and bad news. Specifically, stocks that have underperformed in the past tend to outperform over the next 3-5 years. This anomaly may be driven by investor overconfidence, overreaction to news events, and behavioral biases.

- **Stock Buybacks Effect** refers to the observation that companies that buy back their own stock tend to have positive risk-adjusted returns. This effect may be driven by the belief that stock buybacks indicate a company's confidence in its own prospects or by the impact of buybacks on earnings per share.

- **Stock Splits and Reverse Splits Effect** refers to the observation that stock splits are followed by positive returns. Investor perceptions that stock splits signal a company's financial health and growth prospects may drive this effect.

- **Spin-offs Effect*** refers to the observation that parent companies tend to have excess returns after the spin-off of a subsidiary. This effect may be driven by increased focus on the operations of the subsidiary and improved management efficiency at the parent company.

- **Accruals Effect** refers to the observation that low accrual companies tend to perform better than high accrual companies. Accruals refer to the amount of non-cash expenses recorded in a company's financial statements. Low accrual companies are generally considered to be of higher quality than high accrual companies.

- **Low Volatility Effect** refers to the observation that low historical volatility stocks tend to outperform high volatility stocks. This effect may be driven by the tendency of investors to avoid stocks with high volatility, as well as by the belief that low volatility stocks are less risky.

- **Low Beta Effect** refers to the observation that low beta stocks tend to outperform high beta stocks on a risk-adjusted basis. Beta is a measure of a stock's volatility relative to the overall market. Low beta stocks are generally considered to be less risky than high beta stocks.

- **Liquidity Effect** refers to the observation that less liquid stocks tend to have higher returns than more liquid stocks. This effect may be driven by the tendency of investors to demand a higher return for investing in less liquid stocks, as well as by the difficulty of trading in and out of less liquid stocks.

- **Crowding Effect** refers to the observation that stocks invested in by many money managers tend to underperform less invested-in stocks. The difficulty of selling positions in crowded stocks, as well as the tendency of managers to follow similar investment strategies leading to reduced diversification, may drive this effect. Crowding can be measured using holdings-based and return-based measures of saturation by money managers.

:::{note}
The P/B anomaly, P/E anomaly, size anomaly, and January effect are most susceptible to data mining or data snooping. While there have been several studies on the P/B and size anomalies since the original work by Fama and others, the P/E anomaly and January effect have also been well-documented. Nearly every quantitative portfolio manager and academic is aware of these factors either through their own testing or reading about them.
:::

# Behavioral Anomalies 

Behavioral finance is a branch of finance that considers psychological and behavioral factors in investment decisions, leading to outcomes that differ from those predicted by rational decision-making theories. It recognizes profitable opportunities from investors' behavior.

Documented anomalies:

- **Anchoring**: Investors tend to rely too heavily on a single piece of information or reference point when making investment decisions, leading to a bias in their assessments. For example, an investor may be anchored to a specific price point for a stock and may continue to hold the stock even if the price deviates from their expectations, resulting in a loss.

- **Ambiguity aversion**: Investors tend to avoid stocks or investments that are unfamiliar to them and have a preference for familiar investments, even if they are not necessarily the best choice. For example, an investor may choose to invest in a well-known brand name rather than a lesser-known company with stronger financials.

- **Availability bias**: Investors tend to overestimate the likelihood of future events based on memories that are easily accessible to them, such as recent events or information that is top of mind. This can result in an overestimation of risks and opportunities, leading to poor investment decisions. For example, an investor may overestimate the potential risks of a certain stock based on recent news articles, leading them to avoid investing in the stock.

- **Confirmation bias**: Investors tend to give more weight to information that confirms their beliefs or expectations, and less weight to information that contradicts them. This can lead to a failure to consider new information and an unwillingness to adapt to changing circumstances. For example, an investor may choose to hold on to a stock that is underperforming despite evidence indicating that it is unlikely to recover.

- **Disposition effect**: Investors tend to hold on to losing investments for too long, and sell winning investments too soon. This is often due to a belief that the losing investment will eventually recover, or that the winner has reached its peak. For example, an investor may continue to hold on to a stock that has significantly decreased in value, hoping that it will recover in the future.

- **Endowment effect**: Investors tend to demand more to give up an investment than they are willing to pay to acquire it. This can result in suboptimal decisions, as they may hold on to underperforming investments or sell winning investments too early. For example, an investor may hold on to a stock that has lost significant value because they believe that it will eventually recover, even if the odds are against it.

- **Escalation bias**: Investors tend to compound losses by putting more money into a losing investment, rather than cutting their losses and moving on. This is often due to a belief that the investment will eventually recover, or a failure to admit to a bad decision. For example, an investor may continue to invest in a stock that has lost significant value, hoping that the investment will eventually recover.

- **Framing effect**: Investors may be influenced by the way information is presented to them, such as whether it is presented in a positive or negative light. This can result in suboptimal decisions, as investors may be swayed by the framing of the information rather than the underlying facts.

- **Herding mentality**: Investors tend to follow the actions of others, even in investing. This can result in poor investment decisions, as investors may not be considering the reasons behind the actions of others. For example, an investor may choose to invest in a stock solely because it is popular among other investors, without considering the underlying financials of the company.

- **Illusion of knowledge**: Investors may have an overreliance on data and analysis when evaluating stocks, leading to an over-confidence in their abilities. This can result in frequent trading, high transaction costs, and poor investment decisions. For example, an investor may believe that they have a deep understanding of a certain industry and may invest heavily in stocks within that industry without considering other factors.

- **Loss aversion**: Investors tend to feel the pain of losses more acutely than the pleasure of gains, leading to a preference for avoiding losses over seeking gains. This can result in a reluctance to take risks and a failure to fully realize potential gains.

- **Narrow framing**: Investors may focus too narrowly on individual investments, failing to consider them in the context of their overall portfolio or broader market trends. This can lead to suboptimal decisions, such as failing to diversify sufficiently, taking on excessive risk, or missing out on opportunities that would have been apparent with a broader perspective.

- **Overconfidence**: Investors may overestimate their ability to predict market movements or choose winning investments, leading to overconfidence in their investment decisions. This can result in frequent trading and high transaction costs, as well as poor investment outcomes due to acting on emotions rather than rational analysis. Overconfidence can also lead to a failure to adequately consider risk, diversification, or the possibility of unforeseen events that can disrupt even the best-laid investment plans.

- **Recency bias**: Investors tend to give more weight to recent events when making investment decisions, and may neglect to consider longer-term trends or historical data. This can result in suboptimal decisions and a failure to properly diversify portfolios.

-- **Sunk cost fallacy**: Investors tend to factor in past investments and costs when making decisions about future investments, even if these costs are irrelevant to the current decision. This can result in a reluctance to sell losing investments or a failure to invest in potentially profitable opportunities.

Examples of behavioral anomalies include the "dot-com bubble" of the late 1990s, where investors became overconfident in the growth prospects of technology stocks and failed to consider their underlying valuations. Another example is the 2008 financial crisis, where many investors were anchored to past market trends and failed to anticipate the risks posed by complex financial instruments. The recent GameStop frenzy, where investors piled into the stock to drive up prices, is another example of herding mentality and narrow framing.

# Why is market efficiency imperfect?

- **Information asymmetry**: Corporate insiders have access to information not available to the general public, which they can use to trade stocks profitably. For example, if an insider knows that a company will soon announce positive earnings results, they may buy the company's stock before the announcement to benefit from the subsequent price increase.

- **Slow information diffusion**: A company may announce a positive earnings surprise, but it may take time for the news to spread throughout the market. During this lag period, some investors may be able to exploit the mispricing by buying the stock before the price adjusts.

- **Limited capacity**: Small investors may not have the resources or expertise to analyze a large number of stocks effectively. This can lead to mispricings in less-followed stocks, which may create opportunities for informed investors.

- **Private information**: Hedge fund managers may obtain information through extensive research or expert networks that is not publicly available. This can give them an advantage over other investors and lead to market inefficiencies as they trade on their knowledge.

- **Emotional decisions**: Investors may overreact to news events, leading to short-term price swings that do not reflect the true underlying value of the stock. For example, panic selling during a market downturn can cause stocks to be undervalued, while euphoria during a market rally can cause stocks to be overvalued.

- **Market manipulation**: Large traders or institutional investors may manipulate the market to exploit other investors' irrational behavior. For example, a hedge fund manager may spread false rumors about a company to drive down its stock price before buying the stock at a lower price.

- **Technological change**: The rise of algorithmic trading has increased the speed and complexity of trading, leading to new types of market inefficiencies. For example, algorithmic traders may use high-frequency trading strategies to take advantage of momentary mispricings in the market.

- **Transactions costs**: The bid-ask spread, which is the difference between the highest price a buyer is willing to pay for a stock and the lowest price a seller is willing to accept, can create inefficiencies in real-world markets. This is because investors may be reluctant to trade if the spread is too wide, leading to less efficient price discovery.

- **Taxation**: Taxation policies can create market inefficiencies by influencing investors' decisions. For example, if there is a tax on capital gains, investors may be less likely to sell their winning stocks, leading to a mispricing between taxed and untaxed markets.

- **Government regulations**: Regulations aimed at preventing market manipulation or insider trading may increase transactions costs and reduce the flow of information to market participants. This can lead to market inefficiencies as investors may be unable to trade on the best available information.

# Brief history of financial theory

The modern financial theory has a history of over 100 years, starting from Bachelier's work in 1900 to today's portfolio risk measurement. The growth of quantitative equity portfolio management was accelerated by technological and theoretical advances in the late 20th century, but it's based on a vast literature of modern portfolio theory. Despite being widely used, many practitioners may not be aware of its origin. Here's a brief overview of the progress in investment philosophy. Knowledge of modern portfolio theory is valuable for both practitioners and students of finance, even if they later question its parts.

Louis Bachelier, a French mathematician, wrote "The Theory of Speculation" in 1900 and laid the foundation for dynamic security pricing. He showed that prices fluctuate randomly, making predictions impossible. In the 1930s, Alfred Cowles III found no evidence of professionals' ability to outperform the market after examining thousands of stock selections. This supports the notion that trying to predict the market was no better than flipping a coin.

In 1949, Benjamin Graham published "The Intelligent Investor" and introduced value investing. He believed that investors could pick stocks and beat the market by following certain rules, and his student, Warren Buffett, was successful in outperforming the S&P 500 Index. The concept of security analysis still exists today, although it was more prevalent in the past. John Maynard Keynes also managed the Cambridge Trust fund with a small portfolio of stocks he knew, reflecting the world of investing before modern portfolio theory.

Before Warren Buffett started his first investment fund, Harry Markowitz, a PhD student in economics from Chicago, published "Portfolio Selection" in 1952 in the Journal of Finance. The paper discussed combining different assets to reduce risk without lowering return. The idea was initially overlooked, with Markowitz's advisor, Nobel Prize winner Milton Friedman, even jokingly suggesting the University of Chicago wouldn't award Markowitz a PhD in economics for his topic. A similar article by A.D. Roy, "Safety First and the Holding of Assets," received even less attention. This marked the start of modern portfolio theory, where Markowitz emphasized the importance of considering risk in addition to return and showed that holding many stocks instead of just a few could reduce risk while maintaining expected return.

In the early 1960s, the first theory of asset prices, the Capital Asset Pricing Model (CAPM), emerged. William F. Sharpe, who would later win a Nobel Prize for his work, was the most well-known name associated with the CAPM's development, but other authors including Jan Mossin, Jack Treynor, and John Linter also wrote about asset pricing during this time. The CAPM concluded that all investors should invest in the market portfolio, consisting of all existing securities in proportion to their market capitalization. Investors seeking more or less risk should place part of their wealth in money market or risk-free instruments and the rest in the market portfolio or borrow money at the risk-free rate and invest more in the market portfolio.

The concept of beta (β) was introduced in 1964, which relates the expected return and risk of a security or portfolio to the entire stock market. A stock with a high beta will outperform the market when it does well, but underperform when the market does poorly. The CAPM provided a simple way to understand investment behavior, but there was the issue of stock-specific risk that could alter the relationship between the security and the market. The solution was to hold a group of securities in a portfolio, eliminating company-specific risk and leaving only market-related risk, allowing the investor to have a portfolio of desired risk level with respect to the market and a higher return than any individual stock.

The CAPM theory claimed that stock returns could be predicted based on market risk exposure, but Paul Samuelson's "Proof that Properly Anticipated Prices Fluctuate Randomly" (1965) showed that prices couldn't be forecasted if properly anticipated. Michael Jensen's 1968 study found that actively managed mutual funds underperformed the market, and past performance didn't predict future performance. Eugene Fama defined and found evidence for market efficiency in 1970, with weak form efficiency meaning past prices can't predict future prices, semistrong meaning publicly available information can't forecast stock prices, and strong meaning even private information can't predict stock prices. Fama found extensive evidence for the semistrong and strong forms of market efficiency, but recent evidence suggests deviations from efficiency exist (market anomalies).

The greatest invention in financial theory was the Black-Scholes options pricing model, developed by Fischer Black and Myron Scholes in the 1960s. They based the formula on the Capital Asset Pricing Model (CAPM), but found that the price of an option didn't depend on the expected return of a stock. Robert Merton provided a more elegant derivation of Black-Scholes, which is now widely used to value options. The Arbitrage Theory of Capital Asset Pricing (APT) proposed by Stephen Ross in 1976 was an alternative to the CAPM that allowed for multiple factors instead of one and took into account non-diversifiable risk. In 1992, Eugene Fama and Kenneth French published a three-factor APT model for stock returns that explained 95% of the variability in stock returns (market risk, company size, and book-to-market ratio). Researchers later added a fourth factor, momentum, to the Fama-French model. Today, many academics and practitioners use either a three- or four-factor APT model to explain stock returns.

The growth of financial quantitative research since the 1990s is due to advancements in technology and the development of financial theory. The multifactor model of stock returns is widely used by quantitative managers to forecast returns and manage portfolio risk, and it's becoming a more influential tool in performance measurement. However, financial theory also defines the limits of quantitative research's use and raises questions about its effectiveness. For example, if the market is weak-form efficient, quantitative research's arbitrage opportunities may be limited. Financial theory provides valuable insights, but investors must understand its implications to make informed decisions.
