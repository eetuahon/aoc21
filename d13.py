def read_file():
    a = []
    f = open("inputd13", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    dots = set()
    folds = list()
    for i in f:
        if len(i) == 0:
            continue
        elif i[0] == "f":
            folds.append(i.split(" ")[2])
        else:
            c = i.split(",")
            dots.add((int(c[0]), int(c[1])))
    return (dots, folds)

def task1(f):
    dots = set()
    folds = f[1]
    first_f = folds[0].split("=")
    fo = int(first_f[1])
    for d in f[0]:
        if first_f[0] == "y":
            if d[1] > fo:
                dots.add((d[0], 2 * fo - d[1]))
            else:
                dots.add(d)
        else:
            if d[0] > fo:
                dots.add((2 * fo - d[0], d[1]))
            else:
                dots.add(d)
    print(len(dots)) #13.1

def task2(f):
    folds = f[1]
    dots = f[0]
    xs = 10
    ys = 10
    for fo in folds:
        nd = set()
        cf = fo.split("=")
        if cf[0] == "y":
            ys = int(cf[1])
            for d in dots:
                if d[1] > ys:
                    nd.add((d[0], 2 * ys - d[1]))
                else:
                    nd.add((d[0], d[1]))
        else:
            xs = int(cf[1])
            for d in dots:
                if d[0] > xs:
                    nd.add((2 * xs - d[0], d[1]))
                else:
                    nd.add((d[0], d[1]))
        dots = nd
    line = ""
    for i in range(xs):
        line += "."
    box = []
    for i in range(ys):
        box.append(line)
    for d in dots:
        row = box[d[1]]
        row = row[:d[0]] + "#" + row[d[0]+1:]
        box[d[1]] = row
    for i in box:
        print(i)
    print("See {} lines above for answer".format(ys)) #13.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()