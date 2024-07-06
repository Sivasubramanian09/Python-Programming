#Input and Output Section

#question 1
#x = int(input())
#y = int(input())
#
# mul = x*y
# print(mul)


#question 2
# print('Name','Is','James',sep='**')

#queston 3
# n = 8
# print('%o'% n)

#question 4
# n = 458.541315
# print('%.2f'%n)
# print('{:.2f}'.format(n))

#question 5
# list = []
# for i in range(5):
#     x = float(input())
#     list.append(x)
#
# print(list)

#question 6
# fp = open("test.txt","r")
# lines = fp.readlines()
#
# fp = open("new_file.txt","w")
# count =0
# for line in lines:
#     if count == 4:
#         count += 1
#         continue
#     else:
#         fp.write(line)
#     count += 1

#quesion 7
# name1,name2,name3 = input().split()
# print(f'Name1:{name1}\nName2:{name2}\nName3:{name3}')


#question 8
# total = 1000
# quantity = 3
# price = 450
#
# print(f'I have {total} dollars so I can Buy {quantity} football for {price} dollars')


#question 9

# import os
# fd = os.stat("test.txt").st_size
# if fd == 0:
#     print("Empty")
# else:
#     print("Not Empty")


#question 10
fd = open("test.txt","r")
lines = fd.readlines()
print(lines[1])





