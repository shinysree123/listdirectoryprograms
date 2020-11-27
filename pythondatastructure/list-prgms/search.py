lst=[23,56,3,45,6778,78,788]
search=int(input("enter the search element"))
for num in lst:
    if(search==num):
        print(num,"search element is found")
    else:
        print("not found")