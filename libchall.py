def morse(c):
    alphabet = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
    }
    return alphabet[c]

def morse_phrase(S):
    return ''.join([morse(c) for c in S.split(' ')])

def sum_digits(n):
    a = list(str(n))
    r = 0
    for x in a:
        r += int(x)
    return r

def rot_n(s,shift,d=False):
    A = [chr(65+x) for x in xrange(26)]
    B = [chr(65+((x+shift)%26)) for x in xrange(26)]
    C = [chr(97+x) for x in xrange(26)]
    D = [chr(97+((x+shift)%26)) for x in xrange(26)]
    r = []
    for c in s:
        oc = ord(c)
        try:
            if (oc >= 65 and oc <= 90) and d: r += B[A.index(c)]
            elif (oc >= 65 and oc <= 90) and not d: r += A[B.index(c)]
            elif (oc >= 97 and oc <= 122) and d: r += D[C.index(c)]
            elif (oc >= 97 and oc <= 122) and not d: r += C[D.index(c)]
            else: r += c
        except: pass
    return ''.join(r)

def rot_n_phrase(s,shift,d=False):
    return ' '.join([rot_n(w,shift,d) for w in s.split(' ')])

def divisors(n):
    return [d for d in xrange(1,n/2+1) if n % d == 0] + [n]

def url_decode(s):
    return urllib.unquote(s)

def matrix3(m):
    return reduce(lambda a,b: (a[0]*b[0] + a[1]*b[1], a[0]*b[1] + a[1]*b[2], a[1]*b[1] + a[2]*b[2]),m)

def matrix3power(m,n):
    if n == 1: return m
    halves = matrix3power(m,n//2)
    if n%2 == 0:
        return matrix3((halves,halves))
    else:
        return matrix3((halves,halves,m))

# http://raganwald.com/2015/12/20/an-es6-program-to-compute-fibonacci.html
def fib_n(n):
    return n if n < 2 else matrix3power((1,1,0),n-1)[0]

def fib(limit):
    return [fib_n(r) for r in xrange(1,limit+1)]

def is_palindrome(s):
    T = str(s)
    r = True
    for i,c in enumerate(T):
        if T[i] <> T[i*-1-1]:
            r = False
            break
    return r

def is_prime(n):
    p_under_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    return n in [p_under_100,sieve_of_eratosthenes(n)]

def sieve_of_eratosthenes(max):
    answers = [True for i in xrange(max+1)]
    for i,v in enumerate(answers):
        if v == False or i in [0,1]: continue
        n = 2
        while i*n <= max:
            if answers[i*n]: answers[i*n] = False
            n += 1
    return [i for i,v in enumerate(answers) if v == True][2:]

def factorial(n):
    r = 1
    for i in xrange(n,1,-1):
        r *= i
    return r

def triangle(n):
    r = 0
    for i in xrange(n+1):
        r += i
    return r

def collatz_seq(n):
    r = [n]
    while n > 1:
        if n % 2 == 0: n /= 2
        else: n = 3 * n + 1
        r.append(n)
    return r

def is_pandigital(n):
    return sorted(str(n)) == list('123456789'[:len(n)])

# import timeit
# import __builtin__
# __builtin__.__dict__.update(locals())
# print timeit.timeit('is_prime(10000)','',number=1000)
