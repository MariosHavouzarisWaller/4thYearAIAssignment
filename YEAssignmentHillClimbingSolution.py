# Read the data given a file name. Returns: n = no. of items, rows = values included in the csv file
import csv
import random as rnd
import matplotlib.pyplot as plt

def read_art_data(fname):       
    rows = []
    with open(fname, 'r') as file: 
        csvreader = csv.reader(file)
        n = len(next(csvreader))
        for row in csvreader:
            rows.append(row)
    return n, rows
    

# Reading data from a file, in this example the instance with 5 items
artfile = "values50.csv"     # filename, should be located in the same directory
n, values = read_art_data(artfile)

# # To increase the chance of generating a valid solution, we produce a random string with less number of 1's than 0's
# # Output: a random solution, as well as its value and weight 

def random_sol(l):
    sol = rnd.choices([0,1], weights=[50, 50], k = l)
    return sol

solution = random_sol(n)

    # Implementation using a for loop
def evaluate(sol):
    AnneVal = 0
    BobVal = 0
    for i in range(n):
        if sol[i] == 1:
            AnneVal += int(values[0][i])
        if sol[i] == 0:
            BobVal += int(values[0][i]) 
    return AnneVal, BobVal

def neighbour(sol) :
    neig = sol[:]
    i = rnd.randint(0, n-1)
    neig[i] = 0 if sol[i] == 1 else 1
    return neig

neig = neighbour(solution)

def hill_climbing(maxiter):
    trace = []
    t = []
    s = random_sol(n)
    v = evaluate(s)
    trace.append(v)
    for i in range(maxiter):
        s1 = neighbour(s)
        v1 = evaluate(s1)
        if v1 >= v:
            v = v1
            s = s1[:]
            trace.append(v)
    for j in trace:
        v2 = j[0] - j[1]
        if v2 < 0:
             v2 *= -1
        t.append(v2)
    v = min(t)
    return s, v, t, trace

ntries = 200
nruns = 30
s, v, t, trace = hill_climbing(ntries)
print(f'Best Solution: {s}\n Best Value: {v}\n Trace: {t}')

plt.plot(t, color='green', linewidth=2)
plt.title('Hill-Climbing Trace')
plt.ylabel('Values')
plt.xlabel('Improving Steps')

plt.plot(trace, color='red', linewidth=2)
plt.title('Hill-Climbing Trace')
plt.ylabel('Values')
plt.xlabel('Improving Steps')
plt.show()

hc_vals = []
for i in range(nruns):
    s, v, t, trace = hill_climbing(ntries)
    hc_vals.append(v)

plt.title("Hill Climbing")
plt.ylabel("Values")
plt.boxplot(hc_vals)
plt.show()