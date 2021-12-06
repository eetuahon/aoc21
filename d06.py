def read_file():
    a = []
    f = open("inputd06", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    f = f[0].split(",")
    return [int(x) for x in f]

def dicter(l):
    d = dict()
    for i in range(8):
        d.update({i:0})
    for i in l:
        if i in d.keys():
            c = d[i]
            d.update({i: c + 1})
    return d

def rounder(a):
    for i in range(1, len(a)):
        a[i-1] = a[i]
    return a

def calculator(f,d):
    howmanydays = d #80 in 6.1, 256 in 6.2
    counters = dicter(f)
    c = len(f)
    memory = [0,0,0,0,0,0,0,0]
    for d in range(howmanydays):
        check = d % 7
        add = memory[0]
        memory = rounder(memory)
        memory[7] = counters[check]
        counters[(check + 1) % 7] += add
        c += add
    c += sum(memory)
    return c

def task1(f):
    c = calculator(f, 80) #80 days asked
    print(c) #6.1

def task2(f):
    c = calculator(f, 256) #256 days asked
    print(c) #6.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()