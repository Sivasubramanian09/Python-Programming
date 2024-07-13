#question 1:

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
#
# x = set(sample_set)
# x.update(sample_list)
#
# print(x)

#question 2:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# x = set1.intersection(set2)
# # set1.update(set2)
# # print(set1)
# print(x)


#question3:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1.update(set2)
# print(set1)

#question 4:

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
#
# set2.difference_update(set1)
# set2 -= set1
# print(set2)


#question 5:

# set1 = {10,20,30,40,50}

# set1 -= {10,20,30}

# set1.difference_update({10,20,30})
# print(set1)


#question 6:

# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set()

# for i in set1:
#     if i not in set2:
#         set3.add(i)
# for i in set2:
#     if i not in set1:
#         set3.add(i)
# print(set3)

# x = set1.symmetric_difference(set2)
# print(x)

#question 7:

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
#
# if set1.isdisjoint(set2):
#     print("False")
# else:
#     print("True")
#     print(set1.intersection(set2))

#question 8

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# x = set1.symmetric_difference(set2)
# print(x)

#question 9

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))