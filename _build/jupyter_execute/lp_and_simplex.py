#!/usr/bin/env python
# coding: utf-8

# # A2) Theory of Linear Programing and the Simplex Method
# 
# In this section, we will discuss the theory of linear programming and the simplex method. Linear programming is a mathematical technique used to optimize a linear objective function subject to linear equality and inequality constraints. The simplex method is an algorithm used to solve linear programming problems.
# 
# To begin, let us consider the **primal-dual theory** with a few examples. The primal-dual theory states that every linear programming problem has a dual problem, and the optimal values of the primal and dual problems are equal.
# 
# Now, let's look at an example linear programming problem:
# 
# $$
# \begin{aligned}
# &\text{max}&&\\
# &\qquad z=40𝑥_1 + 50𝑥_2\\
# &\text{subject to}&&\\
# &\qquad 1x_1 + 2𝑥_2 \le 40\\
# &\qquad 4𝑥_1 + 3𝑥_2 \le 120\\
# &\qquad x_1, x_2 \ge 0.\\
# \end{aligned} 
# $$

# In[1]:


from gurobipy import *
m = Model()
m.setParam('OutputFlag', 0)

x1 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name='x1') 
x2 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name='x2')
m.setObjective(40*x1+50*x2, GRB.MAXIMIZE)
m.addConstr(1*x1+2*x2<=40, name='c1')
m.addConstr(4*x1+3*x2<=120, name= 'c2')
m.optimize()
print('*'*100)
for var in m.getVars(): # descision variable
    print(var.varName, '=', var.x, (var.obj,var.SAObjLow, var.SAObjUp, var.RC))
print('*'*100)
print('optimal total revenue:', m.objVal)
print('*'*100)
for con in m.getConstrs(): # constraints
    print(con.ConstrName, ': slack =', con.slack,', shadow price=',
          con.pi,',', (con.RHS, con.SARHSLow, con.SARHSUp))
print('*'*100)
print('*'*100)


# The optimal solution to the linear programming problem is given by
# 
# $$
# (x^*,z)=((24,8),1360).
# $$
# 
# The Gurobi output also shows the sensitivity analysis results for the problem:
# 
# $$
# \begin{aligned}
# \qquad c_1 &= 40~(25, 66.667),\\
# \qquad c_2 &= 50~(30, 80),\\
# \qquad b_1 &= 40~(30, 80),~\text{with shadow price } 16, \\
# \qquad b_2 &= 120~(60, 160),~\text{with shadow price } 6,\\
# \qquad s_1 &= 0, \\
# \qquad s_2 &= 0. \\
# \end{aligned}
# $$
# 
# * The cost coefficients, $c_1$ and $c_2$, have values of 40 and 50, respectively. The ranges in which they are allowed to change without affecting the optimal solution are $(25, 66.667)$ and $(25, 66.667)$, respectively.
# * The right-hand side values of the constraints, $b_1$ and $b_2$, have values of 40 and 120, respectively. They can change to within the values $(30, 80)$ and $(60, 160)$, respectively, without affecting the optimal solution mix.
# * The shadow prices of the constraints are 16 and 6 for $b_1$ and $b_2$, respectively. (The shadow price is the change in the optimal objective value of the linear program per unit increase in the right-hand side of a constraint.)
# * There is no slack in either constraint. (Slack variables are non-negative variables that are introduced to convert inequalities into equations.)
# 
# **Can we infer the optimal value of $z$, or at least bound its value, without solving the LP model?** 
# 
# One way to do this is by using the first constraint and the fact that both decision variables are non-negative. The objective function is $40𝑥_1 + 50𝑥_2$, which can be bounded as follows:
# 
# $$
# 40𝑥_1 + 50𝑥_2<=40\times(x_1 + 2𝑥_2)=40x_1 + 80𝑥_2\le 1600.
# $$
# 
# Therefore, the optimal value of $z$ must be less than or equal to 1600.
# 
# Is it possible to obtain a tighter bound on the optimal value of $z$? We can use the second constraint to derive another bound:
# 
# $$
# 40𝑥_1 + 50𝑥_2<=50/3\times(4𝑥_1 + 3𝑥_2)=66.67x_1 + 50𝑥_2=2000
# $$
# 
# However, this bound is actually looser than the previous bound we obtained using the first constraint, which was 1600. Therefore, using the second constraint does not provide a better bound in this case.
# 
# Systematically, we can write:
# 
# $$
# 40𝑥_1 + 50𝑥_2\le d_1x_1 +d_2x_2 \le h,
# $$
# 
# where $h$ is an upper bound on the maximum of the objective. To infer $d_1$, $d_2$, and $h$, we can multiply the first constraint by $v_1\ge0$, the second by $v_2\ge0$, and then add the two:
# 
# $$
# v_1(1x_1 + 2𝑥_2)+v_2(4𝑥_1 + 3𝑥_2)\le 40v_1+120v_2
# $$
# 
# which gives us:
# 
# $$
# (v_1+4v_2)x_1+(2v_2+3v_2)x_2\le 40v_1+120v_2.
# $$
# 
# Therefore, we can infer that:
# 
# $$
# \begin{aligned}
# &d_1=v_1+4v_2, \\
# &d_2=2v_2+3v_2,\qquad \text{and}\\
# &h=40v_1+120v_2.
# \end{aligned}
# $$ 
# 
# How can we determine the best coefficients $v_1$ and $v_2$? We must ensure that $d_1\geq 40$ and $d_2\geq 50$, and we want $h$ to be as **small** as possible while satisfying these constraints. This is an LP model called the **dual** of the primal problem:
# 
# $$
# \begin{aligned}
# &\text{min}\\
# &\qquad h=40v_1 + 120v_2\\
# &\text{s.t.}\\
# &\qquad 1v_1 + 4v_2 \ge 40\\
# &\qquad 2v_1 + 3v_2 \ge 50\\
# &\qquad v_1, v_2 \ge 0.
# \end{aligned} 
# $$
# 
# In general, the dual of a primal LP is another LP that is obtained by interchanging the roles of variables and constraints, and changing the objective from maximizing to minimizing, or vice versa. Specifically, if the primal problem is:
# 
# $$
# \begin{aligned}
# &\max \\
# &\qquad\mathbf c\cdot\mathbf x,\\
# &\text{s.t.}\\
# &\qquad\mathbf A\mathbf x\le \mathbf b,\\
# &\qquad\mathbf x \ge 0,
# \end{aligned}
# $$ 
# 
# then the dual problem is:
# 
# $$
# \begin{aligned}
# &\min \\
# &\qquad\mathbf b\cdot\mathbf v,\\
# &\text{s.t.}\\
# &\qquad\mathbf A^T\mathbf v\ge \mathbf c,\\
# &\qquad\mathbf v\ge 0.
# \end{aligned}
# $$ 
# 
# The interpretation is that we solve for $\mathbf v$, the shadow prices of the primal, by constraining the shadow prices with the cost coefficients, $\mathbf c$. 
# The dual LP provides a lower bound on the optimal value of the primal LP.
# 
# To determine the optimal values of $v_1$ and $v_2$, we can solve the dual LP using Python or other LP solvers. For this problem, the optimal values are:
# 
# $$
# (v^*,h)=((16,6),1360).
# $$
# 
# Therefore, we can use $d_1=16+4\cdot 6=40$, $d_2=2\cdot 16+3\cdot 6=50$, and $h=1360$ as the optimal coefficients and upper bound for the primal LP.

