# COUNT THE NUMBER OF EVEN AND ODD
entry = (input ('Enter the list using space'))
lst = list(map(int, entry.split()))
# lst = [25,14,26,49,44]
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd
even, odd = count(lst)
print(even)
print(odd)