#!/usr/bin/env python
# coding: utf-8

# # A1) Hands-on Optimization
# Optimization is a powerful tool that is widely used in practice to solve real-world problems. Optimization problems arise in a variety of fields such as finance, engineering, operations research, and machine learning. These problems often involve decision-making under constraints, where one needs to find the best possible solution given the available resources.
# 
# By using optimization techniques, we can identify the optimal solution that satisfies the given constraints and minimizes or maximizes the objective function. This allows us to make better decisions and achieve our desired outcomes more efficiently.
# 
# In finance, optimization is used to solve problems such as portfolio optimization, asset allocation, and risk management. In engineering, optimization is used to design and optimize systems such as transportation networks, communication systems, and manufacturing processes. In operations research, optimization is used to solve problems such as production planning, inventory management, and supply chain optimization.
# 
# Optimization is also widely used in machine learning to train models and make predictions. In machine learning, optimization techniques are used to find the optimal parameters of a model that best fits the data and minimizes the error.
# 
# In this chapter, we will discuss examples of linear programming (LP), binary optimization, and mixed-integer programming (MIP).
# We will introduce the widely used optimization libraries such as CVXPY, GurobiPy, and Mosek Fusion that can be used to solve optimization problems effectively. These libraries provide user-friendly interfaces to model and solve optimization problems using a variety of algorithms and solvers.
# 
# First, we will discuss LP, which is a technique to optimize a linear objective function subject to linear constraints. 
# Next, we will cover binary optimization, which involves decision-making in scenarios where the variables can only take binary values of 0 or 1. 
# Lastly, we will delve into mixed-integer programming, which involves optimization problems where some or all of the variables can take both continuous and discrete values.
# 
# # Simple Linear Programing model
# Let's consider a simple example of a company that produces two products, Product A and Product B, to illustrate the usefulness of optimization in practice.
# 
# To produce one unit of Product A, the company requires 2 hours of labor and 3 pounds of material. The company has 80 hours of labor available and 120 pounds of material available. To produce one unit of Product B, the company requires 3 hours of labor and 2 pounds of material. The company has 60 hours of labor available and 100 pounds of material available. The profit for each unit of Product A is \$5, and the profit for each unit of Product B is \$4. The objective is to maximize the company's profit subject to the available resources.
# 
# Optimization is useful in practice because it helps us make better decisions by finding the best possible solution to a problem given certain constraints. In this case, the LP model helps us determine the optimal number of units of Product A and Product B that the company should produce to maximize its profit while staying within the available resources.
# 
# Let's call the number of units of Product A produced $x_1$ and the number of units of Product B produced $x_2$. Then, the LP model is:
# 
# $$
# \begin{aligned}
# &\text{Maximize } &&5x_1 + 4x_2 \\
# &\text{Subject to } &&2x_1 + 3x_2 \le 80 &&\text{(labor constraint for Product A)} \\
# &&&3x_1 + 2x_2 \le 60 &&\text{(labor constraint for Product B)} \\
# &&&3x_1 + 2x_2 \le 100 &&\text{(material constraint for both products)} \\
# &&&x_1, x_2 \ge 0 &&\text{(non-negativity constraint)}
# \end{aligned}
# $$
# 
# We can use various optimization solvers such as CVXPY, GUROBIPY, and MOSEK in Python to solve this LP model and find the optimal solution.
# 
# ## Using CVXPY

# In[1]:


import cvxpy as cp
import numpy as np

x = cp.Variable(2, nonneg=True)
objective = cp.Maximize(5*x[0] + 4*x[1])
constraints = [2*x[0] + 3*x[1] <= 80,
               3*x[0] + 2*x[1] <= 60,
               3*x[0] + 2*x[1] <= 100]
prob = cp.Problem(objective, constraints)
prob.solve()

print("Optimal value:", prob.value)
print("Optimal solution:", x.value)


# ## Using GUROBIPY

# In[2]:


import gurobipy as gp

model = gp.Model()
model.setParam('OutputFlag', 0)

x = model.addVars(2, lb=0, vtype=gp.GRB.CONTINUOUS)
objective = 5*x[0] + 4*x[1]
model.setObjective(objective, sense=gp.GRB.MAXIMIZE)
model.addConstr(2*x[0] + 3*x[1] <= 80)
model.addConstr(3*x[0] + 2*x[1] <= 60)
model.addConstr(3*x[0] + 2*x[1] <= 100)
model.optimize()

