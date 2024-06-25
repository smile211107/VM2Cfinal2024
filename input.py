import sys

sys.stdin = open("./data/2.3/Facility.txt", "r")
sys.stdout = open("./data/2.3/Facility.csv", "w")
print("id, x, y, capacity, cost")
for i in range(10):
    print(input().replace("\t", ", "))


sys.stdin = open("./data/2.3/DemandAdd.txt", "r")
sys.stdout = open("./data/2.3/DemandAdd.csv", "w")
print("id, x, y, require")
for i in range(200):
    print(input().replace("\t", ", "))


sys.stdin = open("./data/2.3/TransCost.txt", "r")
sys.stdout = open("./data/2.3/TranCost.csv", "w")
for i in range(10):
    print(input().replace("\t", ", "))