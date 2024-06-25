import sys


def txt_to_csv(filenameWithoutExtension, header):
    inp = sys.stdin
    out = sys.stdout
    header_len = 0

    sys.stdin = open(f"{filenameWithoutExtension}.txt", 'r')
    sys.stdout = open(f"{filenameWithoutExtension}.csv", 'w')

    if header:
        header_len = len(header)
        print(", ".join(header))
    while True:
        try:
            temp = input()
            if temp.count("\t") < header_len - 1:
                raise RuntimeError("Number of header is not enough")
            print(temp.replace("\t", ","))
        except EOFError:
            break

    sys.stdin = inp
    sys.stdout = out

txt_to_csv("./data/2.5/Facility", ["id", "x", "y", "capacity", "cost"])
txt_to_csv("./data/2.5/DemandRand", ["id", "x", "y", "avg", "std"])
txt_to_csv("./data/2.5/TransCost", None)