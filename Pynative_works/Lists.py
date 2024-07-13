#question 1

# list1 = [100,200,300,400,500]
#
# list1.reverse()
#
# print(list1)


#question 2

# list1 = ["M","na","i","Ke"]
# list2 = ["y","me","s","lly"]
#Method 1
# y = ""
# z =[]
# x = len(list1)
#
# for i in range(x):
#     y = y + list1[i]
#     y = y + list2[i]
#     z.append(y)
#     y = ""
# print(z)


#Method 2
# list3 =[]
# for i,j in zip(list1,list2):
#     list3.append(i+j)
# print(list3)
#

#question 3
# list1 = [1,2,3,4,5,6,7]
# list2 = []
# for i in list1:
#     list2.append(i*i)
# print(list2)


#question 4
# import itertools
# x = []
# list1 = ["Hello", "take"]
# list2 = ["Dear", "Sir"]
#
# x = itertools.product(list1,list2)
#
# print(list(x))

#method2
# x = []
# for i in list1:
#     for j in list2:
#         x.append(i+" "+j)
#
# print(x)

#question 5

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# # list2[::-1]
#
# for i,j in zip(list1,list2):
#     print(i,j)


#question 6

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
# # list1 = set(list1)
# # list1.remove("")
# # print(list1)
# res = list(filter(None,list1))
# # for i in list1[:]:
# #     if i is None:
# #         list1.remove(i)
#
# print(res)

#question 7

# list1 = [10,20, [300,400, [5000,6000],500],30,40]
#
# print(len(list1))

# list1[2][2].append(7000)
# print(list1)
#
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         print(list[i][j])
#         # if list1[i][j] == 6000:
#         #     list1[i][j].append(7000)


#question 8

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# sub_list = ["h","i","j"]
#
# list1[2][1][2].extend(sub_list)
#
# print(list1)


#question 9

list1 = [5, 10, 15, 20, 25, 50, 20]

#Method 1
# for i in range(len(list1)):
#     # print(list1[i])
#     if list1[i] == 20:
#         list1[i] = 200
# print(list1)

#Method 2
# index = list1.index(20)
#
# list1[index] = 200
#
# print(list1)


#question 10
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1[:]:
    if i == 20:
        list1.remove(i)
print(list1)