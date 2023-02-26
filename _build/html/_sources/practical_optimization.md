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
\begin{align*}
&\text{Maximize}\quad &2x + 3y\\
&\text{Subject to:}
&x + y \le 4\\
&&x \ge 0\\
&&y \ge 0\\
\end{align*}
$$

To solve this problem using cvxpy, gurobipy, and mosek, we will need to install these libraries first. Here are the installation commands for each library using pip:


Once we have these libraries installed, we can write the code to solve the LP model using each of them.

## Using CVXPY

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

## Using Gurobipy

```{code-cell}
import gurobipy as gp

# Create a new model
model = gp.Model()

# Define the variables
x = model.addVar(lb=0, name="x")
y = model.addVar(lb=0, name="y")

# Define the objective function
objective = 2*x + 3*y

# Add the objective function to the model
model.setObjective(objective, gp.GRB.MAXIMIZE)

# Add the constraints
model.addConstr(x + y <= 4, "c1")

# Optimize the model
model.optimize()

# Print the optimal values of x and y
print("Optimal value of x:", x.x)
print("Optimal value of y:", y.x)
```
## Using Mosek

```{code-cell}
import mosek

# Create a new optimization task
with mosek.Env() as env:
    with env.Task() as task:
        # Set the optimization sense to maximize
        task.putobjsense(mosek.objsense.maximize)

        # Define the variables
        x_idx = task.appndvars(1)
        y_idx = task.appndvars(1)

        # Define the objective function
        task.putcj(x_idx, 2)
        task.putcj(y_idx, 3)

        # Add the constraints
        task.putconbound(0, mosek.boundkey.up, 4)
        task.putaij(0, x_idx, 1)
        task.putaij(0, y_idx, 1)

        # Optimize the task
        task.optimize()

        # Print the optimal values of x and y
        print("Optimal value of x:", task.getxx(x_idx)[0])
        print("Optimal value of y:", task.getxx(y_idx)[0])
```
