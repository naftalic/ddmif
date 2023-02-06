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

# The fundamental factor model

In financial economics, the average return of a stock is believed to be the reward for taking on risk. In a factor model, the risk exposure of a stock is represented by its factor exposure vector $\beta_i = (\beta_{i,1},...,\beta_{i,K})$. The factor premium vector $f = (f_1,...,f_K)$ represents the reward to an investor who takes on the risk by buying the stock.

The return on stock i can be expressed as:

$r_i = \alpha + β_1f_1 + β_2f_2 + ... + β_Kf_K + \epsilon_i = \alpha + \beta_i^T f + \epsilon_i$

where $\alpha$ is the constant term, $\beta_i$ and $f$ are the vector notations for the factor exposure and premium, and $\epsilon_i$ is the error term, representing the part of the stock return that does not depend on the K factors.

The fundamental factor model assumes that a stock's factor exposure, which is a measure of its exposure to a specific type of risk, can be represented by an observable characteristic such as market capitalization or book-to-market ratio. However, the factor premium, which represents the reward for taking on that risk, must be estimated through observation of the relationship between the average stock return and the factor exposure.

## The average stock return 

Using the assumption that the average $\epsilon_i$ is zero, we calculate the average stock return as

$$E(r_i) = E(\alpha) + E(β_if)+E(\epsilon_i)=\alpha + β_iE(f)$$

as $\alpha$, and $β_i$ are constants and $E(\epsilon_i)=0$. Hence, the average stock return is simply the product of the factor exposure and the factor premium.

The average stock return is the payoff for taking risk—but what is this risk exactly? The risk of a stock has two components, diversifiable risk and nondiversifiable risk.

Total risk  = Nondiversifiable risk + Diversifiable risk

Since investors can eliminate diversifiable risk from their portfolios through diversification, the market only rewards exposure to nondiversifiable risk. Thus we may restate the central idea of modern financial economics as: 

The average stock return is the payoff for taking nondiversifiable risk.

The nondiversifiable risk can be expressed as the product of the factor exposure squared and the risk included in one unit of exposure. We will call the risk of one unit of exposure the factor risk. Then we may write

Nondiversifiable risk = factor exposure^2 x factor risk

Within the framework of the fundamental factor model, the total risk of a stock (nondiversifiable risk plus diversifiable risk) can be measured by the variance:

$$
V(r_i) &= V( \alpha + β_1f_1 + β_2f_2 + ... + β_Kf_K + \epsilon_i)\\
&= V( \alpha) + V(β_1f_1 + β_2f_2 + ... + β_Kf_K) + V(\epsilon_i)\\
&= V(β_1f_1 + β_2f_2 + ... + β_Kf_K)
$$

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

