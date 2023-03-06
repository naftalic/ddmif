#!/usr/bin/env python
# coding: utf-8

# # 8) Quadratic Programming
# 
# The general quadratic programming problem can be expressed as minimizing the function 
# 
# $$
# \min\limits_w 0.5 w^\top \Sigma w + w^\top c \quad\text{s.t.}\quad Aw\le b
# $$ 
# 
# where $w$ is the vector of unknowns, $\Sigma$ is a symmetric positive semidefinite matrix supplying coefficients on the quadratic terms, $c$ is a vector of coefficients related to the linear objective function, $A$ is a matrix of coefficients for the constraints, and $b$ is a vector of constraint values.
# 
# This general quadratic optimization problem works for both quadratic and linear optimization problems. For linear optimization problems, $\Sigma$ can be set to 0, and the problem becomes a linear programming problem. In contrast, for quadratic optimizations, the appropriate $\Sigma$ is used.
# 
# Let's examine two special cases of the general quadratic optimization program. One case only involves equality constraints, while the other case includes both inequality and equality constraints. We separate these into two categories because with equality constraints, we can solve for the optimal weights using a closed-form solution. Although the objective function and constraints are abstract mathematical concepts in the general optimization problem, they become more meaningful when applied to real-world problems. In the next section of this appendix, we will demonstrate this.
# 
# ## Quadraric programming with equality constraints
# In the case of quadratic optimization problems with only equality constraints, a closed-form solution can be obtained. Specifically, the problem can be formulated as follows:
# 
# $$
# \min\limits_x 0.5 w^\top \Sigma w + w^\top c \quad\text{s.t.}\quad Aw= b
# $$ 
# 
# Given that matrix $A$ is of full rank and matrix $\Sigma$ is positive definite, a unique solution for $w$ exists. By unique solution, we refer to a set of values for $w$ that yields the minimum value of our objective function. 
# 
# :::{note}
# A matrix $A$ is said to be of full rank if its rows or columns are linearly independent. In other words, there are no redundant rows or columns that can be expressed as linear combinations of other rows or columns. This implies that the matrix has the maximum possible number of linearly independent rows or columns, which is equal to the minimum of the number of rows or columns of the matrix.
# A matrix of full rank has an inverse, and it is invertible. Additionally, the determinant of a matrix of full rank is non-zero.
# 
# A matrix $\Sigma$ is positive definite if it satisfies the following two conditions:
# * The matrix $\Sigma$ is symmetric, meaning that $\Sigma$ is equal to its transpose: $\Sigma = \Sigma^\top$.
# * For any non-zero vector $w$, the scalar value $x^\top \Sigma w$ is positive. This means that $w^\top \Sigma w > 0$ for any non-zero vector $w$.
# Geometrically, this means that the quadratic form defined by the matrix $\Sigma$ is always positive, and thus the matrix $\Sigma$ defines a "bowl-shaped" surface.
# The concept of positive definiteness is important in many areas of mathematics, particularly in linear algebra and optimization. For example, if the objective function of a quadratic optimization problem involves a positive definite matrix $\Sigma$, then the optimization problem has a unique global minimum, and this minimum can be found by solving a system of linear equations.
# :::
# 
# To solve this minimization problem, we can apply the Lagrange method and derive the first-order optimality conditions.
# The Lagrangian for this problem is given by:
# 
# $$
# \mathcal{L} = 0.5 w^\top \Sigma w + w^\top c-\lambda^\top(b-Aw)
# $$
# 
# Taking partial derivatives with respect to $w$ and λ, we can derive the Lagrange necessary (or first-order) conditions for a solution:
# 
# $$
# \Sigma w + A^\top \lambda + c = 0, \text{  and } Aw-b = 0. 
# $$
# 
# :::{note}
# The Lagrange method is a powerful tool for solving constrained optimization problems. It involves introducing Lagrange multipliers to convert a constrained optimization problem into an unconstrained optimization problem. The method is named after Joseph Louis Lagrange, a celebrated mathematician and physicist who was a professor at the University of Turin in 1755 and later served as director of mathematics at the Berlin Academy of Science, succeeding Euler in this position.
# :::
# 
# We can obtain the optimal value of $w$ by solving these equations algebraically. Specifically, we can start by solving the first equation for $w$, which gives:
# 
# $$
# \begin{align*}
# \Sigma w &= -A^\top \lambda - c\\
# w &= -\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c
# \end{align*}
# $$
# 
# Substituting this expression for $w$ into the second equation yields:
# 
# $$
# \begin{align*}
# &Aw-b = 0 \\
# &A(-\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c)-b= 0 \\
# &\lambda = -(A\Sigma^{-1}A^\top)^{-1}(A\Sigma^{-1}c+b)
# \end{align*}
# $$
# 
# Finally, we can substitute the value of λ into the expression for $w$ to obtain a closed-form solution for $w:$
# 
# $$
# \begin{align*}
# w &= -\Sigma^{-1}A^\top \lambda - \Sigma^{-1}c \\
#   &= -\Sigma^{-1}A^\top [-(A\Sigma^{-1}A^\top)^{-1}(A\Sigma^{-1}c+b)] - \Sigma^{-1}c \\
#   &= -\Sigma^{-1}[ -A^\top(A\Sigma^{-1}A^\top)^{-1}A\Sigma^{-1} +I]c 
#   +\Sigma^{-1}A^\top(A\Sigma^{-1}A^\top)^{-1}b\\
# \end{align*}
# $$
# 
# where $I$ is the identity matrix.
# 
# :::{note}
# The identity matrix is a square matrix with ones on the diagonal and zeros elsewhere. 
# :::
# 
# ### A Numerical Example
# In a portfolio risk-minimization problem, the objective is to minimize the variance of the portfolio for a given expected return level, subject to an equality constraint that the weights of the portfolio sum to 1. This can be translated into a quadratic optimization problem, where the risk of a portfolio is given by the variance-covariance matrix of the stock returns and the vector of stock weights. The mean return of the portfolio can be expressed as the dot product of the vector of mean returns and the vector of stock weights.
# 
# To illustrate this, let's consider a six-stock portfolio with known annualized mean returns and a variance-covariance matrix. We can construct the matrix A and vector b to reflect the equality constraint of summing to 1 by solve the following quadratic optimization problem:
# 
# $$
# \begin{align*}
# A&=
# \begin{bmatrix}
# 1 & \cdots & 1 \\
# \mu_1 & \cdots & \mu_N \\
# \end{bmatrix}\\
# b &=
# \begin{bmatrix}
# 1 \\
# \mu_P \\
# \end{bmatrix}\\
# c &= 0
# \end{align*}
# $$
# 
# It follows that
# 
# $$
# \begin{aligned}
# w &= \Sigma^{-1}A^\top(A\Sigma^{-1}A^\top)^{-1}b\\
# \end{aligned}
# $$
# 
# To provide a detailed illustration of the application, let's consider a simple portfolio consisting of six stocks. The annualized mean returns for these stocks are as follows: $μ_1$ = 14.4, $μ_2$ = 10.19, $μ_3$ = 9.87, $μ_4$ = 7.52, $μ_5$ = 20.05, and $μ_6$ = 2.66. The variances and covariances are expressed in percentage terms. For instance, the annualized variance for stock 1 is 452.33, which is equivalent to a variance of 452% per year (or a standard deviation of 21.26% per year). Finally, we select the value of $μ_P$ to reflect an annualized return of 8%.
# 
# Now, we can determine the optimal weights for the six stocks that will minimize the risk while achieving an expected mean return of 8% per year.

