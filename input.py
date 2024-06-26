import sys


def txt_to_csv(filenameWithoutExtension, header, delimiter="\t"):
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
            if temp.count(delimiter) < header_len - 1:
                raise RuntimeError("Number of header doesn't match number of columns")
            print(temp.replace(delimiter, ","))
        except EOFError:
            break

    sys.stdin = inp
    sys.stdout = out

txt_to_csv("./data/2.6/Demand", ["id", "x", "y", "require"])
txt_to_csv("./data/2.6/Facility", ["id", "x", "y", "capacity", "cost"], delimiter=" ")
# txt_to_csv("./data/2.6/TransCost", header=None)