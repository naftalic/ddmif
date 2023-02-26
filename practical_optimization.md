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

Let us consider the following simple Linear Programing Model:

$$
&\text{Maximize}\quad 2x + 3y
&\text{Subject to:}
x + y \le 4\\
x \ge 0\\
y \ge 0\\
$$

To solve this problem using cvxpy, gurobipy, and mosek, we will need to install these libraries first. Here are the installation commands for each library using pip:


Once we have these libraries installed, we can write the code to solve the LP model using each of them.

## Using cvxpy

```{code-cell}
import cvxpy as cp

# Define the variables
x = cp.Variable()
y = cp.Variable()

# Define the objective function
objective = cp.Maximize(2*x + 3*y)

# Define the constraints
constraints = [
    x + y <= 4,
    x >= 0,
    y >= 0
]

# Define the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Print the optimal values of x and y
print("Optimal value of x:", x.value)
print("Optimal value of y:", y.value)
```

