x = [115,13,42,89,66]

for y in x:
    if y%5 == 0:
        print(y)
        break
else:           # else can come in the indention of for 
    print("not found")