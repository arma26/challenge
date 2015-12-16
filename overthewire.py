'''
bandit.labs.overthewire.org
0 bandit0
12 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
16 cluFn7wTiGryunymYOu4RcffSxQluehd
18 kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
19 IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
20 GbKksEFF4yrVs6il55v6gwY5aVje5f0j
21 gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
22 Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
23 jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
24 UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
25 uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
26 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

leviathan.labs.overthewire.org
0 leviathan0
1 leviathan0
2 rioGegei8m

http://natas0.natas.labs.overthewire.org
0 natas0
1 gtVrDuiDfck831PqWsLEZy5gyDz1clto
2 ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
'''

import codecs
import libchall as lc
import string

def bandit11():
    T = '5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
    print codecs.encode(T, 'rot_13')

def krypton2():
    T = 'OMQEMDUEQMEK'
    T2 = ['IMATEST','UYMFQEF']
    for i in xrange(26):
        if lc.rot_n(T2[0],i) == T2[1]:
            print i
    print lc.rot_n(T,14,True)


def get(fn):
    r = []
    with open(fn,'r') as f:
        for line in f:
            line = line.rstrip()
            r.append(line)
    return r

def krypton3():
    sub = ['JDSQNGWCBKV','thearndiowl']
    trans = string.maketrans(sub[0], sub[1])
    R = [x.translate(trans) for x in get('files\krypton3-2.txt')]
    Z = [x.translate(trans) for x in get('files\krypton3-3.txt')]
    T = [x.translate(trans) for x in get('files\krypton3-found.txt')]
    W = [x.translate(trans) for x in get('files\krypton3-enc.txt')]
    for i in [T,Z,R,W]:
        print ''
        print ' '.join(i)
    # doubles UU VV

krypton3()
