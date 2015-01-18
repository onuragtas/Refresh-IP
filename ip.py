#!/usr/bin/python
#-*-coding:utf8-*-
 

import pexpect,time

 

child = pexpect.spawn('telnet 192.168.2.1');

child.expect('Escape.*');

child.sendline('root');

 

child.sendline("şifreniz"); # sifre yoksa child.sendline(""); olarak degistirin.

time.sleep(5)

child.sendline('kill `cat /var/run/ppp*.pid`m');

child.sendline('exit');

 

child.expect(pexpect.EOF);

 

print child.before;
