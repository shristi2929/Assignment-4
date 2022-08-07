def add(x):
    return lambda num: x+num
num=int(input("enter any number to add with 25:"))
result=add(25)
print("Result:",result(num))