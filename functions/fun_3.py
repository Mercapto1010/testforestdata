# def person(name, age):
#     print(name)
#     print(age)

# person('Yash', 20)

def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)    
sum(23,44,5,6,7)