# In[2]:


m = Model()    
m.setParam('OutputFlag', 0)

x1 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name='v1') 
x2 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name='v2')
m.setObjective(40*x1+120*x2, GRB.MINIMIZE)
m.addConstr(1*x1+4*x2>=40, name='c1')
m.addConstr(2*x1+3*x2>=50, name= 'c2')
m.optimize()
print('*'*100)
for var in m.getVars(): # descision variable
    print(var.varName, '=', var.x, (var.obj,var.SAObjLow, var.SAObjUp, var.RC))
print('*'*100)
print('optimal total revenue:', m.objVal)
print('*'*100)
for con in m.getConstrs(): # constraints
    print(con.ConstrName, ': slack =', con.slack,', shadow price=',
          con.pi,',', (con.RHS, con.SARHSLow, con.SARHSUp))


# Furthermore, as demonstrated earlier,
# 
# $$
# \begin{aligned}
# \qquad b_1 &= 40~(30,80),\\
# \qquad b_2 &= 120~(60,160),\\
# \qquad c_1 &= 40~(25, 66.667),~\text{with shadow price } 24, \\
# \qquad c_2 &= 50~(30, 80),~\text{with shadow price } 8,\\
# \qquad s_1 &= 0, \\
# \qquad s_2 &= 0. \\
# \end{aligned}
# $$
# 
# The primal's shadow prices are the dual's decision variables, and the dual's $\mathbf b$ and $\mathbf c$ correspond to the primal's values. Moreover, the dual's shadow prices are the primal's decision variables.
# 
# The primal-dual relationship provides us with additional flexibility in solving LP models. When the dual is simpler, we can solve it instead of the primal.
# 
# Few other properties emerge from the primal-dual relationship:
# 
# # Weak duality
# Weak duality refers to the fundamental property of linear programming that the optimal value of the dual problem is always less than or equal to the optimal value of the primal problem. In other words, the dual objective function provides a natural lower bound for the primal objective function.
# 
# To see this, consider the difference between the primal and dual objectives:
# 
# $$
# \mathbf c\cdot \mathbf x-\mathbf v\cdot \mathbf b. 
# $$
# 
# Expanding this equation by adding and subtracting $\mathbf v\cdot\mathbf A\mathbf x$, we have:
# 
# $$
# \begin{aligned}
# &\qquad \mathbf c\cdot \mathbf x-\mathbf v\cdot \mathbf b=\\
# &\qquad \mathbf c\cdot \mathbf x-\mathbf v\cdot\mathbf A\mathbf x+ \mathbf v\cdot\mathbf A\mathbf x-\mathbf v\cdot \mathbf b =\\
# &\qquad (\mathbf c-\mathbf v\mathbf A)\cdot\mathbf x+ \mathbf v\cdot(\mathbf A\mathbf x- \mathbf b).\\
# \end{aligned}
# $$
# 
# Since $\mathbf A\mathbf x\le \mathbf b$ for the primal and $\mathbf c-\mathbf v\mathbf A\le0$ for the dual, we have that 
# 
# $$
# \mathbf c\cdot \mathbf x-\mathbf v\cdot \mathbf b \le 0.
# $$
# 
# Therefore, the optimal value of the dual problem, $\mathbf v\cdot \mathbf b$, provides a lower bound for the optimal value of the primal problem, $\mathbf c\cdot \mathbf x$.
# 
# Note that this holds true for both maximizing and minimizing problems.
# 
# # Complementary slackness
# Complementary slackness is a fundamental concept in linear programming that links the primal and dual problems' optimal solutions. Specifically, it states that when a constraint is binding (i.e., its slack is zero) in the primal problem, the corresponding dual variable must be positive, and vice versa. This implies that the product of the primal and dual variables associated with each constraint is zero.
# 
# For a feasible solution $(\mathbf x, \mathbf v)$ to the primal-dual pair, the complementary slackness conditions are:
# 
# $$
# \begin{aligned}
# &(\mathbf c-\mathbf v\mathbf A)\cdot \mathbf x=0 \quad\text{(primal complementary slackness)},\\
# &\text{and}\\
# &\mathbf v\cdot (\mathbf A\mathbf x- \mathbf b)=0 \quad\text{(dual complementary slackness)}.\\
# \end{aligned}
# $$
# 
# The primal-dual value equality theorem further states that the optimal objective values of the primal and dual problems are equal:
# 
# $$
# \qquad \mathbf c^T \mathbf x^* = \mathbf b^T \mathbf v^* \quad\text{(primal-dual value equality)}.
# $$
# 
# Therefore, if the primal problem is a maximization problem, the optimal value of the primal problem is equal to the optimal value of the dual problem, which is a minimization problem. In the given example, we can verify that:
# 
# $$
# \mathbf c^T \mathbf x^* = (40,50)\cdot (24,8)=1360,
# $$
# 
# and 
# 
# $$
# \mathbf b^T \mathbf v^* = (40,120)\cdot (16,6)=1360
# $$
# 
# confirming the primal-dual value equality theorem.
# 
# # KKT conditions for optimality
# 
# The Karush-Kuhn-Tucker (KKT) conditions are necessary and sufficient conditions for linear programming (LP) optimality. To maximize the objective $\mathbf c^T \mathbf x$, the following conditions must be satisfied:
# 
# Primal feasibility:
# 
# $$
# \begin{aligned}
# &\mathbf A\mathbf x\le \mathbf b\\
# &\mathbf x\ge 0
# \end{aligned}
# $$
# 
# Dual feasibility:
# 
# $$
# \begin{aligned}
# &\mathbf A^T\mathbf v\ge \mathbf c\\
# &\mathbf v\ge 0
# \end{aligned}
# $$
# 
# Complementary slackness:
# 
# $$
# \begin{aligned}
# &(\mathbf c-\mathbf A^T\mathbf v)\mathbf x=0\\
# &\mathbf v^T(\mathbf A \mathbf x- \mathbf b)=0.
# \end{aligned}
# $$
# 
# These conditions ensure that the primal and dual solutions are feasible and that the primal and dual objectives are equal at the optimal point. Additionally, the complementary slackness condition requires that if a constraint in the primal problem is binding (i.e., its slack is zero), then the corresponding dual variable must be positive, and vice versa. This condition implies that the product of the primal and dual variables associated with each constraint is zero.
# 
# Overall, the KKT conditions are used to determine the optimal solution for a linear programming problem.
# 
# # Improving search
# If $\mathbf x$ is feasible, the goal is to *improve* the solution from $\mathbf x^{(t)}$ to $\mathbf x^{(t+1)}$ via
# 
# $$
# \mathbf x^{(t+1)}=\mathbf x^{(t)}+\lambda \Delta \mathbf x, \quad\text{with}\quad\lambda >0
# $$
# 
# where $\lambda$ is the step size and $\Delta \mathbf x$ is the direction.
# 
# *Improve direction* means that $\mathbf x^{(t+1)}=\mathbf x^{(t)}+\lambda \Delta \mathbf x$ is better than $\mathbf x^{(t)}$ for all $\lambda>0$ sufficiently small.
# 
# $\Delta \mathbf x$ is a *feasible direction* if $\mathbf x^{(t)}+\lambda \Delta \mathbf x$ is feasible for all $\lambda>0$ sufficiently small. 
# 
# The objective $z$ is $\max z=\mathbf c^T\mathbf x$. So, 
# 
# $$
# \mathbf c^T\mathbf x^{(t+1)}=\mathbf c^T\mathbf x^{(t)}+\lambda \mathbf c^T\Delta \mathbf x.
# $$
# 
# If $\mathbf c=\Delta x$, then 
# 
# $$
# \lambda \mathbf c^T\Delta \mathbf x=\lambda (\Delta \mathbf x)^2\ge 0
# $$ 
# 
# which always improve ($\Delta x\ne 0$) for maximize objective function at any feasible point.
# 
# Feasible set of points is convex if any line segment between pair of feasible points fall entirely within the feasible region. I.e., line segment between $x^{(1)}$ and $x^{(2)}$ consists of all points along $x^{(1)}+\lambda (x^{(2)}-x^{(1)})$ with $0\le\lambda\le 1$.
# Hence, discrete feasible sets are NOT convex. 
# 
# If the feasible set is convex, then there is *always* an improve direction. I.e., 
# 
# $$
# \mathbf c\cdot (\mathbf x^{(t+1)}-\mathbf x^{(t)})=\lambda \mathbf c\cdot\Delta\mathbf x=\lambda(\Delta\mathbf x)^2\ge 0,
# $$
# 
# unless $\mathbf x^{(t+1)}=\mathbf x^{(t)}=\mathbf x^*$. In that case, $\mathbf x^*$ is the local max which is equal to the global max and the solution cannot improve.
# 
# If all constraints are linear, their feasible is convex:
# 
# $$
# \mathbf A \mathbf x^{(1)}\ge b,~~~ \text{and}\quad\mathbf A \mathbf x^{(2)}\ge b.
# $$
# 
# Then,
# 
# $$
# \lambda\mathbf A \mathbf x^{(2)}+(1-\lambda)\mathbf A \mathbf x^{(1)}\ge \lambda\mathbf b+(1-\lambda)\mathbf b=\mathbf b
# $$
# 
# and 
# 
# $$
# \mathbf A [\mathbf x^{(1)}+\lambda(\mathbf x^{(2)}-\mathbf x^{(1)})]\ge b
# $$
# 
# which means that points along $\mathbf x^{(1)}$ and $\mathbf x^{(2)}$ are feasible and convex.
# 
# In LP over continuance variables w/ linear constraints and objective, the set of feasible points is convex, and the solution will stop improving at local $=$ global maxima. Feasible sets of linear programs are called polyhedral and are convex.
# 
# Boundary point is defined s.t. at least one inequality becomes equality (or active) at that point. Else it is called an interior point.
# 
# Unless the objective is constant, every optimal point to an LP will occur at a boundary point of its feasible region. 
# 
# Why?
# 
# If all inequalities are strict, we can take a small step in ALL directions from the interior point without losing feasibility. Then,  $\mathbf c=\Delta x$ will always improve the maximize problem. Hence, no interior point can be optimal.
# 
# Unique optimal must be an extreme point. 
# 
# Why? 
# 
# Consider optimal $\mathbf x^*$ for the maximize problem $\mathbf c^T\mathbf x$. If $\mathbf x^*$ is NOT extreme of the feasible, then it must be the weighted average of two other feasible solutions $\mathbf x^{(1)}$ and $\mathbf x^{(2)}$. That is 
# 
# $$
# \mathbf x^*=(1-\lambda)\mathbf x^{(1)}+\lambda \mathbf x^{(2)},\quad 0\lt\lambda\gt1
# $$
# 
# and
# 
# $$
# \mathbf c\cdot\mathbf x^*=(1-\lambda)\mathbf c\cdot\mathbf x^{(1)}+\lambda \mathbf c\cdot\mathbf x^{(2)}.
# $$
# 
# If the objective of the two endpoints differs, their average $\mathbf c\cdot\mathbf x^*$ must be lower than the higher, and thus $\mathbf x^*$ is not optimal. If the two endpoints are equal, there are multiple optimal and $\mathbf x^*$ is not unique. We conclude that the LP solution can be unique only if it is an extreme point of the feasible. If LP has any optimal solution, it follows that it has one at an extreme point of its feasible.
# 
# # A few remarks:
# 
# 1.  Ratio constraints as $x_1/x_2\le2/3$
# can be "linearized" to
# $3x_1-2x_2\le0.$
# 
# 2. Decision variables of relatively large magnitude are best modeled as continuance variables even though they correspond physically to integer quantities.
# 
# 3. We can also linearize nonlinear constraints. In an example, *minimax* or *min-deviation* operators.
# 
# Minmax:
# 
# $$
# \begin{aligned}
# &\quad\text{min}\\
# &\quad\quad f\\
# &\quad\text{s.t.} \\
# &\quad \quad f\ge 3x_1+2x_2+x_3\\
# &\quad \quad  f\ge x_1+x_2.\\
# \end{aligned}
# $$
# 
# Min deviation:
# 
# $$
# \begin{aligned}
# &\quad\text{min}\\
# &\quad\quad 4|x_1-x_2|\\
# \\
# &\text{which is replaced with}\\
# \\
# &\quad\text{min}\\
# &\quad\quad 4(s_1^++s_1^-)\quad(\text{total deviation})\\
# &\quad\text{s.t.}\\
# &\quad\quad x_1-x_2=s_1^+-s_1^-\\
# &\quad\quad s_1^+,s_1^-\ge0
# \end{aligned}
# $$
# 
# # The Simplex Algorithm
# 
# The algorithm is designed to improve the solution by moving from an extreme point to another adjacent while retaining feasibility.
# 
# Consider the following standard LP model of the Factory probelm with $x_1$, $x_2$ decision varibales and $x_3$, $x_4$ slack varibales:
# 
# $$
# \begin{aligned}
# &\quad\text{max}\\
# &\quad\quad z=40x_1+50x_2\\
# &\quad\text{s.t.}\\
# &\quad\quad x_1+2x_2+x_3=40\\
# &\quad\quad 4x_1+3x_2+x_4=120\\
# &\quad\quad x_1,x_2,x_3,x_4\ge0
# \end{aligned}
# $$
# 
# Then, we insert the input parameters, $\mathbf A$, $\mathbf b$, and $\mathbf c$, into a tabular format  
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\                   
# \end{array}
# $$
# 
# Now, to begin, we choose an initial solution which is unique and feasible. For that we set $(x_1, x_2) = (0,0)$, which leave use with $(x_3, x_4) = (40,120)$. We call the active nonzero varibales basic feasible (B) and the others nonbasic feasible (N). Hence, the initial solution at $t=0$ is $\mathbf{x}^{(0)}=(0,0,40,120)$, and the current objective is $\mathbf c^T \mathbf x^{(0)}=0$. Note that basic solutions exists only if the columns form a basis - the largest possible collection of linearily independent columns.
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\
# t=0       & N & N  & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 40 & 120 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\                    
# \end{array}
# $$
# 
# The goal is to improve the objective. For that we need to find the "best" improve direction $\Delta \mathbf{x}$ and step size $\lambda$ while maintaining feasability: $\mathbf{x}^{(t+1)}=\mathbf{x}^{(t)}+\lambda \Delta \mathbf{x}$.
# 
# The constraints equations are $\mathbf A\mathbf{x}^{(t)}=\mathbf{b}$. So, if the improved $\mathbf{x}^{(t+1)}$ is feasible than $\mathbf A\mathbf{x}^{(t+1)}=\mathbf{b}$, or $\mathbf A(\mathbf{x}^{(t)}+\lambda \Delta \mathbf{x})=\mathbf{b}$. Subtracting the two
# 
# $$
# \mathbf A(\mathbf{x}^{(t)}+\lambda \Delta \mathbf{x})-\mathbf A\mathbf{x}^{(t)}=\mathbf{b}-\mathbf{b}=0.
# $$
# 
# It follows that
# 
# $$
# \mathbf A \Delta \mathbf{x}=0.
# $$
# 
# In our example,
# 
# $$
# \begin{pmatrix}
# 1 & 2 & 1 & 0 \\
# 4 & 3 & 0 & 1
# \end{pmatrix}
# \begin{pmatrix}
# \Delta x_1 \\
# \Delta x_2 \\
# \Delta x_3 \\
# \Delta x_4
# \end{pmatrix}=0.
# $$
# 
# We want to switch one nonbasic variable with one basic to move to the adjacent edge without losing uniqueness and feasibility. For that, we set $\Delta x_1,\Delta x_2=(1,0)$ and also  $\Delta x_1,\Delta x_2=(0,1)$ (Don't think too much on the meaning of $\Delta x=1$ as this value gets scaled out later when multiplying by $\lambda$ that has $\Delta x$ on its denominator). Solving for the former
# 
# $$
# \begin{pmatrix}
# 1 & 2 & 1 & 0 \\
# 4 & 3 & 0 & 1
# \end{pmatrix}
# \begin{pmatrix}
# 1 \\
# 0 \\
# \Delta x_3 \\
# \Delta x_4
# \end{pmatrix}=0\Rightarrow \Delta \mathbf{x}^T=(1,0,-1,-4),
# $$
# 
# and for the latter we find that
# 
# $$
# \begin{pmatrix}
# 1 & 2 & 1 & 0 \\
# 4 & 3 & 0 & 1
# \end{pmatrix}
# \begin{pmatrix}
# 0 \\
# 1 \\
# \Delta x_3 \\
# \Delta x_4
# \end{pmatrix}=0\Rightarrow \Delta \mathbf{x}^T=(0,1,-2,-3).
# $$
# 
# The corresponding change to the objective $\mathbf c^T \Delta \mathbf{x}$ yield values of 40 and 50 which leads us to prefer the higher value of 50 that goes with $\Delta \mathbf{x}^T=(1,0,-1,-4)$.
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\
# t=0       & N & N  & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 40 & 120 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=40\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & -2 & -3 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{50}\\                 
# \end{array}
# $$
# 
# Now, we need to choose the improved step, $\lambda$, s.t. feasibility will be maintained. 
# 
# The improved solution must maintain the non-negativity constraint
# 
# $$
# \mathbf{x}^{(t+1)}=\mathbf{x}^{(t)}+\lambda \Delta \mathbf{x}\ge 0.
# $$
# 
# Hence, 
# 
# $$
# \lambda \ge -\mathbf{x}^{(t)}/\Delta \mathbf{x}.
# $$
# 
# In addition, $\lambda$ must be non-negative and sufficiently small not to take the improved solution outside of the feasible region. Hence,
# 
# $$
# \lambda=\text{min}\{-\frac{x_j}{\Delta  x_j}: \Delta x_j\le 0\}
# $$
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\
# t=0       & N & N  & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 40 & 120 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=40\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & -2 & -3 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{50}\\                 
# \lambda & 0 & 1  & \boxed{20} & 40 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\  
# \end{array}
# $$
# 
# Hence, 
# 
# $$
# \mathbf{x}^{(1)}=(0,0,40,120)^T+20\times (0,1,-2,-3)^T=(0,20,0,60)^T
# $$
# 
# with the obective $\mathbf c^T \mathbf x^{(1)}=1000$. 
# 
# The process then continues with $x_2$ replacing $x_3$ as basic variable.
# 
# Now, we are looking for an improved solution. For that, we solve for the improved direction and step. We start by solving $\Delta x$ for $x_1$ and $x_3$ to replace the current basic variables. This is done as before, resulting in the best improvement direction using $\Delta\mathbf x$ for $x_1$ with the largest change to the objective. The minimal step turns out to be $\lambda=24$, and hence
# 
# $$
# \mathbf{x}^{(2)}=(0,20,0,60)^T+24(1,-1/2,0,-5/2)^T=(24,8,0,0)
# $$
# 
# with the obective $\mathbf c^T \mathbf x^{(2)}=1360$. 
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\
# t=0       & N & N  & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 40 & 120 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=40\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & -2 & -3 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{50}\\                 
# \lambda &  &   & \boxed{20} & 40 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# --- 
# 
# $$
# \begin{array}{lccccl}
# t=1       & N & B  & N & B & \\
# \mathbf{x}^{(1)} & 0 & 20  & 0 & 60 & \text{Current objective}: \mathbf c^T \mathbf x^{(1)}=1000\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & -1/2  & 0 & -5/2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{15}\\ 
# \Delta\mathbf x ~\text{for}~  x_3 & 0 & -1/2  & 1 & 3/2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-25<0\\                 
# \lambda &  & 40  &  & \boxed{24} & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# Again, we are looking for an improved solution by solving for the improved direction and step. We solve $\Delta x$ for $x_3$ and $x_4$ to replace the current basic variables $x_1$ and $x_2$. This is done as before, resulting in the best improvement direction using $\Delta\mathbf x$ for $x_4$ with the largest change to the objective. But, the minimal step turns out to be negative, and thus the search stops. The local optimum is global because it is an LP model over continuance variables and convex domain. $\mathbf{x}^*=\mathbf{x}^{(2)}$ is optimal with max objective of $1360$.
# 
# $$
# \begin{array}{lccccl}
# & x_1 & x_2 & x_3 & x_4 &\\
# \mathbf c & 40 & 50 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 2  & 1 & 0 & 40\\
#           & 4 & 3  & 0 & 1 & 120\\
# t=0       & N & N  & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 40 & 120 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=40\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & -2 & -3 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{50}\\                 
# \lambda &  &   & \boxed{20} & 40 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# --- 
# 
# $$
# \begin{array}{lccccl}
# t=1       & N & B  & N & B & \\
# \mathbf{x}^{(1)} & 0 & 20  & 0 & 60 & \text{Current objective}: \mathbf c^T \mathbf x^{(1)}=1000\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & -1/2  & 0 & -5/2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{15}\\ 
# \Delta\mathbf x ~\text{for}~  x_3 & 0 & -1/2  & 1 & 3/2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-25<0\\                 
# \lambda &  & 40  &  & \boxed{24} & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# --- 
# 
# $$
# \begin{array}{lccccl}
# t=2       & B & B  & N & N & \\
# \boxed{\mathbf{x}^{(2)}} & 24 & 8  & 0 & 0 & \text{Current objective}: \mathbf c^T \mathbf x^{(1)}=1360\\    
# \Delta\mathbf x ~\text{for}~  x_3 & 3 & -4  & 1 & 0 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-80<0\\ 
# \Delta\mathbf x ~\text{for}~  x_4 & 1/5 & 1/10  & 0 & 1 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{13}\\                 
# \lambda &  &   &  &  & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# # Top Brass Trophy 
# 
# As for another example for solving a LP using the Simplex, we will solve the Top Brass Trophy problem from Chapter 5 in Rardin's book: "Optimization in Operations Research."
# 
# Solve the folowing LP problem using the Simplex method:
# 
# $$
# \begin{aligned}
# &\quad\text{max}\\
# &\quad\quad z=12x_1+9x_2\\
# &\quad\text{s.t.}\\
# &\quad\quad x_1 \le 1000\\
# &\quad\quad x_2 \le 1500\\
# &\quad\quad x_1+x_2 \le 1750\\
# &\quad\quad 4x_1+2x_2 \le 4800\\
# &\quad\quad x_1,x_2\ge0
# \end{aligned}
# $$

