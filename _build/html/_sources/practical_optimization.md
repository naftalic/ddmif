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

# Simple Linear Programing (LP) model
Let us consider the following simple Linear Programing (LP) model for a company that produces two products, Product A and Product B:

Product A requires 2 hours of labor and 3 pounds of material to produce one unit. The company has 80 hours of labor available and 120 pounds of material available.
Product B requires 3 hours of labor and 2 pounds of material to produce one unit. The company has 60 hours of labor available and 100 pounds of material available.
The profit for each unit of Product A is \$5, and the profit for each unit of Product B is \$4.
The objective is to maximize the company's profit subject to the available resources. Let's call the number of units of Product A produced $x_1$ and the number of units of Product B produced $x_2$. Then, the LP model is:

$$
\begin{align*}
&\text{Maximize} &5x1 + 4x2 & \\
&\text{Subject to} &2x1 + 3x2 <= 80   \quad &\text{(labor constraint for Product A)} \\
& &3x1 + 2x2 <= 60  \quad &\text{(labor constraint for Product B)} \\
& &3x1 + 2x2 <= 100 \quad &\text{(material constraint for both products)} \\
& &x1, x2 >= 0      \quad &\text{(non-negativity constraint)}
\end{align*}
$$

Now, let's solve this LP model using cvxpy, gurobipy, and mosek in Python

## Using cvxpy

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

## Using gurobipy

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

## Using mosek
```{code-cell}
import mosek.fusion as mf

# Create a Mosek Fusion environment
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
$$
\begin{align*}
&\text{minimize} &x1 + x2 + x3 & \\
&\text{subject to} &x1 + x2 > 1 \\
& & x2 + x3 \le 1 \\
& & x1, x2, x3 \quad\text{are binary variables}
\end{align*}
$$ 

```{code-cell}
import cvxpy as cp

# Define problem data
A = [[1, 1, 0], [0, 1, 1]]
b = [1, 1]

# Define binary decision variables
x = cp.Variable(3, boolean=True)

# Define objective function
obj = cp.sum(x)

# Define constraints
constraints = [A[i] @ x > b[i] for i in range(len(b))]
constraints.append(x[0] >= 0) # x1 is binary
constraints.append(x[1] >= 0) # x2 is binary
constraints.append(x[2] >= 0) # x3 is binary

# Define problem instance and solve it
prob = cp.Problem(cp.Minimize(obj), constraints)
prob.solve(solver=cp.MOSEK)

# Print results
print("CVXPY Solution:")
print("status:", prob.status)
print("optimal value:", prob.value)
print("optimal x:", x.value)
```

```{code-cell}
import gurobipy as gp

# Define problem data
A = [[1, 1, 0], [0, 1, 1]]
b = [1, 1]

# Create a new optimization model
model = gp.Model("binary_optimization")

# Define binary decision variables
x = model.addVars(3, vtype=gp.GRB.BINARY, name="x")

# Define objective function
obj = gp.quicksum(x[i] for i in range(len(x)))
model.setObjective(obj, gp.GRB.MINIMIZE)

# Define constraints
for i in range(len(b)):
    model.addConstr(A[i] @ [x[i] for i in range(len(x))] > b[i])

# Solve problem
model.optimize()

# Print results
print("Gurobi Solution:")
print("status:", model.Status)
print("optimal value:", model.ObjVal)
print("optimal x:", [x[i].X for i in range(len(x))])
```

```{code-cell}
import mosek.fusion as mf

# Define problem data
A = [[1, 1, 0], [0, 1, 1]]
b = [1, 1]

# Create a new Fusion environment
env = mf.Env()

# Create a new Fusion model
with env:
    # Define binary decision variables
    x = env.variable(3, vtype=mf.VariableType.Binary)

    # Define objective function
    obj = env.sum(x)

    # Define constraints
    for i in range(len(b)):
        env.constraint(A[i] @ x, mf.ConstraintType.Greater, b[i])

    # Create a new Fusion problem instance
    task = env.problem("Binary Optimization")

    # Set the objective and constraints
    task.objective(obj, mf.ObjectiveSense.Minimize)
    task.constraints.addAll(env.getConstraints())

    # Solve the problem
    task.solve()

    # Print results
    print("Mosek Fusion Solution:")
    print("status:", task.getProblemStatus(mosek.streamtype.msg))
    print("optimal value:", obj.level())
    print("optimal x:", x.level())
```
