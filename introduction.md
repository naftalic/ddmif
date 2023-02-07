# Introduction

There are two major categories of quantitative equity portfolio management: active and passive. Passive approach, also known as indexing, aims to track a well-known index, such as the S&P 500, and minimize the tracking error. Active approach aims to outperform a benchmark or provide an absolute return without any reference to an index.

Investors can access active or passive portfolios through mutual funds, ETFs, or building their own portfolios. Major equity benchmarks for portfolio managers include [S&P 500](https://en.wikipedia.org/wiki/S%26P_500), [Russell 3000](https://en.wikipedia.org/wiki/Russell_3000_Index), [Wilshire 5000](https://en.wikipedia.org/wiki/Wilshire_5000), [NASDAQ-100](https://en.wikipedia.org/wiki/Nasdaq-100), and MSCI USA.

Qualitative portfolio managers focus on intangibles and study company fundamentals, while quantitative portfolio managers use mathematical models to predict security returns. Famous qualitative portfolio managers include [Peter Lynch](https://en.wikipedia.org/wiki/Peter_Lynch) and [Warren Buffett](https://en.wikipedia.org/wiki/Warren_Buffett). Quantitative portfolio management is usually associated with large institutions or hedge funds, such as [Two Sigma](https://www.twosigma.com/), [Citadel](https://www.citadel.com/), and [Schonfeld](https://www.schonfeld.com/).


# Fundamentals
[Alpha](https://en.wikipedia.org/wiki/Alpha_(finance)) is a key measure in quantitative finance used to evaluate the performance of an investment relative to a benchmark index. It represents the excess return of an investment over the benchmark after adjusting for risk. Alpha helps investors determine if the portfolio manager or investment strategy has produced returns through skill or luck.

There are two types of Alpha: Benchmark Alpha and Multi-Factor Alpha. Benchmark Alpha measures the return of a portfolio not linked to the benchmark's risk, while Multi-Factor Alpha measures the return not linked to multiple factors' risk. The equations for Benchmark Alpha and Multi-Factor Alpha are: $r_p = α + β_pr_b + ϵ$ and $r_p = α + β_1f_1 +...+β_kf_k +ϵ = α + β\cdot f +ϵ$ respectively.

In these equations, α is the benchmark or multi-factor alpha, $r_p$ is the return of the portfolio, $β_p$ is the beta of the portfolio, $r_b$ is the return of the benchmark, $f=(f_1,f_2,...,f_k)^T$ is the returns of the K factors, and $β=(β_1,β_2,...,β_k)^T$ is the factor exposures or sensitivities of the portfolio to the K factors.

The important aspect of Alpha is the residual return, which represents an increase in return independent of increased benchmark exposure. The residual return is the focus of the quantitative portfolio manager, who aims for high Alpha and high Information Ratio (the excess performance in terms of risk units). The expected or consensus return ($βr_b$ or $β\cdot f$) is the part of the portfolio's return related to the benchmark, while the residual return ($α + ϵ$) represents an increase in return independent of increased direct benchmark exposure. $α$ is the expected value of the residual return, while $ϵ$ is the deviation of the residual return from its mean.

Alpha can be divided into Ex-ante (in-sample) and Ex-Post (out-of-sample) alphas, where Ex-ante Alpha is the expected alpha and Ex-post Alpha is the realized one obtained through regression of portfolio and benchmark returns. The Information Ratio is the excess performance of a portfolio manager in terms of risk units and is calculated as IR = residual return / residual risk. An active portfolio manager aims for both high Ex-Post alpha and high Ex-Post Information Ratio.

# The Market Rules
Investing in financial markets is a complex and challenging task that requires a deep understanding of various market rules and principles. The market rules, as stated here, are widely accepted and followed by investors, portfolio managers, and traders around the world. These rules help provide a framework for making informed investment decisions and maximizing returns while mitigating risk. 

- **Efficiency prevails in markets with profits only possible through taking risk**: This rule states that in markets where investors can only make profits by taking risk, prices reflect all available information and future price movements are unpredictable. The only way to generate returns is to take on greater risk, and therefore profits can only be achieved by making better-informed decisions than others in the market.

- **Risk-free arbitrage does not exist**: The concept of risk-free arbitrage refers to a situation where an investor can take advantage of market inefficiencies to make a profit with zero risk. This is not possible in real-world financial markets, as all investments carry some level of risk.

- **Quantitative Analysis seeks profit through statistical arbitrage by using all available information**: Quantitative analysis is a systematic approach to investing that uses mathematical and statistical methods to analyze market data and identify profitable investment opportunities. It seeks to exploit market inefficiencies and generate returns through statistical arbitrage, which is the process of taking advantage of price discrepancies between two or more securities.

- **Quantitative Analysis must be based on solid economic theories and reflect persistent patterns**: To be effective, quantitative analysis must be based on solid economic theories and reflect persistent patterns in the data. This means that the investment strategies used must be backed by research and analysis and be able to withstand changing market conditions.

- **Deviations from the benchmark are acceptable only if they come with manageable uncertainty**: Investors often use benchmark portfolios as a reference point for their own investments. Deviations from the benchmark are acceptable only if they are accompanied by manageable levels of uncertainty and the potential for a higher return. This is because investors are willing to take on additional risk if they believe that the reward is worth it.

# Market Efficiencies

We generaly distingish between three forms of market efficiencies:

- **Weak form** - security prices fully reflect all past market information. Hence, technical analysis is not expected to produce superior stock picks.
- **Semi-strong form** - security prices reflect all publicly available information, including macroeconomic fundamentals and analyst reports. Hence, relying on publicly available information for stock picking is not likely to be effective.
- **Strong form** - security prices reflect all publicly and privately held information, including inside information. Hence, using any form of privileged information is not expected to result in superior stock selection.

Can we test for market efficiency?

- **Weak-form efficiency**: This can be tested by examining the autocorrelation of stock returns and the presence of momentum and reversal effects.
- **Semi-strong form efficiency**: This can be tested by looking for anomalies such as earnings surprise persistence, January effect, low P/B, P/E ratios, and neglected firm effects (e.g. small cap stocks).
- **Strong form efficiency**: This is challenging to test, but one way is to analyze insider trading transactions, limit order book data, and employee stock grants.

# Market Anomalies

- **Defining "normal" returns**: To determine if a strategy violates market efficiency, it's necessary to define what is considered a "normal" or "expected" return. This can be done by using a zero-investment portfolio or a security pricing model (e.g. CAPM).

- **Testing strategy returns**: Using historical data, a strategy can be created and tested for excess returns that are statistically significant. For example, creating an equal-weight portfolio of stocks whose analyst ratings improved in the last month and running a regression analysis.

When testing for anomalies, it's important to be aware of data limitations and to ensure good organization of the data. A good knowledge of statistics and attention to detail is also critical to avoid mistakes in the analysis.

# Documented Market Anomalies

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
The Analyst Forecasts Effect refers to the observation that stocks with "buy" ratings from analysts tend to outperform, though this effect has weakened over time. Changes in analyst ratings and earnings surprises also tend to predict stock returns. This anomaly may be driven by the collective actions of investors following analyst recommendations, as well as by the potential for analyst conflicts of interest.

- **The insider trading effect** refers to the observation that recent insider-bought stocks tend to have excess returns, while recent insider-sold stocks tend to have negative returns. This anomaly may be driven by the actions of corporate insiders who have access to information not available to the general public.

- **The overreaction effect** refers to the observation that investors tend to overreact to both good and bad news. In particular, stocks that have underperformed in the past tend to outperform over the next 3-5 years. This anomaly may be driven by investor overconfidence, overreaction to news events, and behavioral biases.

- **The stock buybacks effect** refers to the observation that companies that buy back their own stock tend to have positive risk-adjusted returns. This anomaly may be driven by the belief that stock buybacks indicate a company's confidence in its own prospects, or by the impact of buybacks on earnings per share.

- **The stock splits and reverse splits effect** refers to the observation that stock splits are followed by positive returns. This anomaly may be driven by investor perceptions that stock splits signal a company's financial health and growth prospects.

- **The spin-offs effect** refers to the observation that parent companies tend to have excess returns after the spin-off of a subsidiary. This anomaly may be driven by increased focus on the operations of the subsidiary and improved management efficiency at the parent company.

- **The accruals effect** refers to the observation that low accrual companies tend to perform better than high accrual companies. Accruals refer to the amount of non-cash expenses recorded in a company's financial statements, and low accrual companies are generally considered to be of higher quality than high accrual companies.

- **The low volatility effect** refers to the observation that low historical volatility stocks tend to outperform high volatility stocks. This anomaly may be driven by the tendency of investors to avoid stocks with high volatility, as well as by the belief that low volatility stocks are less risky.

- **The low beta effect** refers to the observation that low beta stocks tend to outperform high beta stocks on a risk-adjusted basis. Beta is a measure of a stock's volatility relative to the overall market, and low beta stocks are generally considered to be less risky than high beta stocks.

- **The liquidity effect** refers to the observation that less liquid stocks tend to have higher returns than more liquid stocks. This anomaly may be driven by the tendency of investors to demand a higher return for investing in less liquid stocks, as well as by the difficulty of trading in and out of less liquid stocks.

- **The crowding effect** refers to the observation that stocks invested in by many money managers tend to underperform less invested-in stocks. This anomaly may be driven by the difficulty of selling positions in crowded stocks, as well as by the tendency of managers to follow similar investment strategies, leading to reduced diversification. Crowding can be measured using holdings-based and return-based measures of saturation by money managers.

# Behavioral Anomalies 

Behavioral finance is a branch of finance that considers psychological and behavioral factors in investment decisions, leading to outcomes that differ from those predicted by rational decision-making theories. It recognizes profitable opportunities from investors' behavior.

Documented anomalies:

- **Anchoring**: Investors tend to rely too heavily on a single piece of information or reference point when making investment decisions, leading to a bias in their assessments. This often results in a lack of flexibility in decision making, as investors may be anchored to certain expectations or past market experiences.

- **Ambiguity aversion**: Investors tend to avoid stocks or investments that are unfamiliar to them and have a preference for familiar investments, even if they are not necessarily the best choice. This is because they are more comfortable with what they know, even if it is not the most rational choice.

- **Availability bias**: Investors tend to over-estimate the likelihood of future events based on memories that are easily accessible to them, such as recent events or information that is top of mind. This can result in an overestimation of risks and opportunities, leading to poor investment decisions.

- **Confirmation bias**: Investors tend to give more weight to information that confirms their beliefs or expectations, and less weight to information that contradicts them. This can lead to a failure to consider new information and an unwillingness to adapt to changing circumstances.

- **Disposition effect**: Investors tend to hold on to losing investments for too long, and sell winning investments too soon. This is often due to a belief that the losing investment will eventually recover, or that the winner has reached its peak.

- **Endowment effect**: Investors tend to demand more to give up an investment than they are willing to pay to acquire it. This can result in suboptimal decisions, as they may hold on to underperforming investments or sell winning investments too early.

- **Escalation bias**: Investors tend to compound losses by putting more money into a losing investment, rather than cutting their losses and moving on. This is often due to a belief that the investment will eventually recover, or a failure to admit to a bad decision.

- **Herding mentality**: Investors tend to follow the actions of others, even in investing. This can result in poor investment decisions, as investors may not be considering the reasons behind the actions of others.

- **Illusion of knowledge**: Investors may have an overreliance on data and analysis when evaluating stocks, leading to an over-confidence in their abilities. This can result in frequent trading, high transaction costs, and poor investment decisions.

- **Narrow framing**: Investors may consider investments in isolation, rather than considering them in the context of a portfolio or broader market trends. This can result in suboptimal decisions and a failure to consider risk and diversification.

- **Overconfidence**: Investors may overestimate their abilities and have an over-confidence in their investment decisions, leading to frequent trades and high transaction costs. This can result in poor investment outcomes, as they may be acting on emotions rather than rational analysis.


# Why is market efficiency imperfect?

- **Information asymmetry**: Information is not equally accessible to all market participants. Some investors have more resources or expertise to obtain or analyze information. This can lead to a difference in opinion and cause market inefficiencies.

- **Slow information diffusion**: The process of information spreading across the market can be slow, and prices may not immediately reflect new information. This creates opportunities for some investors to act faster and exploit the lag.

- **Limited capacity**: Not all investors have the ability to process large amounts of information, and some may not have the skills to interpret the data correctly. This can lead to mispricings that create opportunities for informed investors.

- **Private information**: Information filtering and interpretation can create private information, giving some investors an advantage over others. This can lead to market inefficiencies as private information holders trade on their knowledge.

- **Emotional decisions**: Investors' emotions can influence their investment decisions, leading to market inefficiencies. For example, overreaction to news events, overconfidence, and herding mentality are emotional biases that can cause prices to deviate from fair value.

- **Market manipulation**: Efforts to exploit irrational behavior can create market inefficiencies. For example, insider trading or market manipulation by large traders can cause prices to deviate from their fair value.

- **Technological change**: Technological advancements, shifts in consumer preferences, and changes in economic conditions can impact market performance and create inefficiencies.

- **Transactions costs**: In real-world markets, transactions costs, such as bid-ask spreads, can diverge from economic models, affecting market performance and creating inefficiencies.

- **Taxation**: Taxation policies can affect market performance and create inefficiencies. For example, taxes on capital gains can impact the decisions of investors and create price differences between taxed and untaxed markets.

- **Government regulations**: Government regulations, such as market manipulation laws, can create deviations from ideal economic models. For example, regulations can reduce the information available to market participants and increase transactions costs, leading to market inefficiencies.


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
