import libchall as lc
import re

def p1():
    r = []
    for i in xrange(1,1000):
        if (i%3 == 0) or (i%5 == 0): r.append(i)
    print sum(r)

def p2():
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    print a

def p8():
    J = []
    with open('files\euler8.txt', 'r') as f:
        for line in f:
            for c in line.strip('\n'):
                J.append(c)
    J = ''.join(J)
    max=0
    for i in range(len(J)-13):
        T = 1
        for n in range(14)[1:]:
            T *= int(J[i+n])
        if T > max:
            max = T
    print max

def p11():
    T = []
    z = [[0 for x in range(20)] for x in range(20)]
    with open('files\euler11.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            T.append([int(i) for i in line.split(' ')])
    max = 0
    for y,a in enumerate(T):
        for x,b in enumerate(a) :
            h = v = d = d2 = 1
            try:
                for i in range(4):
                    h *= T[y][x+i]
                    v *= T[y+i][x]
                    d *= T[y+i][x+i]
                    d2 *= T[y+i][x-i]
            except: pass
            for i in [h,v,d,d2]:
                if i > max:
                    max = i
    print max

def p14():
    maxN = 0
    maxC = 0
    for i in range(1,10**6):
        T = i
        c = 0
        while T > 1:
            if T % 2 == 0: T /= 2
            else: T = 3*T + 1
            c += 1
        if c > maxC:
            maxC = c
            maxN = i
    print maxN, maxC

def value(s):
    r = 0
    for c in s:
        r += ord(c)-64
    return r

def p22():
    names = []
    with open('files\euler22.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            m = re.compile(r'\w+')
            names = sorted(m.findall(line))
    combined = []
    total_score = 0
    for i,n in enumerate(names):
        i += 1
        combined.append([i,n,i*value(n)])
    for i in combined:
        total_score += i[2]
    print total_score
p22()
