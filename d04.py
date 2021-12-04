def read_file():
    a = []
    f = open("inputd04", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    row = [int(i) for i in f[0].split(",")]
    coupons = []
    coupon = []
    value = 0
    for i in range(2,len(f)):
        if len(f[i]) == 0:
            coupons.append((coupon, value, dict()))
            coupon = []
            value = 0
        else:
            ints = [int(j) for j in f[i].split()]
            coupon.append(ints)
            value += sum(ints)
    coupons.append((coupon, value, dict()))
    return (row, coupons)

def play(c, n):
    coupon = c[0]
    val = c[1]
    history = c[2]
    size = len(coupon)
    found = False
    for y in range(size):
        for x in range(size):
            if coupon[y][x] == n:
                val -= n
                y_c = "y" + str(y)
                x_c = "x" + str(x)
                if y_c in history.keys():
                    v = history[y_c]
                    history.update({y_c: v + 1})
                else:
                    history.update({y_c: 1})
                if x_c in history.keys():
                    v = history[x_c]
                    history.update({x_c: v + 1})
                else:
                    history.update({x_c: 1})
    if size in history.values():
        found = True
    return (coupon, val, history, found)

def task1(f):
    row = f[0]
    coupons = f[1]
    c_c = len(coupons)
    br = 0
    lst = -1
    for c in row:
        for i in range(c_c):
            p = play(coupons[i], c)
            if p[3]:
                br = p[1]
                lst = c
                break
            coupons[i] = (p[0], p[1], p[2])
        if lst > -1:
            break
    print(br * lst) # 4.1

def task2(f):
    row = f[0]
    coupons = f[1]
    c_c = len(coupons)
    br = 0
    lst = -1
    count = 0
    won = []
    for c in row:
        for i in range(c_c):
            if i not in won:
                p = play(coupons[i], c)
                if p[3]:
                    br = p[1]
                    lst = c
                    won.append(i)
                    count += 1
                coupons[i] = (p[0], p[1], p[2])
        if count == c_c:
            break
    print(br * lst) #4.2

def main():
    f = read_file()
    f2 = format_file(f.copy())
    f = format_file(f)
    task1(f)
    task2(f2)

if __name__== "__main__":
    main()

