limit=int(input("enter the limit"))
oddlst=list()
evenlst=list()
for i in range(1,limit+1):
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print(oddlst)
print(evenlst)