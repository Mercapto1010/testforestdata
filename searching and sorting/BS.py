#  BINARY SEARCH

pos = -1
def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

list = [2,5,10,12,55,999,9999,10987,305405]
n = 305405

if search(list,n):
    print("Found it at ", pos+1 )

else:
    print("Not found!")