print("Optimal value:", model.objVal)
print("Optimal solution:", [x[i].x for i in range(2)])


# ## Using MOSEK

# In[3]:


import mosek.fusion as mf

M = mf.Model('LP example')

# Define variables
x = M.variable('x', 2, mf.Domain.greaterThan(0.0))

# Define objective
c = [5.0, 4.0]
M.objective('obj', mf.ObjectiveSense.Maximize, mf.Expr.dot(c, x))

# Define constraints
A = [[2.0, 3.0], [3.0, 2.0], [3.0, 2.0]]
b = [80.0, 60.0, 100.0]
for i in range(len(A)):
    M.constraint('c{}'.format(i), mf.Expr.dot(A[i], x), mf.Domain.lessThan(b[i]))

# Solve the problem
M.solve()

# Print the results

print("Optimal value:", M.primalObjValue()) 
print("Optimal solution:", x.level())


# # Binary optimization problem 
# In optimization, one of the most common types of problems is the Mixed Integer Programming (MIP) problem. This is a mathematical optimization problem where some of the variables are restricted to be integers. Binary Optimization, where the variables can only take on values of 0 or 1, is a special case of MIP.
# 
# In this context, we will solve a binary optimization problem using CVXPY and GUROBI. The problem is to minimize the objective function $x_1 + x_2 + x_3$, subject to the constraints $x_1 + x_2 \ge 2$, $x_2 + x_3 \le 1$, and $x_1, x_2, x_3$ are binary variables. 
# 
# ## Using CVXPY + GUROBI
# $$
# \begin{aligned}
# &\text{minimize } &&x_1 + x_2 + x_3 \\
# &\text{subject to } &&x_1 + x_2 \ge 2 \\
# &&&x_2 + x_3 \le 1 \\
# &&&x_1, x_2, x_3 \text{ are binary variables}
# \end{aligned}
# $$

# In[4]:


import cvxpy as cp

# Define problem data
A = [[1, 1, 0], [0, 1, 1]]
b = [2, 1]

# Define binary decision variables
x = cp.Variable(3, boolean=True)

# Define objective function
obj = cp.sum(x)

# Define constraints
constraints = [
    A[0] @ x >= b[0],
    A[1] @ x <= b[1]
]

# Define the problem
problem = cp.Problem(cp.Minimize(obj), constraints)

# Solve the problem
problem.solve(solver=cp.GUROBI)

# Print results
print("CVXPY + GUROBI Solution:")
print("status:", problem.status)
print("optimal value:", obj.value)
print("optimal x:", x.value)


# # Mixed-integer programming problem
# In many real-world problems, we encounter situations where decision variables must take on integer values. For example, in production planning, the number of items produced must be an integer value. MIP provides a way to find optimal solutions to these types of problems.
# 
# In this example, we will solve a very simple MIP problem using CVXPY and GUROBI solver. Suppose we want to maximize the following objective function:
# 
# $$
# \begin{aligned}
# &\text{maximize } &&3x_1 + 2x_2 \\
# &\text{subject to } &&x_1 + x_2 \leq 4 \\
# &&&x_1 \ge 0 \\
# &&&x_2 \ge 0 \\
# &&&x_1, x_2 \in \mathbb{Z}, \text{ where $\mathbb{Z}$ denotes the set of integers}
# \end{aligned}
# $$ 
# 
# Here, we want to find integer values for $x_1$ and $x_2$ that satisfy the constraints and maximize the objective function. This is a very simple example, but it can help us understand the basic syntax and structure of solving MIP problems using CVXPY.
# 
# ## Using CVXPY + GUROBI

# In[5]:


import cvxpy as cp
import mosek

# Define the variables
x1 = cp.Variable(integer=True)
x2 = cp.Variable(integer=True)

# Define the objective function
obj = cp.Maximize(3*x1 + 2*x2)

# Define the constraints
constr = [x1 + x2 <= 4, x1>=0, x2>=0]

# Create the problem instance and solve it
prob = cp.Problem(obj, constr)
prob.solve(solver=cp.GUROBI)

# Print the optimal solution and optimal value
print("Optimal solution: x1 = {}, x2 = {}".format(x1.value, x2.value))
print("Optimal value: {}".format(prob.value))


