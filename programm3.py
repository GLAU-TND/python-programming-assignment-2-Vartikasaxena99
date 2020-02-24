s=input()
l=list(s)
c=0
for i in range(len(l)):
    if(i<len(l)-2):
        if(l[i]=="1"):
            if(l[i+1]=="1" and l[i+2]=="0"):
                c=c+2
            elif(l[i+1]=="1" and l[i+2]=="1"):
                c=c+1
            else:
                pass
        elif(i==(len(1)-2)):
            if(l[i]=="1" and l[i]=="1"):
                c=c+2
print(c)
