import math

def read_file():
    a = []
    f = open("inputd17", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    a = f[0].split()
    xr = a[2][2:-1]
    yr = a[3][2:]
    x = xr.split("..")
    y = yr.split("..")
    return (int(x[0]),int(x[1]),int(y[0]),int(y[1]))

def play_x(p,v):
    p += v
    v = max(0, v-1)
    return (p,v)

def play_y(p,v):
    p += v
    v -= 1
    return (p,v)

def task1(f):
# x-velocity doesn't affect max y-position
# 8+7+6+..+1 is a arithmetic series from 1 to 8
# y-track up corresponds y-track down, max speed
# max y-pos when max-speed down when next hits target's low point
    v = -1 * f[2] - 1
    max_y = int( (v * v + v) / 2)
    print(max_y) #17.1

def task2(f):
    x_speeds = set()
    y_speeds = set()
    acceptables = set()
    x_min = math.ceil((-1 + math.sqrt(8 * f[0])) / 2)
    x_max = f[1]
    y_min = f[2]
    y_max = -1 * f[2] - 1
    for vel in range(x_min,x_max+1):
        pos = 0
        v = vel
        while pos < f[0]:
            pos,v = play_x(pos,v)
        if pos <= f[1] and pos >= f[0]:
            x_speeds.add(vel)
    for vel in range(y_min,y_max+1):
        pos = 0
        v = vel
        while pos > f[3]:
            pos,v = play_y(pos,v)
        if pos <= f[3] and pos >= f[2]:
            y_speeds.add(vel)
    for x in x_speeds:
        for y in y_speeds:
            v_x = x
            v_y = y
            pos_x = 0
            pos_y = 0
            while pos_y > f[2]:
                pos_x, v_x = play_x(pos_x, v_x)
                pos_y, v_y = play_y(pos_y, v_y)
                if pos_x <= f[1] and pos_x >= f[0] and pos_y <= f[3] and pos_y >= f[2]:
                    acceptables.add((x,y))
    print(len(acceptables)) #17.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()