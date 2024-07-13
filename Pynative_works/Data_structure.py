#question 1

#Method 1
l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]
l3 = []
#
# for i in range(len(l1)):
#     if i%2 != 0:
#         l3.append(l1[i])
#
# for i in range(len(l2)):
#     if i%2 == 0:
#         l3.append(l2[i])
#
# print(l3)

#Method 2

# odd = l1[1::2]
# even = l2[0::2]
#
#
# l3.extend(odd)
# l3.extend(even)
# print(l3)


#question 2

# l1 = [34,54,44,27,79,91,41]
#
# x = l1.pop(4)
#
# l1.insert(2,x)
# l1.append(x)
#
# print(l1)


#question 3

# sample = [11,45,8,23,14,12,78,45,89]
#
# x = len(sample)
#
# y = int(x/3)
# start = 0
# end = y
# for i in range(3):
#     index = slice(start,end)
#
#     list_ = sample[index]
#     print(list_)
#
#     print(list(reversed(list_)))
#     start = end
#     end += y

# Question 4:

# list_ = [11,45,8,11,23,45,23,45,89]
#
# count_dict = {}
#
# for i in list_:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
#
# print(count_dict)


#question 5

# list1 = [2,3,4,5,6,7,8]
# list2 = [9,49,36,25,4,16,64]
# x = set()
#
# for i in list1:
#     for j in list2:
#         if i*i == j:
#             x.add((i,j))
#
# print(x)
#
#Method 2
# res = zip(list1,list2)
#
# result = set(res)
# print(result)


#question 6

# first = {23,42,65,57,78,83,29}
# second = {57,83,29,67,73,43,48}
#
# res = first.intersection(second)
#
# print("Intersection is: ",res)
#
# for i in res:
#     first.remove(i)
#
# print(first)


#question 7

# list1 = {27,43,34}
# list2 = {34,93,22,27,43,53,48}
#
# if list1.issubset(list2):
#     print("True")
# else:
#     print("False")
#
# if list2.issuperset(list1):
#     print("True")
# else:
#     print("False")
#
# if list1.issubset(list2):
#     list1.clear()
#
# # print(list1)
# print(list2)


#question 8

# roll_number = [47,64,69,37,76,83,97,11, 95, 225]
# sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#
# print("List:", roll_number)
# print("Dictionary:", sample_dict)
#
# print(sample_dict.values())
#
# x =[]
#
# for i in roll_number[:]:  #While itearating the list , we need to use the copy of it
#     if i not in sample_dict.values():
#         print(i)
#         x.append(i)
#         roll_number.remove(i)
# # create new list
# # roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
# print("after removing unwanted elements from list:", roll_number)
# print("after removing unwanted elements from list:", x)



#question 9
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#
# x = []
# for i in speed.values():
#     if i not in x:
#         x.append(i)
#
# print(x)


#question 10

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#
# sample_list = list(set(sample_list))
# print(sample_list)
#
# sample_list = tuple(sample_list)
# print(sample_list)
#
# sample_list = sorted(sample_list)
# # print(sorted(sample_list))
#
# print("Min: ",sample_list[0])
#
# print("Max: ",sample_list[-1])