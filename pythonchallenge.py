import libchall as lc
import pickle
import re
import urllib2

def zero():
    print 2**38

def map1():
    T = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    T = T.upper()
    for i in xrange(26):
        print i, lc.rot_n_phrase(T,i)
    print lc.rot_n_phrase('map'.upper(),24)

def ocr1():
    r = re.compile(r'[A-Za-z]')
    with open("files\pythonchallenge-ocr-input.txt", 'r') as f:
        for line in f:
            line = line.rstrip()
            if r.findall(line):
                print r.findall(line)

def equality():
    r = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
    answer = []
    with open("files\pythonchallenge-equality-input.txt", 'r') as f:
        for line in f:
            line = line.rstrip()
            if r.findall(line):
                answer += r.findall(line)
    print ''.join(answer)

def linkedlist():
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
    r = re.compile(r'\d+$')
    base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    next = '12345'
    n = 0
    while n < 400:
        response = urllib2.urlopen(base + next)
        html = response.read()
        digits = r.findall(html)
        if digits: next = ''.join(digits)
        n += 1
    next = str(int(next)/2)
    n = 0
    while n < 400:
        response = urllib2.urlopen(base + next)
        html = response.read()
        digits = r.findall(html)
        if digits:
            next = ''.join(digits)
        else:
            print html
            break
        n += 1

def peakhell():
    f = open('files\pythonchallenge-peakhell.jpg', 'r')
    T = pickle.load(f)
    f.close()
    for i in T: print i

peakhell()
