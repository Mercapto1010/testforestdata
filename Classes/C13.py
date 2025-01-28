
try:
    a = int((input("phla number daal!")))
    b = int((input("dusra number daal!")))
    print(a/b)

except ZeroDivisionError as e:
    print("Zero se divide nhi krne ka bidu!!")

except ValueError as e:
    print("Aye bidu number daal na! ")

except Exception as e:
    print("Pta nhi konsa error hai")

print("Kuchh bhi ho apun to aayega")