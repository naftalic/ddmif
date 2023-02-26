#!/usr/bin/env python
# coding: utf-8

# # Practical Optimization
# 
# # Simple Linear Programing (LP) model
# Let us consider the following simple Linear Programing (LP) model for a company that produces two products, Product A and Product B:
# 
# Product A requires 2 hours of labor and 3 pounds of material to produce one unit. The company has 80 hours of labor available and 120 pounds of material available.
# Product B requires 3 hours of labor and 2 pounds of material to produce one unit. The company has 60 hours of labor available and 100 pounds of material available.
# The profit for each unit of Product A is \$5, and the profit for each unit of Product B is \$4.
# The objective is to maximize the company's profit subject to the available resources. Let's call the number of units of Product A produced $x_1$ and the number of units of Product B produced $x_2$. Then, the LP model is:
# 
# $$
# \begin{aligned}
# &\text{Maximize } &&5x_1 + 4x_2 \
# &\text{Subject to } &&2x_1 + 3x_2 \le 80 &&\text{(labor constraint for Product A)} \
# &&&3x_1 + 2x_2 \le 60 &&\text{(labor constraint for Product B)} \
# &&&3x_1 + 2x_2 \le 100 &&\text{(material constraint for both products)} \
# &&&x_1, x_2 \ge 0 &&\text{(non-negativity constraint)}
# \end{aligned}
# $$
# 
# Now, let's solve this LP model using cvxpy, gurobipy, and mosek in Python
# 
# ## Using cvxpy

# In[1]:


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


# ## Using gurobipy

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


# ## Using mosek

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
# ## using CVXPY + GUROBI
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


# In this implementation, we first define the problem data, including the binary decision variables, the objective function, and the constraints. We then create a CVXPY problem instance using the cp.Problem constructor, with the objective function and constraints as arguments. We solve the problem using the GUROBI solver by passing solver=cp.GUROBI to the solve method of the problem instance. Finally, we print the results using the value attribute of the objective function and decision variables.
# 
# # Mixed-integer programming problem
# ## using CVXPY + MOSEK

# In[5]:


import cvxpy as cp

# Define problem data
A = [[1, 2], [-1, 1]]
b = [3, 1]

# Define integer decision variables
x = cp.Variable(2, integer=True)

# Define objective function
obj = cp.Minimize(cp.sum_squares(A @ x - b))

# Define the problem
problem = cp.Problem(obj)

# Solve the problem
problem.solve(solver=cp.MOSEK)

# Print results
print("CVXPY + MOSEK Solution:")
print("status:", problem.status)
print("optimal value:", obj.value)
print("optimal x:", x.value)


# In this implementation, we first define the problem data, including the integer decision variables, the objective function, and the constraints. We then create a CVXPY problem instance using the cp.Problem constructor, with the objective function and constraints as arguments. We solve the problem using the MOSEK solver by passing solver=cp.MOSEK to the solve method of the problem instance. Finally, we print the results using the value attribute of the objective function and decision variables.