# In[1]:


import numpy as np
from numpy.linalg import inv

Sigma = np.array([[452.33, 249.33 , 189.23, 70.75,  481.14 , 106.5],
                  [249.33, 1094.09, 356.85, 93.51 , 1216.91, 135.05],
                  [189.23, 356.85 , 617.57, 161.82, 1304.29, 110.74],
                  [70.75 , 93.51  , 161.82, 372.35, 462.57 , 107.52],
                  [481.14, 1216.91, 1304.29, 462.57, 5658.42, 425.35],
                  [106.5 , 135.05,  110.74, 107.52, 425.35 , 244.31]])
print(Sigma)


# In[2]:


Sigma.T==Sigma


# In[3]:


A = np.array([[1,1,1,1,1,1],[14.4,10.19,9.87,7.52,20.05,2.66]])
print(A)


# In[4]:


b = np.array([1, 8])
print(b)


# In[5]:


w = inv(Sigma) @ A.T @ inv( A @ inv(Sigma) @ A.T) @ b
print(w)


# In[6]:


import cvxpy as cp

N = 6
w = cp.Variable(N)
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Minimize(risk), [A@w == b])
prob.solve(solver=cp.SCS)   

print( w.value, prob.value)


# The optimal solution for a portfolio with a capital of \$1 is to allocate \$0.305 to stock 1, \$0.057 to stock 2, \$0.204 to stock 3, \$0.274 to stock 4, short sell -\$0.085 of stock 5, and allocate \$0.245 to stock 6. However, the short position in stock 5 may not be feasible for many portfolio managers due to various reasons. Therefore, the portfolio manager may want to impose inequality constraints, such as requiring the weight of security 2 to be greater than 10%. Additionally, the portfolio manager may want to ensure that the weights of all securities are greater than zero. These restrictions were not applied in the preceding optimization, but we will introduce them in the next application of our example.
# 
# 
# ## Quadraric programming with inequality constraints
# The quadratic optimization problem with inequality constraints is generally more complex than the case of only equality constraints, and a closed-form solution may not be available. Therefore, numerical solution methods are often used to solve this type of problem. With the advances in computing power and optimization algorithms, numerical methods have become more reliable and efficient for solving quadratic programming problems with inequality constraints.
# 
# One commonly used approach is the active-set method or projection method, which involves iteratively updating a set of active constraints and solving a linear system of equations to find a new candidate solution. Another popular method is the interior-point method, which involves transforming the original problem into a sequence of barrier problems and solving a sequence of smaller optimization problems to approximate the solution to the original problem.
# 
# While these numerical methods can be quite effective, they do require a good understanding of the underlying mathematics and may be computationally intensive for large-scale problems. Fortunately, many software packages and optimization libraries are available that implement these methods and make it easier for portfolio managers and researchers to solve quadratic programming problems with inequality constraints. Therefore, it is not necessary to delve into the technical details of each method, but it is important to understand their underlying principles and limitations in order to use them effectively in practice.
# 
# ### A Numerical Example
# To further illustrate the application, we will continue with the previous numerical example and introduce some inequality constraints. We will use the active-set method to solve the problem. Specifically, we will add three inequality constraints that specify that the weights of each individual stock cannot be less than zero, except for stock 2, which cannot have a weight less than 0.10. Therefore, we have $w ≥ 0$ and $w_2 ≥ 0.10$. These inequality constraints can be easily incorporated into the matrix $A$. 
# The resulting optimization problem has the first two rows of $A$ representing equality constraints and the last seven rows representing inequality constraints. The formulation of the problem is as follows:

