low_coords = []

def read_file():
    a = []
    f = open("inputd09", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    numbers = []
    for i in f:
        row = [int(x) for x in i]
        row.append(10)
        numbers.append(row)
    numbers.append([10 for x in range(len(numbers[0]))])
    return numbers

def check_co(f, c, l):
    x = c[0]
    y = c[1]
    no = f[y][x]
    l.add(c)
    up = f[y-1][x]
    down = f[y+1][x]
    left = f[y][x-1]
    right = f[y][x+1]
    if up > no and up < 9:
        check_co(f, (x,y-1), l)
    if down > no and down < 9:
        check_co(f, (x,y+1), l)
    if left > no and left < 9:
        check_co(f, (x-1,y), l)
    if right > no and right < 9:
        check_co(f, (x+1, y), l)
    return l


def task1(f):
    low_points = []
    global low_coords
    y_len = len(f) - 1
    x_len = len(f[0]) - 1
    for y in range(y_len):
        for x in range(x_len):
            no = f[y][x]
            up = f[y-1][x]
            down = f[y+1][x]
            left = f[y][x-1]
            right = f[y][x+1]
            if no < up and no < down and no < left and no < right:
                low_points.append(no)
                low_coords.append((x, y))
    risk = [n+1 for n in low_points]
    print(sum(risk)) #9.1

def task2(f):
    global low_coords
    basins = list()
    for i in low_coords:
        basins.append(check_co(f, i, set()))
    basins.sort(key=len)
    print(len(basins[-1]) * len(basins[-2]) * len(basins[-3])) #9.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()