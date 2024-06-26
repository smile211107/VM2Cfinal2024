import numpy as np
from pandas import read_csv

nFacility = 10
nShop = 200
filename = "2.4"

input_lines = open(f"Final/out/{filename}.out","r").readlines()
cost = np.array([[0] * nShop] * nFacility,dtype=float)
choose = np.array(list(map(int,input_lines[0].strip().split(" "))))
# print(choose)
optimal_value = float(input_lines[-1].strip().split(" ")[0])
for i in range(1,len(input_lines)-1):
    x,y,w = list(map(float,input_lines[i].strip().split(" ")))
    x,y = int(x),int(y)
    x -= 1
    y -= 1
    cost[x,y] = w

previous_choose = np.array([0,1,0,1,0,1,0,1,1,0])
# print(previous_choose)
# previous_choose = np.array([0,0,1,1,0,1,0,1,1,0])
# Not imple for 2.2.2
MAX_CAPACITY = 1000

for i in range(nFacility):
    # Check if facility is producing while not chosen
    if choose[i] == 0 and cost[i].sum() != 0:
        print(f"Constraint Violated : Facility {i} distribute {cost[i].sum()} goods while not chosen")
        exit(0)

    # Check if facility is over producing
    if cost[i].sum() > MAX_CAPACITY:
        print(f"Constraint Violated : Facility over producing {cost[i].sum() - MAX_CAPACITY} goods")
        exit(0)

match filename:
    case "2.3":
        demand = read_csv("VM2Cfinal2024/data/2.3/DemandAdd.csv").to_numpy()[:,-1]

        for i in range(nFacility):
            # Check if facility is removed from the answer
            if previous_choose[i] == 1 and choose[i] == 0:
                print(f"Constraint Violated : Facility {i} is removed")
                exit(0)
            
        for j in range(nShop):
            # Check if shop is supplied
            if cost[:,j].sum() < demand[j]:
                print(f"Constraint Violated : Shop {j} under supplied: Demand : {demand[j]}, supply : {cost[:,j]}")
                exit(0)
    case "2.4":
        demand = read_csv("VM2Cfinal2024/data/2.4/DemandMinus.csv").to_numpy()[:,-1]
        
        for i in range(nFacility):
            # Check if facility is add from the answer
            if previous_choose[i] == 0 and choose[i] == 1:
                print(f"Constraint Violated : Facility {i} is added")
                exit(0)

        for j in range(nShop):
            # Check if shop is supplied
            if cost[:,j].sum() < demand[j]:
                print(f"Constraint Violated : Shop {j} under supplied: Demand : {demand[j]}, supply : {cost[:,j]}")
                exit(0)

    case "2.5":
        demand = read_csv("Final/2.2.1/Demand.csv").to_numpy()[:,-1]
        for j in range(nShop):
            # Check if shop is supplied
            if cost[:,j].sum() < demand[j]:
                print(f"Constraint Violated : Shop {j} under supplied: Demand : {demand[j]}, supply : {cost[:,j]}")
                exit(0)


