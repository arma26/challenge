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
    s = S.split(' ')
    print ''.join([morse(c) for c in s])


# def base_n(s,base):
#     r = []
#     for c in s[::-1]:
#         t = int(c)
#         while t >= 0:
#             if t <= base-1:
#                 r.append(t)
#             else:
#                 r.append(base-1)
#             t -= base-1
#     return ''.join([str(c) for c in r])

def base_n(s,base):
    t = int(s)
    return str(t)

def sum_digits(n):
    a = list(str(n))
    r = 0
    for x in a:
        r += int(x)
    return r

def is_prime(n):
    p_under_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    if n in p_under_100: return True
    if n < 2: return False
    state = 1
    while state <> -1 and state <> 0:
        if state == 1:
            state = 2
            m = n%10
            if m%2 == 0:
                state = -1
        elif  state == 2:
            state = 3
            if sum_digits(n) % 3 == 0:
                state = -1
        elif state == 3:
            state = 4
            limit = int(n**0.5)+1
            for x in xrange(4,limit):
                if n % x == 0:
                    state = -1
                    break
        elif state == 4:
            state = 0
    if state == -1: return False
    if state == 0: return True

def rot_n(s,shift,d=False):
    A = [chr(65+x) for x in xrange(26)]
    B = [chr(65+((x+shift)%26)) for x in xrange(26)]
    r = []
    for c in s:
        try:
            if d: r += B[A.index(c)]
            else: r += A[B.index(c)]
        except: pass
    return ''.join(r)

def rot_n_phrase(s,shift,d=False):
    return ' '.join([rot_n(w,shift,d) for w in s.split(' ')])

def url_decode(s):
    return urllib.unquote(s)

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
