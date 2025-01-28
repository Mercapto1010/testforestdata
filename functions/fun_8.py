# TO FIND THE FACTORIAL OF A NUMBER
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

x = int(input("Enter any number t finds its factorial!"))
# x = 5
result = fact(x)
print(result)