# # Nonlinear programming problem
# Nonlinear optimization is a type of optimization problem where the objective function or the constraints are nonlinear. Unlike linear optimization, nonlinear optimization problems can be more complex to solve due to the non-convexity of the objective function and/or constraints. 
# 
# In this example, we will consider a simple nonlinear optimization problem of minimizing a quadratic function subject to a linear constraint. We want to minimize the function $f(x) = x_1^2 + x_2^2$ subject to the constraint $x_1 + x_2 \geq 1$. This problem can be solved using nonlinear optimization techniques such as gradient descent, Newton's method, or quasi-Newton methods. However, we will use cvxpy, a Python library for convex optimization, to solve this problem.
# 
# We can express this as an optimization problem:
# 
# $$
# \begin{aligned}
# &\text{minimize } &&x_1^2 + x_2^2 \\
# &\text{subject to } &&x_1 + x_2 \geq 1 
# \end{aligned}
# $$
# 
# To solve this problem using MOSEK, we first define the optimization variables and the objective function:
# 
# ## Using CVXPY + MOSEK

# In[6]:


import cvxpy as cp

# Define the optimization variables
x = cp.Variable(2)

# Define the objective function
objective = cp.Minimize(cp.sum_squares(x))

# Define the constraint
constraint = [x[0] + x[1] >= 1]

# Create the optimization problem
problem = cp.Problem(objective, constraint)

# Solve the problem using the Mosek solver
problem.solve(solver=cp.MOSEK)

# Print the optimal solution and optimal value
print("Optimal solution: x1 = {}, x2 = {}".format(np.round(x[0].value,3), np.round(x[1].value,3)))
print("Optimal value: {}".format(np.round(problem.value,3)))


# # Multiobjective optimization
# Goal programming, also known as multi-objective optimization, is a technique used to solve decision-making problems that involve multiple, often conflicting objectives. It is particularly useful in situations where there is no clear trade-off between objectives and all objectives are important.
# 
# In goal programming, the decision maker identifies a set of goals or objectives to be achieved and then formulates a mathematical model that minimizes the deviations from those goals. The model typically includes decision variables, constraints, and a set of goals or objectives to be achieved. These goals or objectives can be of different types, such as maximizing or minimizing a certain quantity, achieving a certain level of performance, or meeting specific requirements. The model seeks to minimize these deviations subject to the constraints.
# 
# The goals or objectives can be conflicting, meaning that achieving one may come at the expense of the other. In such cases, the decision maker must balance these conflicting objectives and find a solution that achieves a satisfactory compromise. This can be done by assigning weights to each objective, where higher weights indicate higher priority. Alternatively, penalty functions can be used to penalize deviations from certain objectives more heavily than others.
# 
# For example, a company wants to maximize their profits, but also wants to ensure that they don't produce more than a certain amount of waste. They have three goals:
# 
# * Maximize profits
# * Minimize waste produced
# * Achieve a certain level of production
#  
# Let $x$ be the amount of product produced, $p$ be the profit per unit sold, and $w$ be the amount of waste produced per unit produced. Then we can formulate the following goal programming model:
# 
# $$
# \begin{aligned}
# &\text{minimize } &&z_1 + z_2 + z_3\\
# &\text{where}
# &&z_1 = | \text{profit} - \text{target profit}|\\
# &&&z_2 = | \text{waste} - \text{target waste}|\\
# &&&z_3 = |x - \text{target production}|\\
# &\text{subject to}
# &&\text{profit} = p \cdot x\\
# &&&\text{waste} = w \cdot x\\
# &&&x \geq 0\\
# &&&\text{profit} \geq \text{target profit}\\
# &&&\text{waste} \leq \text{target waste}\\
# &&&x = \text{target production}
# \end{aligned}
# $$
# 
# where target profit, target waste, and target production are the company's goals for each respective metric.
# 
# We can solve this model using the CVXPY package with the GUROBI solver. Here's the code:

# In[7]:


import cvxpy as cp
import numpy as np

# Define the problem data
p = 10  # profit per unit sold
w = 0.5  # waste per unit produced
target_profit = 1000
target_waste = 500
target_production = 200

# Define the decision variables
x = cp.Variable()

# Define the constraints
constraints = [x >= 0,
               p * x >= target_profit,
               w * x <= target_waste,
               x == target_production]

# Define the objective function
objective = cp.Minimize(cp.abs(p * x - target_profit) +
                        cp.abs(w * x - target_waste) +
                        cp.abs(x - target_production))

