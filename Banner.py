#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import time
import sys

os.system('apt update')
os.system('apt upgrade -y')
os.system('pkg install figlet -y')
os.system('pkg install ncurses-utils -y') 
os.system('pkg install ruby -y')
os.system('gem install lolcat')

output = '/data/data/com.termux/files/usr/etc/'

print('')
name = raw_input('Input your Name : ')

wlc = '''
import os,sys,time,random
print("")
print("")
color = ["\\033[1;31m","\\033[1;32m"]
m = random.choice(color)+"Welcome {} \\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
'''.format(name)

h1 = open(output+'wlc.py', 'w')
h1.write(wlc)
h1.close()

bashrc1 = '''
clear
echo
echo "
   ♡ ━━━━━━━━━ [♛] 𝐓 𝐄 𝐑 𝐌 𝐔 𝐗 [♛] ━━━━━━━━━━━━ ♡ " |lolcat
echo
    echo "  𝚆𝚎 𝑨𝒓𝒆 𝔸𝕟𝕠𝕟𝕪𝚖𝚘𝚞𝚜𝚎" |lolcat
'''

bashrc2 = '''
echo "
             𝐖𝐞 𝐃o 𝐍0𝙩 𝗛@𝗰𝙆 𝙩𝙤 𝖨𝗆𝗉𝗋𝖾𝗌𝗌.
                            𝐖𝐞 𝗛@𝗰𝙆 𝘛𝘰 𝑬𝒙𝒑𝒓𝒆𝒔𝒔.
   ♡ ━━━━━━━━━━━ [♛] 𝐌𝐫.ERR0R [♛] ━━━━━━━━━━━━ ♡ " |lolcat
   
   #PS1="\\033[1;31mERR0R~#"

PS1="\[\e[1;34m┌──\\a─T─I─M─E─\\a──┐\\033[1;34m\\a┌──\\a─D─A─T─E─\\a───➘\\033[1;34m
\\a┌─[\\033[1;93m \@\\033[1;34m ] ☠ [\\033[1;93m \d\\033[1;34m ]\\033[1;34m
\\a├─[\\033[1;32m\w\\033[1;34m]\\033[1;34m
'''

h2 = open(output+'bash.bashrc', 'w')
h2.write(bashrc1)
h2.write("\nfiglet    '    "+name+"' |lolcat\n")
h2.write(bashrc2)
h2.write('\[\e[34m\]└──━≫\[\e[35m\]'+name+'\[\e[34m\][⇶]:➔\[\e[1;32m\] "\n')
h2.write('echo -e "\e[6 q"')
h2.close()
print('DONE')

