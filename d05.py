def read_file():
    a = []
    f = open("inputd05", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    coords = []
    m = -1
    for i in f:
        r = i.split(" -> ")
        c = [int(x) for x in r[0].split(",")]
        c += [int(x) for x in r[1].split(",")]
        if max(c) > m:
            m = max(c)
        coords.append(c)
    return (coords, m)

def mapper(m):
    map = []
    for i in range(m):
        map.append([])
        for j in range(m):
            map[i].append(0)
    return map

def move(c, m):
    x = c[0]
    y = c[1]
    x2 = c[2]
    y2 = c[3]
    dy = y2 - y
    dx = x2 - x
    if dy < 0:
        if dx < 0:
            while x >= x2:
                m[y][x] += 1
                x -= 1
                y -= 1
        elif dx > 0:
            while x <= x2:
                m[y][x] += 1
                x += 1
                y -= 1
        else:
            while y >= y2:
                m[y][x] += 1
                y -= 1
    elif dy > 0:
        if dx < 0:
            while x >= x2:
                m[y][x] += 1
                x -= 1
                y += 1
        elif dx > 0:
            while x <= x2:
                m[y][x] += 1
                x += 1
                y += 1
        else:
            while y <= y2:
                m[y][x] += 1
                y += 1
    else:
        if dx < 0:
            while x >= x2:
                m[y][x] += 1
                x -= 1
        elif dx > 0:
            while x <= x2:
                m[y][x] += 1
                x += 1
    return


def task1(f):
    m = f[1]
    coords = f[0]
    map = mapper(m + 1)
    for c in coords:
        if c[0] == c[2] or c[1] == c[3]:
            move(c, map)
    count = 0
    for y in map:
        for x in y:
            if x > 1:
                count += 1
    print(count) #5.1

def task2(f):
    m = f[1]
    coords = f[0]
    map = mapper(m + 1)
    for c in coords:
        move(c, map)
    count = 0
    for y in map:
        for x in y:
            if x > 1:
                count += 1
    print(count) #5.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()