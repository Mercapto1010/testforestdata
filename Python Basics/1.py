a = 5 #101
b = 6 #110
# temp = a
# a = b
# b = temp
# a = a + b #11
# b = a - b #5
# a = a - b #6
# a = a ^ b #a^b = 3
# b = a ^ b #a^b = 5 (^ = XOR)
# a = a ^ b #a^b = 6
a,b = b,a
print(a)
print(b)
