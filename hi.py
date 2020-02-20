i = int(input("enter no: "))
if i >=10:
    for j in range(10, i):
        if j % 2 == 0:
            print(j, "even no")
        else:print(j, "odd no")
else: print("not valid no")