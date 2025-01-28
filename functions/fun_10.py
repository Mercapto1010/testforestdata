# Factorial of a number using a recursion
def fact(n):
        if n == 0:
                return 1
        
        return n * fact(n-1)

num = int(input("Enter number"))
result = fact(num)
print(result)