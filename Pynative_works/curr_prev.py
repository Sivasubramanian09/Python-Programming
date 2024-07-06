n = int(input())
num = 0
for i in range(n):
    print(f"Current Number {i} Previous Number {num} Sum: {i+num}")
    num = i