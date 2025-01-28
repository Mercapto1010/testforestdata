# FIBONACCI SERIES
def fib(n):
    if n <= 0:
        print("Enter valid number")
    else:    
        a = 0
        b = 1
        if n == 1:
            print(a)
        else:    
            print(a)
            print(b)
            for i in range(2,n):
                c = a+b
                a = b
                b = c
                if c <= n:
                    print(c)
                else:
                    break    

fib(int(input("enter the number")))    