import copy

def read_file():
    a = []
    f = open("inputd18", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    lines = []
    for line in f:
        l = form_line(line)
        lines.append(l)
    return lines

def form_line(s):
    b = s[1:-1]
    lvls = {0: "", 1: "", 2: "", 3:""}
    c = 0
    for i in range(len(b)):
        if b[i] == ",": continue
        if b[i] == "[":
            c+=1
            lvls.update({c-1: lvls[c-1] + "*"})
        elif b[i] == "]":
            c-=1
            lvls.update({c+1: lvls[c+1]})
        else:
            lvls.update({c: lvls[c] + b[i]})
    c = 0
    for i in range(4):
        line = list(lvls[c])
        lvls.update({c: [i if i=="*" else int(i) for i in line]})
        if "*" in lvls[i]: c+=1
    while c > 0:
        line = lvls[c-1]
        sel = 0
        for i in range(len(line)):
            if line[i] == "*":
                line[i] = [lvls[c][sel], lvls[c][sel+1]]
                sel += 2
        c -= 1
    return lvls[0]

def xplode(f):
    c = 0
    carry = 0
    prev = ()
    for i in range(len(f)):
        if type(f[i]) != list:
            prev = (i)
            if carry > 0:
                f[i] += carry
                carry = 0
            continue
        for j in range(len(f[i])):
            if type(f[i][j]) != list:
                prev = (i,j)
                if carry > 0:
                    f[i][j] += carry
                    carry = 0
                continue
            for k in range(len(f[i][j])):
                if type(f[i][j][k]) != list:
                    prev = (i,j,k)
                    if carry > 0:
                        f[i][j][k] += carry
                        carry = 0
                    continue
                for l in range(len(f[i][j][k])):
                    if type(f[i][j][k][l]) != list:
                        prev = (i,j,k,l)
                        if carry > 0:
                            f[i][j][k][l] += carry
                            carry = 0
                        continue
                    if carry > 0: f[i][j][k][l][0] += carry ###
                    carry = f[i][j][k][l][1]
                    if len(prev) == 4:
                        f[prev[0]][prev[1]][prev[2]][prev[3]] += f[i][j][k][l][0]
                    elif len(prev) == 3:
                        f[prev[0]][prev[1]][prev[2]] += f[i][j][k][l][0]
                    elif len(prev) == 2:
                        f[prev[0]][prev[1]] += f[i][j][k][l][0]
                    elif len(prev) != 0:
                        f[prev] += f[i][j][k][l][0]
                    prev = (i,j,k,l)
                    f[i][j][k][l] = 0
                    c += 1
    return c

def split(f):
    for i in range(len(f)):
        if type(f[i]) != list:
            if f[i] > 9:
                left = int(f[i] / 2)
                f[i] = [left, f[i] - left]
                return 1
            continue
        for j in range(len(f[i])):
            if type(f[i][j]) != list:
                if f[i][j] > 9:
                    left = int(f[i][j] / 2)
                    f[i][j] = [left, f[i][j] - left]
                    return 1
                continue
            for k in range(len(f[i][j])):
                if type(f[i][j][k]) != list:
                    if f[i][j][k] > 9:
                        left = int(f[i][j][k] / 2)
                        f[i][j][k] = [left, f[i][j][k] - left]
                        return 1
                    continue
                for l in range(len(f[i][j][k])):
                    if f[i][j][k][l] > 9:
                        left = int(f[i][j][k][l] / 2)
                        f[i][j][k][l] = [left, f[i][j][k][l]-left]
                        return 1
    return 0

def addup(a,b):
    sum = [a,b]
    x = 1
    while x > 0:
        while x > 0:
            x = xplode(sum)
        x = split(sum)
    return sum

def magnitude(f):
    a = f[0]
    b = f[1]
    if type(a) == list:
        a = 3 * magnitude(a)
    else:
        a = 3 * a
    if type(b) == list:
        b = 2 * magnitude(b)
    else:
        b = 2 * b
    return a + b

def task1(f):
    sum = f[0]
    for i in range(1,len(f)):
        sum = addup(sum,f[i])
    m = magnitude(sum)
    print(m) #18.1

def task2(f):
    mm = 0
    for i in f:
        for j in f:
            if i == j: continue
            m = magnitude(addup(copy.deepcopy(i),copy.deepcopy(j)))
            if m > mm: mm = m
    print(mm) #18.2

def main():
    f = read_file()
    f2 = format_file(f)
    f = format_file(f)
    task1(f)
    task2(f2)

if __name__== "__main__":
    main()