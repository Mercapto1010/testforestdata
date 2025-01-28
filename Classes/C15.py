print(f.read())
print(f.readline())
f = open('MyData', 'r')
print(f.readline(1), end= "")

f1 = open('yash', 'w')
f1 = open('yash', 'a' )
for data in f:
    f1.write(data)

f = open('Pic.jpg', 'rb')
f1 = open('Photu.jpg', 'wb')
for i in f:
    f1.write(i)