lst=[6,6,8,9,4,2,3]
ot=[]
for num in lst:
    if num>5:
        num+=1
        ot.append(num)
    else:
        num-=1
        ot.append(num)
print(ot)