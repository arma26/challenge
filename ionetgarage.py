## level1
#
# level1@io:~$ ls -alh /levels/level01
# -r-sr-x--- 1 level2 level1 1.2K Jan 13  2014 /levels/level01
#
# setuid bit is set ... so this file will probably escalate me to another user
#
# $  file /levels/level01
# /levels/level01: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
# $ strings /levels/level01
#
# notice the string:
#   # Enter the 3 digit passcode to enter: Congrats you found it, now read the password for level2 from /home/level2/.pass
# also notice "/bin/sh", guessing it'll call sh when I enter the correct password
#
# gdb /levels/level01
# (gdb) disassemble main
# Dump of assembler code for function main:
#    0x08048080 <+0>:	push   $0x8049128
#    0x08048085 <+5>:	call   0x804810f
#    0x0804808a <+10>:	call   0x804809f
#    0x0804808f <+15>:	cmp    $0x10f,%eax # test if eax == 0x10f, jump if equal
#    0x08048094 <+20>:	je     0x80480dc
#    0x0804809a <+26>:	call   0x8048103
#
# google 0x10f, a site that that says Decimal: 271
#
# level1@io:~$ /levels/level01
# Enter the 3 digit passcode to enter: 271
# Congrats you found it, now read the password for level2 from /home/level2/.pass
#
# sh-4.3$ id
# uid=1001(level1) gid=1001(level1) euid=1002(level2) groups=1001(level1),1029(nosu)
#
# sh-4.3$ cat /home/level2/.pass
# XNWFtWKWHhaaXoKI