# Solve the problem
prob = cp.Problem(objective, constraints)
prob.solve(solver=cp.GUROBI)

# Print the results
print("Status: ", prob.status)
print("Optimal value: ", np.round(prob.value,3))
print("Optimal x: ", np.round(x.value,3))
print("Profit: ", p * np.round(x.value,3))
print("Waste: ", np.round(w * x.value,3))


# ## Blended Multiobjective Optimization
# The above problem is actually a blended multiobjective optimization problem, where we aim to minimize a linear combination of multiple objectives. Blended multiobjective optimization involves finding a solution that optimizes multiple objectives by combining them into a single objective using weighted coefficients.
# 
# In the following example, we aim to minimize a linear combination of two decision variables, $x_1$ and $x_2$, subject to two linear constraints. The objective function is defined as $0.4x_1 + 0.6x_2$, which is a weighted sum of the two decision variables. The weights of the decision variables determine their relative importance in the optimization process.
# 
# $$
# \begin{aligned}
# &\text{minimize} && 0.4x_1 + 0.6x_2 \\
# &\text{subject to} 
# &&-2x_1 + 3x_2 \geq 6 \\
# & &&3x_1 + 2x_2 \geq 12 \\
# & &&x_1, x_2 \geq 0 \\
# \end{aligned}
# $$
# 
# Here, the problem is subject to two linear constraints, which are defined as $-2x_1 + 3x_2 \geq 6$ and $3x_1 + 2x_2 \geq 12$. These constraints represent the feasible region of the problem, where the solution must lie. Additionally, we have the non-negative constraint $x_1, x_2 \geq 0$, which means that the decision variables cannot be negative.
# 
# Here is the Python code to solve a the blended multiobjective optimization problem using CVXPY and GUROBI:

# In[8]:


import cvxpy as cp
from gurobipy import *

# Define the problem data
n = 2
m = 2
A = np.array([[-2, 3], [3, 2]])
b = np.array([6, 12])
c = np.array([0.4, 0.6])

# Define the decision variables
x = cp.Variable(n)

# Define the objective function
obj = cp.Minimize(c @ x)

# Define the constraints
constraints = [A @ x >= b, x >= 0]

# Solve the problem using CVXPY and Gurobi
prob = cp.Problem(obj, constraints)
prob.solve(solver=cp.GUROBI)

# Print the optimal value and the optimal solution
print("Optimal value =", np.round(prob.value,3))
print("Optimal solution =", np.round(x.value,3))


# ## Hierarchical Multiobjective Optimization
# Hierarchical Multiobjective Optimization (HMO) is an approach to solving complex optimization problems with multiple objectives that are often conflicting and cannot be optimized simultaneously. In HMO, the objective functions are organized in a hierarchy, where the higher-level objectives are more important than the lower-level objectives. The optimization problem is solved in a hierarchical manner, where the lower-level objectives are optimized subject to the constraints and objectives of the higher-level problems.
# 
# As an example, let's consider the following example:
# 
# $$
# \begin{aligned}
# & \text{minimize} && f_1(x) = x_1^2 + x_2^2 \\
# & \text{subject to} && g(x) = x_1 + x_2 - 1 \ge 2 \\
# &&&\\
# & \text{minimize} && f_2(x) = \left\lVert x - \begin{bmatrix}1 \ 1\end{bmatrix} \right\rVert_2 \\
# & \text{subject to} && h(x) = x_1 - x_2 - 1 \leq -2 \\
# &&& f_1(x) \leq f_1^*
# \end{aligned}
# $$
# 
# In this example, we have two optimization problems that we want to solve using Python, CVXPY, and GUROBI. In the first problem, we aim to minimize the sum of squares of two real-valued variables, subject to the constraint that the sum of the variables is less than or equal to 1. In the second problem, we want to minimize the Euclidean distance between a two-dimensional real-valued variable and the point [1,1], subject to the constraint that the difference between the variables is less than or equal to 1 and subject to the additional constraint that the value of the objective function from the first problem is less than or equal to a previously calculated value.
# 
# Here is the code to solve the hierarchical multiobjective optimization problem using CVXPY and GUROBI:

# In[9]:


import cvxpy as cp
import numpy as np
# Define the variables
x = cp.Variable(2)

# Define the constraints
g = x[0] + x[1] - 1
h = x[0] - x[1] - 1

# Define the objective functions
f1 = cp.sum_squares(x)
f2 = cp.norm(x - np.array([1, 1]), 2)

