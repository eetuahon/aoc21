def read_file():
    a = []
    f = open("inputd11", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    c = []
    for i in f:
        r = list(i)
        c.append([int(x) for x in r])
    return c

def step(f):
    flash = set()
    for y in range(10):
        for x in range(10):
            f[y][x] += 1
            if f[y][x] > 9:
                flash.add((x,y))
    return flash

def flashing(f, l):
    done = set()
    while len(l) > len(done):
        waiting = set()
        for i in l:
            if i in done: continue
            x = i[0]
            y = i[1]
            if x < 9:
                f[y][x+1] += 1
                if f[y][x+1] > 9: waiting.add((x+1,y))
            if x > 0:
                f[y][x-1] += 1
                if f[y][x-1] > 9: waiting.add((x-1,y))
            if y < 9 and x > 0:
                f[y+1][x-1] += 1
                if f[y+1][x-1] > 9 : waiting.add((x-1,y+1))
            if y < 9:
                f[y+1][x] += 1
                if f[y+1][x] > 9: waiting.add((x,y+1))
            if y < 9 and x < 9:
                f[y+1][x+1] += 1
                if f[y+1][x+1] > 9: waiting.add((x+1,y+1))
            if y > 0 and x > 0:
                f[y-1][x-1] += 1
                if f[y-1][x-1] > 9: waiting.add((x-1,y-1))
            if y > 0:
                f[y-1][x] += 1
                if f[y-1][x] > 9: waiting.add((x,y-1))
            if y > 0 and x < 9:
                f[y-1][x+1] += 1
                if f[y-1][x+1] > 9: waiting.add((x+1,y-1))
            done.add(i)
        l.update(waiting)
    for i in done:
        f[i[1]][i[0]] = 0
    return len(done)

def task1(f):
    s = 0
    for steps in range(100): #count after 100 steps
        flash = step(f)
        s += flashing(f, flash)
    print(s) #11.1

def task2(f):
    s = 0
    no_flashes = -1
    while no_flashes != 100:
        s += 1
        flash = step(f)
        no_flashes = flashing(f, flash)
    print(s) #11.2

def main():
    f = read_file()
    f = format_file(f)
    f2 = [i.copy() for i in f]
    task1(f)
    task2(f2)

if __name__== "__main__":
    main()