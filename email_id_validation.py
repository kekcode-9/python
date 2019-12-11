#takes n no. of name and mail id pair as input: name <mail id> and if mail id is valid displays them on console

import re

def checkValid(s):
	check1=re.compile(r'^[a-zA-Z]([a-zA-Z0-9._-])*@([a-zA-Z]+)[.]{1}([a-zA-Z]{1,3})$')
	mo=check1.search(s)
	if mo==None:
		return False
	return True

def printInfo(str1,fl):
	nameregex=re.compile(r'[^<]+') #extracts everything before <
	mo1=nameregex.search(str1)
	n=mo1.group()
	mailregex1=re.compile(r'[<](\S)+[>]$') #extracts: <username@domainname.extension>
	mo2=mailregex1.search(str1)
	v=mo2.group()
	mailregex=re.compile(r'[^<](\S)+[^>]') #extracts everything inside <>
	mo3=mailregex.search(v)
	s=mo3.group()
	if checkValid(s)==True:
		fl.append(str1)


n=int(input())
list1=[]
final=[]
i=0
while n>0:
	str1=input()
	list1.append(str1)
	printInfo(list1[i],final)
	i=i+1
	n=n-1
for x in final:
	print (x)