# Define problem 1
problem1 = cp.Problem(cp.Minimize(f1), [g >= 2])
problem1.solve(solver=cp.GUROBI)
f1_star = problem1.value
x1_star = x.value

print("Optimal value of f1: ", np.round(problem1.value,3))
print("Optimal decision variables: ", np.round(x1_star,3))
    
# Define problem 2 with f1_star constraint
problem2 = cp.Problem(cp.Minimize(f2), [h <= -2, f1 <= f1_star])

# Solve problem 2
try:
    problem2.solve(solver=cp.GUROBI)
    print("Optimal value of f2: ", np.round(problem2.value,3))
    x2_star = x.value
    print("Optimal decision variables: ", np.round(x2_star,3))
except cp.error.SolverError:
    print("Solver failed to find optimal value for problem2")


# # Risk-adjusted portfolio optimization
# Risk-adjusted portfolio optimization is a common problem in finance, where the goal is to find the optimal allocation of assets that maximizes expected returns while minimizing risks. One common approach to risk-adjusted portfolio optimization is the mean-variance optimization model developed by Harry Markowitz. The model assumes that investors are risk-averse and seek to maximize the expected return while minimizing the variance of their portfolio.
# 
# The mean-variance optimization model can be expressed mathematically as follows:
# 
# $$
# \begin{aligned}
# & \text{maximize} && \mu^T x - \gamma x^T \Sigma x \\
# & \text{subject to} && \sum_{i=1}^n x_i = 1 \\
# & && x \geq 0
# \end{aligned}
# $$
# 
# where $\mu$ is a vector of expected returns for each asset, $\Sigma$ is the covariance matrix of asset returns, $x$ is a vector of weights for each asset, and $\gamma$ is a scalar that represents the risk aversion of the investor.
# 
# The parameter $\gamma$ can be adjusted to reflect the risk aversion of the investor. A higher value of $\gamma$ indicates a higher level of risk aversion, leading to a portfolio with lower expected returns but also lower risk. On the other hand, a lower value of $\gamma$ indicates a lower level of risk aversion, leading to a portfolio with higher expected returns but also higher risk.
# 
# In the following example, we randomly generated expected returns and covariance matrix for a portfolio of three assets. We set the risk aversion parameter $\gamma$ to 0.5. We defined the decision variables, objective function, and constraints using CVXPY. We then solved the problem using the Gurobi solver through the CVXPY interface. Finally, we printed out the optimal value and optimal solution of the problem.

# In[10]:


import cvxpy as cp
import numpy as np
import gurobipy as gp

# Define the problem data
n = 3
np.random.seed(1)
mu = np.abs(np.random.randn(n))
Sigma = np.abs(np.random.randn(n, n))
Sigma = Sigma.T @ Sigma
gamma = 0.5

# Define the decision variables
x = cp.Variable(n)

# Define the objective function
objective = cp.Maximize(mu.T @ x - gamma * cp.quad_form(x, Sigma))

# Define the constraints
constraints = [cp.sum(x) == 1, x >= 0]

# Solve the problem using CVXPY and Gurobi solver
prob = cp.Problem(objective, constraints)
prob.solve(solver=cp.GUROBI)

# Print the optimal value and the optimal solution
print("Optimal value =", prob.value)
print("Optimal solution =", x.value)


# # Sharpe Ratio maximization
# To maximize the Sharpe ratio, we need to use the formula:
# 
# $$
# \text{Sharpe Ratio} = (r_p - r_f) / σ_p
# $$
# 
# where $r_p$ is the expected return of the portfolio, $r_f$ is the risk-free rate, and $σ_p$ is the standard deviation of the portfolio returns. The goal is to find the portfolio weights that maximize the Sharpe ratio.
# 
# We can solve this optimization problem using a similar code structure as before. First, we generate a set of random portfolio weights, calculate the expected returns and standard deviation of the portfolio, and then calculate the Sharpe ratio for each portfolio. Finally, we find the portfolio with the highest Sharpe ratio.
# 
# In the following example, we generate some random data for 5 assets over 100 observations. We define the objective function as the negative Sharpe ratio of the portfolio, and use the constraints that the weights must sum to 1. We also define the bounds as 0 to 1 for each asset, and use a random initial guess. Then, we solve the optimization problem using the SLSQP solver, and print out the optimal portfolio weights and Sharpe ratio.
# 
# to be continued...
