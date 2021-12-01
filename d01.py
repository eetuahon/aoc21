def read_file():
    a = []
    f = open("inputd01", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    l = len(f)
    c = 0
    for i in range(1, l):
        if f[i] > f[i-1]:
            c += 1
    print(c) # 1.1

def task2(f):
    l = len(f)
    c = 0
    f2 = []
    for i in range(l-2):
        f2.append(f[i] + f[i+1] + f[i+2])
    task1(f2) # 1.2

def main():
    f = read_file()
    ints = [int(i) for i in f]
    task1(ints)
    task2(ints)

if __name__== "__main__":
    main()