def read_file():
    a = []
    f = open("inputd16", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    a = f[0] #avoid missing lead zeros
    a = a.replace("0","0000")
    a = a.replace("1","0001")
    a = a.replace("2","0010")
    a = a.replace("3","0011")
    a = a.replace("4","0100")
    a = a.replace("5","0101")
    a = a.replace("6","0110")
    a = a.replace("7","0111")
    a = a.replace("8","1000")
    a = a.replace("9","1001")
    a = a.replace("A","1010")
    a = a.replace("B","1011")
    a = a.replace("C","1100")
    a = a.replace("D","1101")
    a = a.replace("E","1110")
    a = a.replace("F","1111")
    return a

def analyzer(f):
    if len(f) == 0: return (0,0,0,"")
    ver = int(f[0:3],2)
    pid = int(f[3:6],2)
    val = -1
    versum = ver
    left = ""
    v0 = 0
    v1 = 1
    v2 = 9999999999999999
    v3 = -1
    v567 = []
    if pid == 4:
        ch = 6
        while f[ch] == "1":
            ch += 5
        value = list(f[6:ch+5])
        del value[::5]
        value = "".join(value)
        val = int(value,2)
        left = f[ch+5:]
        return (ver,pid,val,left)
    else:
        if f[6] == "0":
            l = int(f[7:22],2)
            left = f[22:22+l]
            rleft = f[22+l:]
            while len(left) > 0:
                subs = analyzer(left)
                versum += subs[0]
                left = subs[3]
                val = subs[2]
                v0 += val
                v1 *= val
                if val < v2: v2 = val
                if val > v3: v3 = val
                v567.append(val)
            left = rleft
        else:
            l = int(f[7:18],2)
            counts = 0
            left = f[18:]
            while counts < l:
                ver = analyzer(left)
                versum += ver[0]
                left = ver[3]
                counts += 1
                val = ver[2]
                v0 += val
                v1 *= val
                if val < v2: v2 = val
                if val > v3: v3 = val
                v567.append(val)
    if pid == 0:
        val = v0
    elif pid == 1:
        val = v1
    elif pid == 2:
        val = v2
    elif pid == 3:
        val = v3
    elif pid == 5:
        if v567[0] > v567[1]:
            val = 1
        else:
            val = 0
    elif pid == 6:
        if v567[0] < v567[1]:
            val = 1
        else:
            val = 0
    elif pid == 7:
        if v567[0] == v567[1]:
            val = 1
        else:
            val = 0
    return (versum,pid,val,left)

def task1(f):
    v = analyzer(f)
    print(v[0]) #16.1

def task2(f):
    v = analyzer(f)
    print(v[2]) #16.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()