from collections import Counter
import libchall as lc
import re
import urllib

def the_beginning():
    T = [
    'bitwarrior',
    'LameStartup',
    'HiddenIsConfig',
    'AndIknowchown',
    'OhRightThePerms']
    print ','.join(T)

def encodings_i():
    T = '10101001101000110100111100110100' \
    '00011101001100101111100011101000'  \
    '10000011010011110011010000001101'  \
    '11010110111000101101001111010001'  \
    '00000110010111011101100011110111'  \
    '11100100110010111001000100000110'  \
    '00011110011110001111010011101001'  \
    '01011100100000101100111011111110'  \
    '10111100100100000111000011000011'  \
    '11001111100111110111110111111100'  \
    '10110010001000001101001111001101'  \
    '00000110010111000011110011111100'  \
    '11110011111010011000011110010111'  \
    '0100110010111100100101110'

    print ''.join([chr(int(T[i:i+8],2)) for i in xrange(len(T))])

def crypto_substitution_i():
    T = 'WA GJZ UQTDPJGA PHM AHR KUY IZUM GJDB TA XIDZYM D UT DTEIZBBZM FZIA LZQQ MHYZ AHRI BHQRGDHY NZA DB UBMXYWEYPMDK GJDB QDGGQZ KJUQQZYPZ LUB YHG GHH JUIM LUB DG'
    for i in xrange(26):
        print lc.rot_n_phrase(T,i)

def crypto_ceasar_ii():
    T = '41 69 69 5E 20 64 69 5C 26 20 73 69 6F 20 6D 69 ' \
    '66 70 5F 5E 20 69 68 5F 20 67 69 6C 5F 20 5D 62 ' \
    '5B 66 66 5F 68 61 5F 20 63 68 20 73 69 6F 6C 20 ' \
    '64 69 6F 6C 68 5F 73 28 20 4E 62 63 6D 20 69 68 ' \
    '5F 20 71 5B 6D 20 60 5B 63 6C 66 73 20 5F 5B 6D ' \
    '73 20 6E 69 20 5D 6C 5B 5D 65 28 20 51 5B 6D 68 ' \
    '21 6E 20 63 6E 39 20 2B 2C 32 20 65 5F 73 6D 20 ' \
    '63 6D 20 5B 20 6B 6F 63 6E 5F 20 6D 67 5B 66 66 ' \
    '20 65 5F 73 6D 6A 5B 5D 5F 26 20 6D 69 20 63 6E ' \
    '20 6D 62 69 6F 66 5E 68 21 6E 20 62 5B 70 5F 20 ' \
    '6E 5B 65 5F 68 20 73 69 6F 20 6E 69 69 20 66 69 ' \
    '68 61 20 6E 69 20 5E 5F 5D 6C 73 6A 6E 20 6E 62 ' \
    '63 6D 20 67 5F 6D 6D 5B 61 5F 28 20 51 5F 66 66 ' \
    '20 5E 69 68 5F 26 20 73 69 6F 6C 20 6D 69 66 6F ' \
    '6E 63 69 68 20 63 6D 20 6C 5C 5E 5D 61 67 5C 68 ' \
    '62 67 60 62 28'
    for n in xrange(128):
        shifted = []
        for c in T.split(' '):
            shifted.append(chr((int(c,16)+n)%256))
        print ''.join(shifted)

def crypto_ceasar_i():
    T = 'DRO AESMU LBYGX PYH TEWZC YFOB DRO VKJI NYQ YP MKOCKB KXN IYEB EXSAEO CYVEDSYX SC SONNCNLKCVBV'
    for i in xrange(25):
        print lc.rot_n_phrase(T,i)

def training_ascii():
    T = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 114, 108, 104, 112, 115, 99, 103, 108, 109, 112, 100, 102]
    print ''.join([chr(c) for c in T])

def prime_factor():
    answers = []
    T = 10**6
    while len(answers)<=1:
        if lc.is_prime(T) and lc.is_prime(lc.sum_digits(T)):
            answers.append(T)
        T += 1
    print answers

def encoding_url():
    T = '%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%70%6F%68%67%73%61%6C%72%6F%6F%6E%68%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21'
    print urllib.unquote(T)

encoding_url()
