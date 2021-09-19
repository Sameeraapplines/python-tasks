

acount=0
ecount =0
icount=0
ocount=0
ucount=0
snt = input("enter a sentence\n")
for i in range(0,len(snt)):
    if snt[i]=='a':
     acount=acount+1
    elif snt[i]=='e':
      ecount=ecount+1
    elif snt[i]=='i':
     icount=icount+1
    elif snt[i]=='o':
     ocount=ocount+1
    elif snt[i]=='u':
     ucount=ucount+1
dict={}
dict['a'] = acount
dict['e'] = ecount
dict['i'] = icount
dict['o'] = ocount
dict['u'] = ucount


print("final solution is: ", dict)
