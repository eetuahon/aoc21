def read_file():
    a = []
    f = open("inputd08", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    numbers = []
    for r in f:
        row = r.split(" | ") # 0 to 9 in random order + 4 numbers
        a = row[0].split()
        a += row[1].split()
        numbers.append(a)
    return numbers

def lens(): #digit: its len
    return {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

def dictize(l):
    l.sort(key=len)
    k = dict()
    k.update({l[0] : 1})
    k.update({l[1] : 7})
    k.update({l[2] : 4})
    k.update({l[9] : 8})
    a = l[1].replace(l[0][0],"").replace(l[0][1],"")
    d = ""
    e = ""
    g = ""
    nine = ""
    for i in l[6:9]:
        lines = {l[2][0], l[2][1], l[2][2], l[2][3]}
        if l[2][0] in i and l[2][1] in i and l[2][2] in i and l[2][3] in i:
            lines.update({l[1][0], l[1][1], l[1][2]})
            if l[1][0] in i and l[1][1] in i and l[1][2] in i:
                k.update({i : 9})
                nine = i
                j = i
                for x in lines:
                    j = j.replace(x, "")
                g = j
    for i in l[3:6]:
        if l[0][0] in i and l[0][1] in i:
            k.update({i : 3})
            d = i.replace(a,"").replace(l[0][0],"").replace(l[0][1],"").replace(g,"")
    for i in l[6:9]:
        if d not in i:
            k.update({i: 0})
    for i in l[6:9]:
        if i not in k.keys():
            k.update({i: 6})
            e = i
            for i in nine:
                e = e.replace(i, "")
    for i in l[3:6]:
        if e in i:
            k.update({i: 2})
    for i in l[3:6]:
        if i not in k.keys():
            k.update({i: 5})
    return k

def task1(f,d):
    counter = 0
    for r in f:
        for n in r[10:]:
            if len(n) == d[1]:
                counter += 1
            elif len(n) == d[4]:
                counter += 1
            elif len(n) == d[7]:
                counter += 1
            elif len(n) == d[8]:
                counter += 1
    print(counter) #8.1

def task2(f,d):
    s = 0
    for r in f:
        r = ["".join(sorted(i)) for i in r]
        ns = dictize(r[:10])
        num = ns[r[-1]] + ns[r[-2]] * 10 + ns[r[-3]] * 100 + ns[r[-4]] * 1000
        s += num
    print(s) #8.2

def main():
    f = read_file()
    f = format_file(f)
    d = lens()
    task1(f,d)
    task2(f,d)

if __name__== "__main__":
    main()