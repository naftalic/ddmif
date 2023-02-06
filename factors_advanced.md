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

The central concept of modern financial economics is that the average return of a stock represents the reward for taking on risk. 
In a factor model, the factor exposure, represented by the vector $\beta_i = (\beta_{i,1},...,\beta_{i,K})$, 
represents the exposure of a stock to some kind of risk. The factor premium, represented by the vector $f = (f_1,...,f_K)$, 
quantifies the payoff to an investor who takes on that risk by buying the stock. 
The average stock return therefore equals the product of the factor exposure and the factor premium:

$r_i = \beta_i^T f + \alpha + \epsilon_i$

where $\alpha$ is the constant term and $\epsilon_i$ is the error term (i.e., the part of the stock return that does not depend
on the K factors). Note that the average of $\epsilon_i$ is zero.

In a factor model, a stock's factor exposure is a measure of its exposure to a specific type of risk, 
while the factor premium quantifies the reward to an investor who takes on that risk by buying the stock. 
The average stock return is the product of the factor exposure and the factor premium, which can be calculated using the following formula:



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

