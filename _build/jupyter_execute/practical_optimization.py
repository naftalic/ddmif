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
# \begin{align*}
# &\text{Maximize} &5x1 + 4x2 & \\
# &\text{Subject to} &2x1 + 3x2 <= 80   \quad &\text{(labor constraint for Product A)} \\
# & &3x1 + 2x2 <= 60  \quad &\text{(labor constraint for Product B)} \\
# & &3x1 + 2x2 <= 100 \quad &\text{(material constraint for both products)} \\
# & &x1, x2 >= 0      \quad &\text{(non-negativity constraint)}
# \end{align*}
# $$
# 
# Now, let's solve this LP model using cvxpy, gurobipy, and mosek in Python
# 
# # Using cvxpy

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


# # Using gurobipy

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


# # Using mosek

# In[3]:


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


#  
# $$
# \begin{align*}
# &\text{minimize} &x1 + x2 + x3 & \\
# &\text{subject to} &x1 + x2 le 1 \\
# & &x2 + x3 \le 1 \\
# & &x1, x2, x3 \quad\text{are binary variables}
# \end{align*}
# $$
