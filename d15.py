def read_file():
    a = []
    f = open("inputd15", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    y = []
    for l in f:
        x = list(l)
        y.append([int(i) for i in x])
    return y

def update_diags(f, s):
    c = 0
    y_len = len(f)
    x_len = len(f[0])
    for y in range(y_len - 2, -1, -1):
        for x in range(x_len - 2, -1, -1):
            n = min(s[y+1][x], s[y][x+1])
            if s[y][x] > f[y][x] + n:
                c += 1
                s[y][x] = f[y][x] + n
    for y in range(1, y_len):
        for x in range(1, x_len):
            n = min(s[y-1][x], s[y][x-1])
            if s[y][x] > f[y][x] + n:
                c += 1
                s[y][x] = f[y][x] + n
    return c

def make_sumtable(f):
    sumtable = []
    y_len = len(f)
    x_len = len(f[0])
    for y in range(y_len):
        sumtable.append([0 for x in range(x_len)])
    for y in range(y_len):
        for x in range(x_len):
            if y == 0 and x == 0:
                sumtable[y][x] = f[0][0]
            elif y == 0:
                sumtable[y][x] = f[y][x] + sumtable[y][x-1]
            elif x == 0:
                sumtable[y][x] = f[y][x] + sumtable[y-1][x]
            else:
                sumtable[y][x] = f[y][x] + min(sumtable[y-1][x], sumtable[y][x-1])
    updates = 1
    while updates != 0:
        updates = update_diags(f, sumtable)
    return sumtable

def expand_sqr(f):
    y_len = len(f)
    for y in f:
        z = y.copy()
        for i in range(1,5):
            y.extend([x+i if x+i < 10 else x+i-9 for x in z])
    for i in range(1,5):
        for y in range(y_len):
            f.append([x+i if x+i < 10 else x+i-9 for x in f[y]])

def task1(f):
    y_len = len(f)
    x_len = len(f[0])
    sumtable = make_sumtable(f)
    print(sumtable[y_len-1][x_len-1] - sumtable[0][0]) #15.1

def task2(f): #slow but less than 1min
    expand_sqr(f)
    y_len = len(f)
    x_len = len(f[0])
    sumtable = make_sumtable(f)
    print(sumtable[y_len-1][x_len-1] - sumtable[0][0]) #15.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()