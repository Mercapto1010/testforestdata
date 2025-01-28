def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('Yash', age= 20, city= 'Delhi', mob= 8090)    