# In[7]:


A = np.array([[1,1,1,1,1,1],
              [14.4,10.19,9.87,7.52,20.05,2.66],
              [-1,0,0,0,0,0],
              [0,-1,0,0,0,0],
              [0,0,-1,0,0,0],
              [0,0,0,-1,0,0],
              [0,0,0,0,-1,0],
              [0,0,0,0,0,-1],
              [1,0,1,1,1,1]])
print(A)


# In[8]:


b = np.array([1, 8,0,0,0,0,0,0,0.9])
print(b)


# In[9]:


import cvxpy as cp

N = 6
w = cp.Variable(N)
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Minimize(risk), [A[:2,:]@w == b[:2], A[2:,:]@w <= b[2:]])
prob.solve(solver=cp.SCS)   

print( np.round(w.value,3), np.round(prob.value,3))


# It's worth noting that we expressed the constraint $w_2 ≥ 0.10$ as $w_1+w_3+w_4+w_5+w_6 ≤ 0.90$. This is because in certain cases, such as when using certain programming tools, the most apparent constraints may require some tweaking or reengineering to fit into the optimization problem.
# 
# # Advanced Techniques for Quadratic Optimization
# While the basic techniques covered in this chapter address most portfolio optimization problems, there are scenarios where the optimization setup needs to be expanded. For instance, a portfolio manager may need to factor in transaction costs or create a market-neutral portfolio with leverage constraints. Other situations may involve restrictions on the number of stocks in the portfolio, where the number falls between a minimum and maximum or where the weights of any security are either zero or within a minimum and maximum weight. These and other preferences in the optimization require an expanded optimization framework. Additionally, some portfolio optimization problems may involve quadratic constraints, which are not part of the typical optimization framework. In this section, we will discuss the fundamental building blocks for expanding the optimization framework to address these advanced optimization scenarios.
# 
# ### Phantom weights
# In standard portfolio optimization problems, we typically only have $N$ unknowns, which are the portfolio weights. However, in certain nonstandard portfolio problems, it can be useful to introduce what we call "phantom weights." The idea of phantom weights is to create additional weights, in addition to the actual weights of the portfolio, that the optimizer will also find optimal values for. These additional weights can be used for various purposes, such as creating a set of buy and sell weights. For example, if the optimization problem has $N$ stocks, we can create an additional $2N$ weights, denoted as $b_1$ to $b_N$ and $s_1$ to $s_N$. With these additional weights, the new optimization problem becomes more complex, as we now have $3N$ weights to choose from. However, phantom weights offer many benefits in portfolio optimization. Often, the phantom weights have a specific relationship to the underlying weights, such as $b + s = 1$, where $b$ and $s$ are the buy and sell weights, respectively.
# 
# ### Binary weights
# In portfolio optimization, it may be beneficial to use binary variables as optimization weights in addition to phantom weights. Binary variables are weights that are constrained to have a value of either 0 or 1. One practical application of binary variables is to ensure that phantom weights are orthogonal. This is important because having both a long position and a short position on the same stock (i.e., $b>0$ and $s>0$) is a wasteful solution. By creating binary variables and for each of the $N$ stocks, we can add a constraint to force the phantom weights to be orthogonal. The constraint can be formulated as follows:
# 
# To incorporate binary variables as optimization weights, one can create $v_i^+$ and $v_i^-$ binary variables for each of the $N$ stocks. By adding the constraint
# 
# $$
# \begin{aligned}
# & v_i^+\kappa_l \le b_i \le v_i^+\kappa_h \\
# & v_i^-\gamma_l \le s_i \le v_i^-\gamma_h \\
# \end{aligned}
# $$
# 
# and setting $\kappa_l = \gamma_l = 0$ and $\kappa_h = \gamma_h = 1$, the weights can fluctuate between 0 and 1, and the constraint $v_i^++v_i^-\le 1$ ensures that the phantom weights are orthogonal. If $b_i>0$, then $s_i=0$ and vice versa for every stock $i$. However, the addition of binary and phantom weights and their associated constraints makes the optimization problem more complex and challenging to solve.
# 
# ### Market neutrality with leverage constraints
# 
# Adding the following constraints to the optimization problem will create a market-neutral portfolio that is dollar neutral and has limited leverage:
# 
# $$
# \begin{aligned}
# & w_i = w_i^{+} - w_i^{-} \\
# & \sum\limits_{i=1}^N w_i^+ = \sum\limits_{i=1}^N w_i^-\\
# & w_i^+ \ge 0\\
# & w_i^- \ge 0\\
# & \sum\limits_{i=1}^N w_i^+ + \sum\limits_{i=1}^N w_i^- \le 2\\
# \end{aligned}
# $$
# 
# where $w_i^{+}=b_i$ and $w_i^{-}=s_i$.
# These constraints ensure that the sum of the weights of the long stocks equals the sum of the weights of the shorted stocks, creating a dollar-neutral portfolio. The leverage of the portfolio is limited to 2, meaning that the portfolio is 100% long and 100% short of the assets under management.
# 
# If the market-neutral manager wanted to increase the leverage, they could adjust the constraints on the sum of the phantom long and short weights. For example, to create a 130-30 long-short portfolio, one could set $L_l = 1.3$ and $L_s = 0.3$ in the following constraints:
# 
# $$
# \begin{aligned}
# & \sum\limits_{i=1}^N w_i^+=L_l\\
# & \sum\limits_{i=1}^N w_i^-=L_s
# \end{aligned}
# $$
# 
# This would result in a portfolio with long exposure of 130% and short exposure of 30%.
# 
# 
# ## Transactions costs
# When we want to rebalance a portfolio while considering transaction costs (or market impact), we can use phantom weights and binary variables to find an exact solution to the portfolio optimization problem. To do this, we need to add constraints to the optimization problem that consider the current weights of the portfolio represented by $w_b$ and the target weights after rebalancing represented by $w_a$:
# 
# $$
# w_i^a = w_i^b+w_i^+-w_i^-
# $$
# 
# The relationship between the binary variables and the phantom weights is set such that $\kappa_l = \gamma_l = 0$ and $\kappa_h = \gamma_h = 1$, which allows the weights to fluctuate between 0 and 1. We also add the constraint that $v_i^++v_i^-\le 1$ to ensure the phantom weights are orthogonal. Stocks that have reduced weight from the prior portfolio will have negative net weights but positive phantom weights, denoted by $w_i^-$. We can multiply the transactions cost vector by their value. Conversely, stocks that have increased weight will have positive phantom weights, denoted by $w_i^+$, and can also be multiplied by the transactions cost vector. The final optimized weights of the portfolio will be $w_i$. In the case of transaction costs, the phantom weights serve as a mechanism to denote the change to the current weights, storing the positive changes in the positive phantom weights and the negative changes in the negative phantom weights. Both positive and negative phantom weights are positive, so the transaction cost vector remains positive, and the transaction cost rebalance problem is resolved.
# 
# 
# ## Elimination of small-weight stocks
# Portfolio managers may want to reduce the number of securities in their portfolio, which can be achieved by constructing an optimized portfolio that forces individual stock weights to be above a minimum or below a maximum weight. However, the traditional method of adding inequality constraints to optimize weights may not always result in a solution, as it forces all stocks to be within a given range, which may not be optimal. The use of binary variables can create an optimization that limits the optimizer to find weights between the minimum and maximum or forces the weight of a particular stock to zero. This results in more successful optimizations and aligns better with the portfolio manager's thought process.
# 
# To illustrate, we will focus on the situation where all stock weights should be between a lower bound ($\kappa_l$) and an upper bound ($\kappa_h$) for the long portion of the portfolio. Using the inequality relationship of the binary variables and phantom weights, we can set $v_i^+\kappa_l \le b_i \le v_i^+\kappa_h$ and $v_i^-\gamma_l \le s_i \le v_i^-\gamma_h$. Once we specify the values for $\kappa_l$, $\gamma_l$, $\kappa_h$, and $\gamma_h$, we can effectively achieve our goal. If the portfolio is only a long portfolio, phantom weights are not needed, and we should construct one set of binary variables with respect to the actual weights, $w_i$. The binary variables can be either 0 or 1, and the weights of the portfolio will be selected to be within the minimum and maximum weights or set to zero.
# 
# 
# ## A numerical example
# Building upon the previous numerical example, we aim to construct a portfolio that delivers an average annualized return of 8% without short sales and with the restriction that the weights of the portfolio must sum to 1. We further impose the constraint that the weight of each stock can only be greater than 0.03 (i.e., 3%) or less than 0.30 (i.e., 30%), or it must be 0.
# 
# To represent these constraints mathematically, we construct the matrix A, where the first two rows denote equality constraints that the sum of weights should equal 1 and that the target mean return is 8%. Since binary weights are not relevant for these constraints, we place 0 in the corresponding matrix elements. The remaining rows of the matrix are inequality constraints that restrict the weights of each stock to lie between 0.03 and 0.30 or be 0. We use the values of $\kappa_l$ and $\kappa_h$ to ensure that $0.03v_i^+ \le w_i \le 0.3v_i^+$, where $v_i^+$ is a binary variable. If $v_i^+$ equals 1, the weight of stock $i$ must lie within the range of 0.03 to 0.30. Otherwise, if it is more optimal for the weight of stock $i$ to be 0, then $v_i^+= 0$, and $w_i$ is also equal to 0.

