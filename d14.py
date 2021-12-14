def read_file():
    a = []
    f = open("inputd14", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    org = f[0]
    rules = dict()
    letset = set(list(org))
    for i in range(2,len(f)):
        rule = f[i].split(" -> ")
        letset.add(rule[1])
        rules.update({rule[0]: (rule[0][0] + rule[1], rule[1] + rule[0][1])})
    return (org, rules, letset)

def most_minus_least(f, n):
    polymer = f[0]
    rules = f[1]
    letset = f[2]
    counter = dict.fromkeys(rules.keys(), 0)
    s_counter = dict.fromkeys(letset, 0)
    for l in list(polymer):
        s_counter.update({l: s_counter[l] + 1})
    for i in range(1, len(polymer)):
        c = polymer[i-1:i+1]
        if c in counter.keys():
            counter.update({c: counter[c] + 1})
    for step in range(n):
        nd = counter.copy()
        for p in counter.keys():
            c = counter[p]
            if c == 0:
                continue
            p1 = rules[p][0]
            p2 = rules[p][1]
            nd.update({p1: nd[p1] + c})
            nd.update({p2: nd[p2] + c})
            nd.update({p: nd[p] - c})
            l = p1[1]
            s_counter.update({l: s_counter[l] + c})
        counter = nd
    counts = list(s_counter.values())
    counts.sort()
    return (counts[-1] - counts[0])

def task1(f):
    answer = most_minus_least(f, 10) #asked after 10 steps
    print(answer) #14.1

def task2(f):
    answer = most_minus_least(f, 40) # asked after 40 steps
    print(answer) #14.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()