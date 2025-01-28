# ITS NOT RIGHT WAY TO PRINT THIS PATTERN(condition is to use # at once)
# i = 1
# while i<=4:
#     print("#",  end=" ")
#     j = 1
#     while j<=3:
#        print("# ", end= "")
#        j = j+1
#     i = i+1
#     print()


# for i in range(4):
#     for j in range(4):
#         print("# ", end="")

#     print()    

for i in range(4):
    for j in range(i+1):
        print("# ", end="")

    print()


# for i in range(4):
#     for j in range(4-i):
#         print("# ", end="")

#     print()