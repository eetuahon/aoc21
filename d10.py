def read_file():
    a = []
    f = open("inputd10", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    c = []
    for i in f:
        c.append(list(i))
    return c

def task1(f):
    illegals = []
    s = 0
    opens = ["(", "[", "{", "<"]
    closes = [")", "]", "}", ">"]
    for line in f:
        stack = ""
        for i in line:
            if i in opens:
                stack += i
            else:
                ind = opens.index(stack[-1])
                if closes.index(i) == ind:
                    stack = stack[:-1]
                else:
                    illegals.append(i)
                    break
    for i in illegals: # rules given in the task
        if i == ")": s += 3
        if i == "]": s += 57
        if i == "}": s += 1197
        if i == ">": s += 25137
    print(s) #10.1

def task2(f):
    inc = []
    sums = []
    opens = ["(", "[", "{", "<"]
    closes = [")", "]", "}", ">"]
    for line in f:
        stack = ""
        for i in line:
            if i in opens:
                stack += i
            else:
                ind = opens.index(stack[-1])
                if closes.index(i) == ind:
                    stack = stack[:-1]
                else:
                    stack = ""
                    break
        if len(stack) > 0:
            inc.append(stack)
    for i in inc:
        s = 0
        for j in range(len(i)):
            s *= 5
            if i[-1] == "(": s += 1 #as per rules
            if i[-1] == "[": s += 2 #as per rules
            if i[-1] == "{": s += 3 #as per rules
            if i[-1] == "<": s += 4 #as per rules
            i = i[:-1]
        sums.append(s)
    sums.sort()
    print(sums[int(len(sums) / 2)]) #10.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()