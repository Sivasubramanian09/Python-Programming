n = []
x = int(input())
for i in range(x):
    a = int(input())
    n.append(a)

for i in n:
    if (i%5) == 0:
        print(i)
