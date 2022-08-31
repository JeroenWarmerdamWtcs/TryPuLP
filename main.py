import random
from pulp import *

c = [(1, 'a'), (2, 'f'), (3, 'y'), (4, 'ty')]
x = [(1, 3), (2, 6), (3, 4), (4, 7)]
y = [(1, 8), (2, 9), (3, 13), (4, 17)]

c = [i[1] for i in c]
x = [i[1] for i in x]
y = [i[1] for i in y]

d = dict(zip(c, zip(x, y)))
print(d)
exit()

# Creates a list of the Ingredients
Ingredients = ["CHICKEN", "BEEF", "MUTTON", "RICE", "WHEAT", "GEL"]

# A dictionary of the costs of each of the Ingredients is created
costs = {
    "CHICKEN": 0.013,
    "BEEF": 0.008,
    "MUTTON": 0.010,
    "RICE": 0.002,
    "WHEAT": 0.005,
    "GEL": 0.001,
}

# A dictionary of the protein percent in each of the Ingredients is created
proteinPercent = {
    "CHICKEN": 0.100,
    "BEEF": 0.200,
    "MUTTON": 0.150,
    "RICE": 0.000,
    "WHEAT": 0.040,
    "GEL": 0.000,
}

# A dictionary of the fat percent in each of the Ingredients is created
fatPercent = {
    "CHICKEN": 0.080,
    "BEEF": 0.100,
    "MUTTON": 0.110,
    "RICE": 0.010,
    "WHEAT": 0.010,
    "GEL": 0.000,
}

# A dictionary of the fibre percent in each of the Ingredients is created
fibrePercent = {
    "CHICKEN": 0.001,
    "BEEF": 0.005,
    "MUTTON": 0.003,
    "RICE": 0.100,
    "WHEAT": 0.150,
    "GEL": 0.000,
}

# A dictionary of the salt percent in each of the Ingredients is created
saltPercent = {
    "CHICKEN": 0.002,
    "BEEF": 0.005,
    "MUTTON": 0.007,
    "RICE": 0.002,
    "WHEAT": 0.008,
    "GEL": 0.000,
}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The_Whiskas_Problem", LpMinimize)

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
ingredient_vars = LpVariable.dicts("Ingr", Ingredients, 0)

# The objective function is added to 'prob' first
prob += (
    lpSum([costs[i] * ingredient_vars[i] for i in Ingredients]),
    "Total Cost of Ingredients per can",
)
# The five constraints are added to 'prob'
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 100, "PercentagesSum"
prob += (
    lpSum([proteinPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 8.0,
    "ProteinRequirement",
)
prob += (
    lpSum([fatPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 6.0,
    "FatRequirement",
)
prob += (
    lpSum([fibrePercent[i] * ingredient_vars[i] for i in Ingredients]) <= 2.0,
    "FibreRequirement",
)
prob += (
    lpSum([saltPercent[i] * ingredient_vars[i] for i in Ingredients]) <= 0.4,
    "SaltRequirement",
)

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)


x = []
x.append(LpVariable("z2128s13568z2135s13505", 0, None, LpInteger))
x.append(LpVariable("z2128s13511z2135s13505", 0, None, LpInteger))

u = LpVariable("u", 0, None, LpInteger)

'''

for all variables:
    create LpVariable("name", 0, None, LpInteger)

for all equations:
    prob += LpSum(list of variable in equation) >= lower_bound
    prob += LpSum(list of variable in equation) <= upper_bound
    
    if lowerbound >= 50:
        create u = LpVariable("name", 0, None, LpInteger)
        store u in u_list
        prob += LpSum(list of variable in equation) - (upper_bound + lowerbound)/2 >= u
        prob += -LpSum(list of variable in equation) + (upper_bound + lowerbound)/2 >= u
        
prob += LpSum(u_list)
    

'''

prob = LpProblem("m", LpMinimize)
prob += u
prob += x[1] - 129.4 <= u
prob += 129.4 - x[1] <= u


prob += 145 <= x[0] + x[1]
prob += x[0] + x[1] <= 154


#  1,13505,nrm: 2128,150
prob += 145 <= x[0] + x[1]
prob += x[0] + x[1] <= 154

# 1,13505,13568,-1
prob += 1 <= x[0]
prob += x[0] <= 49

# 1,nrm: 2128,nrm: 2135,150
prob += 145 <= x[0] + x[1]
prob += x[0] + x[1] <= 154

# 1,13568,nrm: 2135,-1
prob += 1 <= x[0]
prob += x[0] <= 49


# 1,13505,13511,130
prob += 125 <= x[1]
prob += x[1] <= 134

# 1,13511,nrm: 2135,130
prob += 125 <= x[1]
prob += x[1] <= 134

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(f"{v.name} = {v.varValue}")


MATRIX_SIZE = 3000
rhb = []
for i in range(MATRIX_SIZE):
    rhb.append(random.randint(10, 30))

prob = LpProblem("m2", LpMinimize)
variables = {}
for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        variables[(i, j)] = LpVariable(f"v({i},{j})", 0, None)
for i in range(MATRIX_SIZE):
    prob += variables[(i, i)] <= 0
for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        prob += variables[(i, j)] == variables[(j, i)]

for i in range(MATRIX_SIZE):
    prob += lpSum([variables[(i, j)] for j in range(MATRIX_SIZE)]) == rhb[i]


prob.solve()

for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        print(f"{variables[(i, j)].varValue:4}", end=" ")
    print(f" = {rhb[i]}")


