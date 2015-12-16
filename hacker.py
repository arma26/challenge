import libchall
import urllib

def a_few_percent():
    T = '%66%75%67%6C%79'
    print urllib.unquote(T)

def xor_eval():
    print 17 ^ 39 ^ 11

def counting():
    T = 'eehxhqpmawoewdffplqrturxdjlsaylymgxjsthjpacyuxnpuvqlezhosbnmmjzeeahjll'\
    'nacofwyxxrelwgadsmolyynahrfvqkqonkgjsazwczwbayptsnsuvyomalyisyroxbivlqvtalt'\
    'vjwtqbsbnscqmdcwxxdkvwctbynbvokdcovbebokjlmekezpcnoxvzzpaqhusdhgbhtqzeuoegy'\
    'lofircjlxdypcvekkllxjxlynidhgngtpblebyoazqvoccnhauwcsviqlbzsmyrproffqapjtizl'\
    'rdasradufbjwhkllykgtrqivlrsrwswzdwjuktqgzkyslucqxgtseafofbhvhltparprjunrsivy'\
    'hmelkkodvukwkoiwmhunbjmhtrvowapwuvogjqcaxwepbxoynhygxsqmbcavzvfydrptedyvbzrq'\
    'ficmrobquqvtcjoclyedsafxlhlmyxeyeumiswjjzdxxdqccyqvobspwhsmazmabshscmlquplbm'\
    'hvvuiuasmjjajwyoyezgvxhpfteblvcuxhuosoekqtiobyvbdytyycyesmzkvbcupnbp'
    print len(T)

def basic():
    # todo FEEX
    T = list('28679718602997181072337614380936720482949')
    test = libchall.base_n(T,7)
    answer = '532005663005364261216414503026065341004024261231'
    print test,answer
    if test == answer: print 'pass'

def who_goes_there():
    username = 'username'
    print username[::-1]

def dit_dah():
    T = '- .... . .- -. ... .-- . .-. .. ... .... --- .- .-. ... .'
    libchall.morse_phrase(T)

def didactic_byte():
    T = 233
    print hex(T)

def didactic_bytes():
    T = [199, 77, 202]
    for t in T: print hex(t)

def didactic_text():
    T = '''But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, is far above our poor power to add or detract. The world will little note, nor long remember what we say here today, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the brave unfinished work which they who fought here have thus far so nobly advanced. It is rather for us solvers to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''
    o = '''But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''
    T = T.split(' ')
    o = o.split(' ')

    offset = 0
    for i in xrange(len(T)):
        try:
            if T[i-offset] <> o[i]:
                print T[i]
                offset += 1
        except:
            pass
didactic_text()