# In[10]:


import numpy as np
import gurobipy as gp


# In[11]:


Sigma = np.array([[452.33, 249.33 , 189.23, 70.75,  481.14 , 106.5],
                  [249.33, 1094.09, 356.85, 93.51 , 1216.91, 135.05],
                  [189.23, 356.85 , 617.57, 161.82, 1304.29, 110.74],
                  [70.75 , 93.51  , 161.82, 372.35, 462.57 , 107.52],
                  [481.14, 1216.91, 1304.29, 462.57, 5658.42, 425.35],
                  [106.5 , 135.05,  110.74, 107.52, 425.35 , 244.31]])
print(Sigma)


# In[12]:


A = np.array([[1,1,1,1,1,1,0,0,0,0,0,0],
              [14.4,10.19,9.87,7.52,20.05,2.66,0,0,0,0,0,0],
              [1,0,0,0,0,0,-0.3,0,0,0,0,0],
              [0,1,0,0,0,0,0,-0.3,0,0,0,0],
              [0,0,1,0,0,0,0,0,-0.3,0,0,0],
              [0,0,0,1,0,0,0,0,0,-0.3,0,0],
              [0,0,0,0,1,0,0,0,0,0,-0.3,0],
              [0,0,0,0,0,1,0,0,0,0,0,-0.3],
              [-1,0,0,0,0,0,0.03,0,0,0,0,0],
              [0,-1,0,0,0,0,0,0.03,0,0,0,0],
              [0,0,-1,0,0,0,0,0,0.03,0,0,0],
              [0,0,0,-1,0,0,0,0,0,0.03,0,0],
              [0,0,0,0,-1,0,0,0,0,0,0.03,0],
              [0,0,0,0,0,-1,0,0,0,0,0,0.03]])

