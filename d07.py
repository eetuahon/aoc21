def read_file():
    a = []
    f = open("inputd07", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    f = f[0].split(",")
    return [int(x) for x in f]

def task1(f):
    min_sum = 9999999999
    for i in range(max(f) + 1):
        a = sum([abs(x - i) for x in f])
        if min_sum > a:
            min_sum = a
    print(min_sum) #7.1

def task2(f):
    min_sum = 999999999999999
    for i in range(max(f) +1):
        a = [abs(x - i) for x in f]
        b = [int(x * (1 + x) / 2) for x in a] #arithmetic series
        if min_sum > sum(b):
            min_sum = sum(b)
    print(min_sum) #7.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()