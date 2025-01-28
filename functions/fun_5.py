a = 10
print(id(a))
def something():
    a = 15
    x = globals()['a']
    print(id(x))
    print('Inside',a)
    print('x is ', x)
    globals()['a'] = 22
something()


print('Outside',a)    # Preference is always given to local variable 
