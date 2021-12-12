def read_file():
    a = []
    f = open("inputd12", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    c = dict()
    for i in f:
        r = i.split("-")
        if r[0] in c.keys():
            n = c[r[0]]
            n.add(r[1])
            c.update({r[0]: n})
        else:
            c.update({r[0]: {r[1]}})
        if r[1] in c.keys():
            n = c[r[1]]
            n.add(r[0])
            c.update({r[1]: n})
        else:
            c.update({r[1]: {r[0]}})
    return c

def walk_thru(cave, ways, visited, doors):
    if cave == "end":
        ways.append(",".join(visited))
        return
    for nc in doors[cave]:
        if nc.islower() and nc in visited:
            continue
        visited.append(nc)
        walk_thru(nc, ways, visited, doors)
        visited.pop()
    return

def walk_thru2(cave, ways, visited, doors, used):
    if cave == "end":
        ways.add(",".join(visited))
        return
    for nc in doors[cave]:
        if nc == "start":
            continue
        if used:
            if nc.islower() and nc in visited:
                continue
        else:
            if nc.islower() and visited.count(nc) >= 2:
                continue
        if nc.islower() and nc in visited:
            used = True
        visited.append(nc)
        walk_thru2(nc, ways, visited, doors, used)
        if nc.islower() and visited.count(nc) == 2 and visited[-1] == nc:
            used = False
        visited.pop()
    return

def task1(f):
    ways = []
    visited = ["start"]
    for nc in f["start"]:
        visited.append(nc)
        walk_thru(nc, ways, visited, f)
        visited.pop()
    print(len(ways)) #12.1

def task2(f):
    ways = set()
    visited = ["start"]
    for nc in f["start"]:
        visited.append(nc)
        walk_thru2(nc, ways, visited, f, False)
        visited.pop()
    print(len(ways)) #12.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()