print(A)


# In[13]:


b = np.array([[1,8,0,0,0,0,0,0,0,0,0,0,0,0]])
print(b)


# In[14]:


print(Sigma.shape, A.shape, b.shape)


# In[15]:


# Create a GurobiPy model
model = gp.Model()
model.setParam('OutputFlag', 0)

# Create the decision variables
w = model.addVars(12, vtype=[gp.GRB.CONTINUOUS]*6 + [gp.GRB.BINARY]*6)

# Add the constraints Aw = b for the first two rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) == b[0,j] for j in range(2))

# Add the constraints Aw <= b for the rest of the rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) <= b[0,j] for j in range(2,14))

risk = 0.5 * gp.quicksum(Sigma[i,j]*w[i]*w[j] for i in range(6) for j in range(6))
model.setObjective(risk, gp.GRB.MINIMIZE)

# Solve the model
model.optimize()

# Print the solution
if model.status == gp.GRB.OPTIMAL:
    print("Solution found!")
    for i in range(12):
        print(f"w[{i}] = {np.round(w[i].x,3)}")
else:
    print("No solution found.")


# ## Limiting the Number of Stocks in a Portfolio
# 
# Portfolio managers may choose to limit the number of stocks in their portfolio for various reasons. For instance, it might be more manageable to handle a portfolio with fewer stocks, especially when using a regularly rebalanced quantitative model. To achieve this, portfolio optimization can be performed, allowing managers to restrict the number of stocks within a range of $n_l$ to $n_h$. Here, phantom weights are not necessary unless the managers are working with a long-short portfolio.
# 
# If the managers are only limiting the number of stocks, binary variables will suffice. For a long-only portfolio, the managers should create a set of $N$ binary variables, $v_i^+$, while for a long-short portfolio, they should create two sets of binary variables, $v_i^+$ and $v_i^-,$ allowing them to specify the range of stocks in both the long and short portfolios, respectively. To ensure that the number of stocks in the long portfolio is within the specified range, two inequality constraints should be added. The first constraint is that $\sum\limits_{i=1}^Nv_i^+ \leq n_h$, while the second constraint is that $n_l \leq \sum\limits_{i=1}^Nv_i^+$. For optimization frameworks that require it, the second inequality can be transformed into $-\sum\limits_{i=1}^Nv_i^+ \leq -n_l$. Similarly, for a long-short portfolio, the portfolio manager should add similar constraints on the short portfolio using the corresponding binary variables.
# 
# 
# ## A numerical example
# Continuing from the previous example, our goal is to construct a portfolio with an average annualized return of 8%, without short sales and with the portfolio weights summing to 1. However, we want to restrict the portfolio to have no more than three stocks, despite having six stocks available for purchase.
# 
# As before we condense the quadratic programming problem to 
# 
# $$
# \begin{aligned}
# \min\limits_w 0.5 w^T \Sigma w\quad\text{s.t}\quad Ax \le b
# \end{aligned}
# $$

