import itertools
import libchall as lc
import re

def p1():
    print sum([r for r in xrange(1,1000) if ((r%3==0) or (r%5==0))])

def p2():
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    print a

def p3():
    print lc.sieve_of_eratosthenes(600851475143)[-1:]

def p4():
    largest = 0
    for a in xrange(999,100,-1):
        for b in xrange(999,100,-1):
            tc = a*b
            if lc.is_palindrome(tc):
                if tc > largest: largest = tc
    print largest

def p5():
    found = False
    min = 1
    max = 20
    n = 2
    while found == False:
        divisible = True
        for d in xrange(min,max+1):
            if n % d > 0:
                divisible = False
                break
        if divisible:
            found = True
            break
        n += 1
    print n

def p6():
    sum_squares = 0
    square_sums = 0
    min = 1
    max = 100
    for i in xrange(min,max+1):
        sum_squares += i**2
        square_sums += i
    print square_sums**2 - sum_squares

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

def p9():
    found = False
    c = 2
    while not found:
        for a in xrange(1,c**1/2):
            if found: break
            for b in xrange(a+1,c):
                if a**2 + b**2 == c**2:
                    if a+b+c == 1000:
                        found = True
                        print a,b,c
                        break
        c += 1

def p10():
    print sum(lc.sieve_of_eratosthenes(2*10**6))

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
            h = v = d = b = 1
            try:
                for i in range(4):
                    h *= T[y][x+i]
                    v *= T[y+i][x]
                    d *= T[y+i][x+i]
                    b *= T[y+i][x-i]
            except: pass
            for i in [h,v,d,b]:
                if i > max:
                    max = i
    print max

def p12():
    start = 1
    pivot = 2
    stop = 3
    chunk = 10
    goal = 25
    found = False
    while not found:
        if len(lc.divisors(stop)) < goal:
            start = stop + 1
            stop *= 2
            pivot = (stop-start) // 2

def p14():
    longestSequence = [0,0]
    limit = 10**6
    for i in range(1,limit):
        l = len(lc.collatz_seq(i))
        if l > longestSequence[0]:
            longestSequence = [l,i]
    print longestSequence

def p21():
    limit = 10000
    answer = []
    for n in xrange(1,limit):
        A = sum(lc.divisors(n))
        B = sum(lc.divisors(A))
        if n == B and n <> A:
            answer.append(n)
    print sum(answer)

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

def p32():
    P = itertools.permutations(list('123456789'))
    T = [''.join(p) for p in P]
    R = []
    for t in T:
        for x in xrange(1,len(t)+1):
            c = t[x*-1:]
            B = t[:x*-1]
            if c in R: continue
            for y in xrange(1,len(B)+1):
                a = B[y*-1:]
                b = B[:y*-1]
                if 0 in [len(a),len(b),len(c)]: continue
                if int(a) * int(b) == int(c):
                    R.append(c)
    print sum([int(r) for r in R])

# def p35():
#     T = lc.sieve_of_eratosthenes(1000000)
#     print T[-1]
#     C = 0
#     for t in T:
#         perms = itertools.permutations(str(t))
#         P = [''.join(p) for p in perms]
#         circular = True
#         n = 0
#         for p in P:
#             if int(p) in T:
#                 n += 1
#             else:
#                 circular = False
#                 break
#         if circular:
#             C += n
#             print p
#         else:
#             print 'not', t
#     print C, len(T)

def p35():
    T = lc.sieve_of_eratosthenes(1000000)
    S = [sorted(str(p)) for p in T]
    C = []
    for s in S:
        if S.count(s) == len(s):
            C.append(str(s))
    print sorted(str(c) for c in C)
    print len(C)




p35()
