def read_file():
    a = []
    f = open("inputd03", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def commons(l, i):
    ones = []
    zeros = []
    for no in l:
        if no[i] == "1":
            ones.append(no)
        else:
            zeros.append(no)
    return (zeros, ones)

def task1(f):
    l = len(f[0])
    gam = ""
    eps = ""
    for i in range(l):
        b = commons(f, i)
        if len(b[0]) > len(b[1]):
            gam += "0"
            eps += "1"
        else:
            gam += "1"
            eps += "0"
    gam = int(gam, 2)
    eps = int(eps, 2)
    print(gam * eps) # 3.1

def task2(f):
    l = len(f[0])
    f2 = f.copy()
    gen = ""
    scr = ""
    for i in range(l):
        b = commons(f, i)
        c = commons(f2, i)
        if len(b[0]) > len(b[1]):
            gen += "0"
            f = b[0]
        else:
            gen += "1"
            f = b[1]
        if len(c[0]) == 1:
            scr = c[0][0]
        elif len(c[1]) == 1:
            scr = c[1][0]
        elif len(c[0]) >= len(c[1]):
            f2 = c[1]
        else:
            f2 = c[0]
    gen = int(gen, 2)
    scr = int(scr, 2)
    print(gen * scr) #3.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()