# In[3]:


import numpy as np
from scipy.linalg import null_space
A = np.array([[1,0,1,0,0,0],
              [0,1,0,1,0,0],
              [1,1,0,0,1,0],
              [4,2,0,0,0,1]])
B = np.array([1000,1500,1750,4800])

x=np.array([1000,400,0,1100,350,0])
lam=350
dx=np.array([-1,2,1,-2,-1,0])
x+lam*dx


# $$
# \begin{array}{lccccccl}
# & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 &\\
# \mathbf c & 12 & 9 & 0 & 0 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 0 & 1 & 0 & 0 & 0 & 1000\\
#           & 0 & 1 & 0 & 1 & 0 & 0 & 1500\\
#           & 1 & 1 & 0 & 0 & 1 & 0 & 1750\\
#           & 4 & 2 & 0 & 0 & 0 & 1 & 4800\\
# t=0       & N & N  & B & B & B & B & \\ 
# \end{array}
# $$
# 
# It follows that $\mathbf{x}^{(0)}=(0,0,1000,1500,1750,4800)$.
# 
# $$
# \begin{array}{lccccccl}
# & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 &\\
# \mathbf c & 12 & 9 & 0 & 0 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 0 & 1 & 0 & 0 & 0 & 1000\\
#           & 0 & 1 & 0 & 1 & 0 & 0 & 1500\\
#           & 1 & 1 & 0 & 0 & 1 & 0 & 1750\\
#           & 4 & 2 & 0 & 0 & 0 & 1 & 4800\\
# t=0       & N & N  & B & B & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 1000 & 1500 &1750 & 4800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & 0 & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{12}\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=9\\                 
# \lambda &  &   & \boxed{1000} &  & 1750 & 1200 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# It follows that $\mathbf{x}^{(1)}=\mathbf{x}^{(0)}+1000\times(1,0,-1,0,-1,-4)=(1000,    0,    0, 1500,  750,  800)$.
# 
# $$
# \begin{array}{lccccccl}
# & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 &\\
# \mathbf c & 12 & 9 & 0 & 0 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 0 & 1 & 0 & 0 & 0 & 1000\\
#           & 0 & 1 & 0 & 1 & 0 & 0 & 1500\\
#           & 1 & 1 & 0 & 0 & 1 & 0 & 1750\\
#           & 4 & 2 & 0 & 0 & 0 & 1 & 4800\\
# t=0       & N & N  & B & B & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 1000 & 1500 &1750 & 4800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & 0 & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{12}\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=9\\                 
# \lambda &  &   & \boxed{1000} &  & 1750 & 1200 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=1       & B & N & N & B & B & B & \\
# \mathbf{x}^{(1)} & 1000 & 0 &0 & 1500 & 750 & 800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=12000\\    
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1 & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{9}\\ 
# \Delta\mathbf x ~\text{for}~  x_3 & -1 & 0 & 1 & 0 & 1 & 4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-12\\                 
# \lambda & 1000 &   &   & 1500 & 750 & \boxed{400} & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# It follows that $\mathbf{x}^{(2)}=\mathbf{x}^{(1)}+400\times(0,1,0,-1,-1,-2)=(1000,  400,    0, 1100,  350,    0)$.
# 
# $$
# \begin{array}{lccccccl}
# & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 &\\
# \mathbf c & 12 & 9 & 0 & 0 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 0 & 1 & 0 & 0 & 0 & 1000\\
#           & 0 & 1 & 0 & 1 & 0 & 0 & 1500\\
#           & 1 & 1 & 0 & 0 & 1 & 0 & 1750\\
#           & 4 & 2 & 0 & 0 & 0 & 1 & 4800\\
# t=0       & N & N  & B & B & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 1000 & 1500 &1750 & 4800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & 0 & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{12}\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=9\\                 
# \lambda &  &   & \boxed{1000} &  & 1750 & 1200 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=1       & B & N & N & B & B & B & \\
# \mathbf{x}^{(1)} & 1000 & 0 &0 & 1500 & 750 & 800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=12000\\    
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1 & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{9}\\ 
# \Delta\mathbf x ~\text{for}~  x_3 & -1 & 0 & 1 & 0 & 1 & 4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-12\\                 
# \lambda & 1000 &   &   & 1500 & 750 & \boxed{400} & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=2       & B & B & N & B & B & N & \\
# \mathbf{x}^{(2)} & 1000 &  400 & 0 & 1100 & 350 & 0 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=15600\\    
# \Delta\mathbf x ~\text{for}~  x_3 & -1 & 2 & 1 & -2 & -1 & 0 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{6}\\ 
# \Delta\mathbf x ~\text{for}~  x_6 & 0 & -0.5 & 0 & 0.5 & -0.5 & 1 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-4.5\\                 
# \lambda & 1000 & -200  &   & 550 & \boxed{350} &  & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# It follows that $\mathbf{x}^{(3)}=\mathbf{x}^{(2)}+350\times(-1,2,1,-2,-1,0)=(650, 1100,  350,  400,    0,    0)$.
# 
# $$
# \begin{array}{lccccccl}
# & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 &\\
# \mathbf c & 12 & 9 & 0 & 0 & 0 & 0 & \mathbf b\\
# \mathbf A & 1 & 0 & 1 & 0 & 0 & 0 & 1000\\
#           & 0 & 1 & 0 & 1 & 0 & 0 & 1500\\
#           & 1 & 1 & 0 & 0 & 1 & 0 & 1750\\
#           & 4 & 2 & 0 & 0 & 0 & 1 & 4800\\
# t=0       & N & N  & B & B & B & B & \\
# \mathbf{x}^{(0)} & 0 & 0  & 1000 & 1500 &1750 & 4800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=0\\    
# \Delta\mathbf x ~\text{for}~  x_1 & 1 & 0  & -1 & 0 & -1 & -4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{12}\\ 
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1  & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=9\\                 
# \lambda &  &   & \boxed{1000} &  & 1750 & 1200 & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=1       & B & N & N & B & B & B & \\
# \mathbf{x}^{(1)} & 1000 & 0 &0 & 1500 & 750 & 800 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=12000\\    
# \Delta\mathbf x ~\text{for}~  x_2 & 0 & 1 & 0 & -1 & -1 & -2 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{9}\\ 
# \Delta\mathbf x ~\text{for}~  x_3 & -1 & 0 & 1 & 0 & 1 & 4 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-12\\                 
# \lambda & 1000 &   &   & 1500 & 750 & \boxed{400} & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=2       & B & B & N & B & B & N & \\
# \mathbf{x}^{(2)} & 1000 &  400 & 0 & 1100 & 350 & 0 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=15600\\    
# \Delta\mathbf x ~\text{for}~  x_3 & -1 & 2 & 1 & -2 & -1 & 0 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=\boxed{6}\\ 
# \Delta\mathbf x ~\text{for}~  x_6 & 0 & -0.5 & 0 & 0.5 & -0.5 & 1 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-4.5\\                 
# \lambda & 1000 & -200  &   & 550 & \boxed{350} &  & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# ---
# 
# $$
# \begin{array}{lccccccl}
# t=3       & B & B & B & B & N & N & \\
# \mathbf{x}^{(2)} & 650 & 1100 & 350 & 400 & 0 & 0 & \text{Current objective}: \mathbf c^T \mathbf x^{(0)}=\boxed{17700}\\    
# \Delta\mathbf x ~\text{for}~  x_5 & 1 & -2 & -1 & 2 & 1 & 0 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-6\\ 
# \Delta\mathbf x ~\text{for}~  x_6 & -0.5 & 0.5 & 0.5 & -0.5 & 0 & 1 & \text{Improve direction}: \mathbf c^T \Delta\mathbf x=-1.5\\                 
# \lambda &  &   &  &  &  &  & \text{Improve step}: \lambda=\text{min}\{-x_j/\Delta  x_j: \Delta x_j\le 0\}\\ 
# \end{array}
# $$
# 
# It follows that $\mathbf{x}^{(3)}=\mathbf{x}^*$ is optimal.
