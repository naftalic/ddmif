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

# Practical Optimization
Optimization is a powerful tool that is widely used in practice to solve real-world problems. Optimization problems arise in a variety of fields such as finance, engineering, operations research, and machine learning. These problems often involve decision-making under constraints, where one needs to find the best possible solution given the available resources.

By using optimization techniques, we can identify the optimal solution that satisfies the given constraints and minimizes or maximizes the objective function. This allows us to make better decisions and achieve our desired outcomes more efficiently.

In finance, optimization is used to solve problems such as portfolio optimization, asset allocation, and risk management. In engineering, optimization is used to design and optimize systems such as transportation networks, communication systems, and manufacturing processes. In operations research, optimization is used to solve problems such as production planning, inventory management, and supply chain optimization.

Optimization is also widely used in machine learning to train models and make predictions. In machine learning, optimization techniques are used to find the optimal parameters of a model that best fits the data and minimizes the error.

In this chapter, we will discuss examples of linear programming (LP), binary optimization, and mixed-integer programming (MIP).
We will introduce the widely used optimization libraries such as CVXPY, GurobiPy, and Mosek Fusion that can be used to solve optimization problems effectively. These libraries provide user-friendly interfaces to model and solve optimization problems using a variety of algorithms and solvers.

First, we will discuss LP, which is a technique to optimize a linear objective function subject to linear constraints. 
Next, we will cover binary optimization, which involves decision-making in scenarios where the variables can only take binary values of 0 or 1. 
Lastly, we will delve into mixed-integer programming, which involves optimization problems where some or all of the variables can take both continuous and discrete values.

# Simple Linear Programing model
Let's consider a simple example of a company that produces two products, Product A and Product B, to illustrate the usefulness of optimization in practice.

To produce one unit of Product A, the company requires 2 hours of labor and 3 pounds of material. The company has 80 hours of labor available and 120 pounds of material available. To produce one unit of Product B, the company requires 3 hours of labor and 2 pounds of material. The company has 60 hours of labor available and 100 pounds of material available. The profit for each unit of Product A is \$5, and the profit for each unit of Product B is \$4. The objective is to maximize the company's profit subject to the available resources.

Optimization is useful in practice because it helps us make better decisions by finding the best possible solution to a problem given certain constraints. In this case, the LP model helps us determine the optimal number of units of Product A and Product B that the company should produce to maximize its profit while staying within the available resources.

Let's call the number of units of Product A produced $x_1$ and the number of units of Product B produced $x_2$. Then, the LP model is:

$$
\begin{aligned}
&\text{Maximize } &&5x_1 + 4x_2 \\
&\text{Subject to } &&2x_1 + 3x_2 \le 80 &&\text{(labor constraint for Product A)} \\
&&&3x_1 + 2x_2 \le 60 &&\text{(labor constraint for Product B)} \\
&&&3x_1 + 2x_2 \le 100 &&\text{(material constraint for both products)} \\
&&&x_1, x_2 \ge 0 &&\text{(non-negativity constraint)}
\end{aligned}
$$

We can use various optimization solvers such as CVXPY, GUROBIPY, and MOSEK in Python to solve this LP model and find the optimal solution.

## Using CVXPY

```{code-cell}
import cvxpy as cp

x = cp.Variable(2, nonneg=True)
objective = cp.Maximize(5*x[0] + 4*x[1])
constraints = [2*x[0] + 3*x[1] <= 80,
               3*x[0] + 2*x[1] <= 60,
               3*x[0] + 2*x[1] <= 100]
prob = cp.Problem(objective, constraints)
prob.solve()

print("Optimal value:", prob.value)
print("Optimal solution:", x.value)
```

## Using GUROBIPY

```{code-cell}
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
```

## Using MOSEK
```{code-cell}
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
```    

# Binary optimization problem 
In optimization, one of the most common types of problems is the Mixed Integer Programming (MIP) problem. This is a mathematical optimization problem where some of the variables are restricted to be integers. Binary Optimization, where the variables can only take on values of 0 or 1, is a special case of MIP.

In this context, we will solve a binary optimization problem using CVXPY and GUROBI. The problem is to minimize the objective function $x_1 + x_2 + x_3$, subject to the constraints $x_1 + x_2 \ge 2$, $x_2 + x_3 \le 1$, and $x_1, x_2, x_3$ are binary variables. 

## Using CVXPY + GUROBI
$$
\begin{aligned}
&\text{minimize } &&x_1 + x_2 + x_3 \\
&\text{subject to } &&x_1 + x_2 \ge 2 \\
&&&x_2 + x_3 \le 1 \\
&&&x_1, x_2, x_3 \text{ are binary variables}
\end{aligned}
$$ 

```{code-cell}
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
```

# Mixed-integer programming problem
In many real-world problems, we encounter situations where decision variables must take on integer values. For example, in production planning, the number of items produced must be an integer value. MIP provides a way to find optimal solutions to these types of problems.

In this example, we will solve a very simple MIP problem using CVXPY and MOSEK solver. Suppose we want to maximize the following objective function:

$$
\begin{aligned}
&\text{maximize } &&3x_1 + 2x_2 \\
&\text{subject to } &&x_1 + x_2 \leq 4 \\
&&&x_1, x_2 \in \mathbb{Z}, \text{ where $\mathbb{Z}$ denotes the set of integers}
\end{aligned}
$$ 

Here, we want to find integer values for $x_1$ and $x_2$ that satisfy the constraints and maximize the objective function. This is a very simple example, but it can help us understand the basic syntax and structure of solving MIP problems using cvxpy.

## Using CVXPY + MOSEK
```{code-cell}
import cvxpy as cp
import mosek

# Define the variables
x1 = cp.Variable(integer=True)
x2 = cp.Variable(integer=True)

# Define the objective function
obj = cp.Maximize(3*x1 + 2*x2)

# Define the constraints
constr = [x1 + x2 <= 4]

# Create the problem instance and solve it
prob = cp.Problem(obj, constr)
prob.solve(solver=cp.MOSEK)

# Print the optimal solution and optimal value
print("Optimal solution: x1 = {}, x2 = {}".format(x1.value, x2.value))
print("Optimal value: {}".format(prob.value))
```
