num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if((num1>num2)&(num1>num3)):
    print(num1,"is the greatest")
elif(num2>num3):
    print(num2, "is the greatest")
else:
    print(num3,"is gretest")