# In[16]:


import numpy as np
import gurobipy as gp


# In[17]:


Sigma = np.array([[452.33, 249.33 , 189.23, 70.75,  481.14 , 106.5],
                  [249.33, 1094.09, 356.85, 93.51 , 1216.91, 135.05],
                  [189.23, 356.85 , 617.57, 161.82, 1304.29, 110.74],
                  [70.75 , 93.51  , 161.82, 372.35, 462.57 , 107.52],
                  [481.14, 1216.91, 1304.29, 462.57, 5658.42, 425.35],
                  [106.5 , 135.05,  110.74, 107.52, 425.35 , 244.31]])
print(Sigma)


# In[18]:


A = np.array([[1,1,1,1,1,1,0,0,0,0,0,0],
              [14.4,10.19,9.87,7.52,20.05,2.66,0,0,0,0,0,0],
              [1,0,0,0,0,0,-1,0,0,0,0,0], 
              [0,1,0,0,0,0,0,-1,0,0,0,0],
              [0,0,1,0,0,0,0,0,-1,0,0,0],
              [0,0,0,1,0,0,0,0,0,-1,0,0],
              [0,0,0,0,1,0,0,0,0,0,-1,0],
              [0,0,0,0,0,1,0,0,0,0,0,-1],
              [-1,0,0,0,0,0,0,0,0,0,0,0],
              [0,-1,0,0,0,0,0,0,0,0,0,0],
              [0,0,-1,0,0,0,0,0,0,0,0,0],
              [0,0,0,-1,0,0,0,0,0,0,0,0],
              [0,0,0,0,-1,0,0,0,0,0,0,0],
              [0,0,0,0,0,-1,0,0,0,0,0,0],
              [0,0,0,0,0,0,1,1,1,1,1,1],
              [0,0,0,0,0,0,-1,-1,-1,-1,-1,-1]])
