import numpy as np

EPSILON = 1e-9

def isClose(x,y) -> bool:
    return abs(x-y) <= EPSILON

def isGeq(x,y) -> bool:
    return x - y >= EPSILON

def isLeq(x,y) -> bool:
    return x - y <= EPSILON

def isGreater(x,y) -> bool:
    return x - y > EPSILON

def isLess(x,y) -> bool:
    return x - y < EPSILON

num_test = 0
num_facility = []
coord = []
test_ans = []

def read_input() -> None:
    global num_test,num_facility,coord,test_ans
    with open("Final/out/2.6.out","r") as f:
        input = [i.strip() for i in f.readlines()]
    cnt = -1
    num_test = 9
    for t in range(num_test):
        cnt += 1
        num_facility.append(int(input[cnt]))
        coord.append([])
        for __ in range(num_facility[t]):
            cnt += 1
            coord[t].append(list(map(float,input[cnt].split(" "))))
        cnt += 1
        test_ans.append(float(input[cnt]))


num_rec = 5
rectangle = [
    [[3.5,5.2],[4.8,6.2]],
    [[2.7,3.3],[3.0,3.8]],
    [[3.2,3.0],[3.8,3.4]],
    [[4.7,4.2],[5.0,4.5]],
    [[5.9,2.9],[6.2,3.8]]
]

circle = [[6.25,7.45],0.75]

def check_valid(x,y):
    '''
    Check if facility is NOT in any green area
    '''
    global num_rec,rectangle,circle

    # Check if x,y in any rectangle
    for i in range(num_rec):
        if isGeq(x,rectangle[i][0][0]) and isLeq(x,rectangle[i][1][0]) and isGeq(y,rectangle[i][0][1]) and isLeq(y,rectangle[i][1][1]):
            return False,f"Rec {i}"
        
    # Check if x,y in the circle
    if not isGreater(np.linalg.norm(np.array([x,y]) - np.array(circle[0])),circle[1]):
        return False,"Circle 6"
    
    return True,""

def lp_optimize():
    ...

def main() -> None:
    global num_test,num_facility,coord,test_ans
    read_input()
    # print(num_test)
    # print(num_facility)
    # print(coord)
    print(np.argmin(np.array(test_ans)))
    for t in range(num_test):
        for i in range(num_facility[t]):
            x,y = coord[t][i]
            res = check_valid(x,y)
            if not res[0]:
                print(f"Test {t} -> Facility {i} IS in Green Area (Violation), {res[1]}")

    # print(check_valid(4,6))

if __name__ == "__main__":
    main()
