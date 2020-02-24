t=list(map(str,input().split()))
c=[t[0]]
for i in range(len(t)):
    for j in range(0,len(t)):
        if c[i][-1]==t[j][0]:
            c.append(t[j])
            t.remove(t[j])
            t.insert(j,"0")
            break
print(c)
