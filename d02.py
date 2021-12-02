def read_file():
    a = []
    f = open("inputd02", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify_data(d):
    d2 = []
    for i in d:
        r = i.split(" ")
        d2.append((r[0],int(r[1])))
    return d2

def task1(f):
    hor = 0
    ver = 0
    for i in f:
        if i[0] == "forward":
            hor += i[1]
        elif i[0] == "down":
            ver += i[1]
        elif i[0] == "up":
            ver -= i[1]
    print(hor * ver) # 1.1

def task2(f):
    hor = 0
    ver = 0
    aim = 0
    for i in f:
        if i[0] == "forward":
            hor += i[1]
            ver += aim * i[1]
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "up":
            aim -= i[1]
    print(hor * ver) # 1.2

def main():
    f = read_file()
    f = modify_data(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()