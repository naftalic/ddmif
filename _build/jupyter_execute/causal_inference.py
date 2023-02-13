#!/usr/bin/env python
# coding: utf-8

# One result that will be very useful throughout this section is:
# 
# \begin{align}
#   \sum_{i=1}^n(x_i-\overline{x})^2 & =                                                                                               
#   \sum_{i=1}^n (x_i^2-2x_i\overline{x}+\overline{x}^2)
#   \\
#   & = \sum x_i^2 - 2\overline{x} \sum x_i +n\overline{x}^2                                          \\
#   & = \sum x_i^2 - 2 \dfrac{1}{n} \sum x_i \sum x_i +n\overline{x}^2                                \\
#   & = \sum x_i^2 +n\overline{x}^2 - \dfrac{2}{n} \bigg (\sum x_i \bigg )^2                          \\
#   & = \sum x_i^2+n\bigg (\dfrac{1}{n} \sum x_i \bigg)^2 - 2n \bigg (\dfrac{1}{n} \sum x_i \bigg )^2 \\
#   & = \sum x_i^2 - n \bigg (\dfrac{1}{n} \sum x_i \bigg )^2                                         \\
#   & = \sum x_i^2 - n \overline{x}^2                                                                 
# \end{align}
# 
# A more general version of this result is:
# 
# \begin{align}
#    \sum_{i=1}^n(x_i-\overline{x})(y_i-\overline{y}) & = \sum_{i=1}^n x_i(y_i - \overline{y}) \\
#     & = \sum_{i=1}^n (x_i - \overline{x})y_i \\
#     & = \sum_{i=1}^n x_iy_i - n(\overline{xy}) \\
# \end{align}
