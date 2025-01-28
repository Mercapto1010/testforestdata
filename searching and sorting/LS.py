#  LINEAR SEARCH

pos = -1
def search(list,n):
    i = 0
    # while i < len(list):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        # i += 1

    return False

list = [2,56,46,8,9,2]
n = 56

if search(list,n):
    print("Found it at ", pos+1 )

else:
    print("Not found!")