print(A)


# In[19]:


b = np.array([[1,8,0,0,0,0,0,0,0,0,0,0,0,0,3,0]])
print(b)


# In[20]:


print(Sigma.shape, A.shape, b.shape)


# The $A$ matrix consists of two rows that represent equality constraints. The first row indicates that the sum of weights must be equal to 1, and the second row represents the constraint that the target mean is 8%. For binary weights, a 0 value is assigned to the matrix, as they are not relevant for these constraints.
# 
# The remaining rows of the $A$ matrix represent inequality constraints that limit the weight of each stock between 0 and 1. The last two rows of the matrix represent inequality constraints on the binary variables. Specifically, they ensure that the sum of the binary variables is between 0 and 3, which is equivalent to limiting the number of stocks to be less than or equal to three.

# In[21]:


# Create a GurobiPy model
model = gp.Model()
model.setParam('OutputFlag', 0)

# Create the decision variables
w = model.addVars(12, vtype=[gp.GRB.CONTINUOUS]*6 + [gp.GRB.BINARY]*6)

# Add the constraints Aw = b for the first two rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) == b[0,j] for j in range(2))

# Add the constraints Aw <= b for the rest of the rows
model.addConstrs(gp.quicksum(A[j,i] * w[i] for i in range(12)) <= b[0,j] for j in range(2,16))

risk = 0.5 * gp.quicksum(Sigma[i,j]*w[i]*w[j] for i in range(6) for j in range(6))
model.setObjective(risk, gp.GRB.MINIMIZE)

# Set the objective function to zero (since this is a feasibility problem)
model.setObjective(risk, sense=gp.GRB.MINIMIZE)

# Solve the model
model.optimize()

# Print the solution
if model.status == gp.GRB.OPTIMAL:
    print("Solution found!")
    for i in range(12):
        print(f"w[{i}] = {np.round(w[i].x,3)}")
else:
    print("No solution found.")

