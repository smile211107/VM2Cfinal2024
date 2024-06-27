import pandas as pd
import numpy as np
from gurobipy import *
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

BUILD_COST = 40
CAPACITY = 1000

def populate_factory(k=30):
    D = pd.read_csv("./data/2.6/Demand.txt", delimiter="\t", header=None).to_numpy()
    kmean = KMeans(k)
    kmean.fit(D[:, 1:3])

    centers = kmean.cluster_centers_
    centroid = np.mean(centers, axis=0)
    distances = np.linalg.norm(centers - centroid, axis=1)
    cluster_std = np.std(distances)

    with open("./data/2.6/Facility.txt", "w") as temp:
        for id, i in enumerate(centers):
            print(id + 1, *np.round(i, 3), CAPACITY, BUILD_COST, file=temp)

    with open("./data/2.6/TransCost.txt", "w") as temp:
        for j in centers:
            for i in D:
                print(np.round(np.linalg.norm(j - i[1:3]), 3), end=" ", file=temp)
            print("", file=temp)
    
    return cluster_std

def run():
    f = pd.read_csv("./data/2.6/Facility.txt", delimiter=" ", header=None).dropna(axis=1).iloc[:, 1:].to_numpy()
    t = pd.read_csv("./data/2.6/TransCost.txt", delimiter=" ", header=None).dropna(axis=1).to_numpy()
    D = pd.read_csv("./data/2.6/Demand.txt", delimiter="\t", header=None).to_numpy()
    with Env(empty=True) as env:
        env.setParam('OutputFlag', 0)
        env.start()
        with Model("2.6", env=env) as model:
            x = model.addMVar(t.shape, vtype=GRB.CONTINUOUS, name="x")
            c = model.addMVar((f.shape[0]), vtype=GRB.BINARY, name="c")
            model.update()

            model.addConstr(x.sum(axis=1) <= CAPACITY * c)
            model.addConstr(x.sum(axis=0) >= D[:, -1])

            model.setObjective((c * BUILD_COST).sum() + (x * t).sum(), sense=GRB.MINIMIZE)

            model.optimize()
            if model.Status == GRB.status.OPTIMAL:
                return model.ObjVal
            else:
                return 10**12
    
best = 10**12
k_best = -1
attempt = 5
lost_history = []

for k in range(2, 35):
    avg = 0
    for t in range(attempt):
        try:
            populate_factory(k)
            avg += run()
        except:
            continue
    loss = avg / attempt
    if loss != 1000000000000: lost_history.append(loss)
    if best > loss:
        best = loss
        k_best = k
    print(f"k={k} avg_loss={loss:.4f} best={best:.4f} k_best={k_best}")

plt.plot(lost_history)
plt.show()