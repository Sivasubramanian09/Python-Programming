str = input().split(" ")
sub_str = input()
count = 0
for i in str:
    if i == sub_str:
        count = count+1

print(f"{sub_str} appeared {count} times")