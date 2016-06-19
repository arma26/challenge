# Level 1

```
level1@io:~$ ls -alh /levels/level01
-r-sr-x--- 1 level2 level1 1.2K Jan 13  2014 /levels/level01
$  file /levels/level01
/levels/level01: setuid ELF 32-bit LSB executable ...
```

setuid bit is set ... so this binary will probably escalate me to another user
with strings I see
```
$ strings /levels/level01
Enter the 3 digit passcode to enter: Congrats you found it, now read the password for level2 from
/bin/sh
```

guessing it'll call sh when I enter the correct password

```
gdb /levels/level01
(gdb) disassemble main
Dump of assembler code for function main:
  0x08048080 <+0>:	push   $0x8049128
  0x08048085 <+5>:	call   0x804810f
  0x0804808a <+10>:	call   0x804809f
  0x0804808f <+15>:	cmp    $0x10f,%eax
  0x08048094 <+20>:	je     0x80480dc
  0x0804809a <+26>:	call   0x8048103
```
so jump if eax is equal to 0x10f

Google 0x10f, one of the first results says `Decimal: 271` Great, a 3 digit number
```
level1@io:~$ /levels/level01
Enter the 3 digit passcode to enter: 271
Congrats you found it, now read the password for level2 from /home/level2/.pass
sh-4.3$
```
I'm not in a new shell, lets see what changed
```
sh-4.3$ id
uid=1001(level1) gid=1001(level1) euid=1002(level2) groups=1001(level1),1029(nosu)
```

now lets read that file

```
sh-4.3$ cat /home/level2/.pass
XNWFtWKWHhaaXoKI
```
