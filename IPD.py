import sh
import os
#https://github.com/karimAMG
#CopyRight : Karim Amougay
#notice : install packege sh
# python -m pip install sh

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EN = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLINK    = '\33[5m'
    CRED2    = '\33[91m'
    CVIOLETBG2 = '\33[105m'
    CBLUEBG2   = '\33[104m'
    CURL      = '\33[4m'


ip = "192.168.1."

def f10():
  for i in range(1,10+1):
    ip2 = ip+str(i)
    try:
      sh.ping(ip2,"-c 1")
      print "[+]",'\x1b[6;30;42m' + ip2 + '\x1b[0m',color.CBLINK,"Live",color.EN
    except:
     continue    
    
def f100():
  for i in range(1,100+1):
    ip2 = ip+str(i)
    try:
      sh.ping(ip2,"-c 1")
      print "[+]",'\x1b[6;30;42m' + ip2 + '\x1b[0m',color.CBLINK,"Live",color.EN
    except:
     continue
    
    
def f200():
  for i in range(100,200+1):
    ip2 = ip+str(i)
    try:
      sh.ping(ip2,"-c 1")
      print "[+]",'\x1b[6;30;42m' + ip2 + '\x1b[0m',color.CBLINK,"Live",color.EN
    except:
     continue
    

def ff00():
  for i in range(1,200+1):
    ip2 = ip+str(i)
    try:
      sh.ping(ip2,"-c 1")
      print "[+]",'\x1b[6;30;42m' + ip2 + '\x1b[0m',color.CBLINK,"Live",color.EN
    except:
     continue
    
    
def f500():
  for i in range(200,500+1):
    ip2 = ip+str(i)
    try:
      sh.ping(ip2,"-c 1")
      print "[+]",'\x1b[6;30;42m' + ip2 + '\x1b[0m',color.CBLINK,"Live",color.EN
    except:
     continue
os.system("clear")
print color.CURL+"============== IP Detecter ============="+color.EN
print color.CBLINK+color.CRED2+"#"*40+color.EN
print color.CBLINK+color.CRED2+">"*40+color.EN
print color.CBLINK+color.CRED2+"#"*40+color.EN
print color.HEADER,"    1./from 1     to 10",color.EN,color.OKGREEN,"\n     2./from 1     to 100",color.EN,color.HEADER,"\n     3./from 100   to 200",color.EN,color.WARNING,"\n     4./from 1     to 200",color.EN,color.HEADER,"\n     5./from 200   to 500",color.EN
print color.CBLINK+color.CRED2+"#"*40+color.EN
print color.CBLINK+color.CRED2+"<"*40+color.EN
print color.CBLINK+color.CRED2+"#"*40+color.EN
print color.CVIOLETBG2+" CopyRight : "+color.CBLUEBG2+" Karim Amougay "+color.EN+"\n\n"

n = input("Input> ")    

if n == 1:
  f10()
if n == 2:
  f100()
if n == 3:
  f200()
if n == 4:
  ff00()
if n == 5:
  f500()