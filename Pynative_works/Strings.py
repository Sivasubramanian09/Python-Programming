#question 1
# str1 = "Sivasubramanian"
import string

# if len(str1) %2 == 0:
#     mid = len(str1)/2
#     print(int(mid))
# else:
#     mid = (len(str1)/2)+1
#     print(int(mid))
#
# first = str1[0]
# last = str1[-1]
# mid_ = str1[int(mid)-1]
# print(mid_)
#
# print(first+mid_+last)

#question 2
# str =  "JaSonAy"
#
# mid = int(len(str)/2)
# _mid = mid-1
# mid_ = mid+1
#
# print(str[_mid]+str[mid]+str[mid_])

#question 3
# str1 = "Ault"
# str2 = "kelly"
#
# mid = int(len(str1)/2)
#
# print(str1[:mid]+str2+str1[mid:])


#question 4
# str1 = "America"
# str2 = "Japan"
#
# mid1 = int(len(str1)/2)
# mid2 = int(len(str2)/2)
#
# print(str1[0]+str2[0]+str1[mid1]+str2[mid2]+str1[-1]+str2[-1])
#


#quesztion 5
# str1 = "PyNaTive"

#method-1
# for i in str1:
#     if i.islower():
#         print(i,end="")
#
# for i in str1:
#     if i.isupper():
#         print(i,end='')

#method-2
# l =[]
# u=[]
# for i in str1:
#     if i.islower():
#         l.append(i)
#     else:
#         u.append(i)
#
# # str2 = ''.join(l+u)
# print(''.join(l+u))


#question 5

# str1 = "P@#yn26at^&i5ve"
#
# count =0
# digit =0
# symbol=0
# for i in str1:
#     if i.isalpha():
#         count += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         symbol += 1
#
# print(count,digit,symbol)


#question 6
# s1 = "Abcde"
# s2 = "Xyz"
#
# # get string length
# s1_length = len(s1)
# s2_length = len(s2)
# print(s1_length,s2_length)
#
# # get length of a bigger string
# length = s1_length if s1_length > s2_length else s2_length
# result = ""
#
# print(length)
#
# # reverse s2
# s2 = s2[::-1]
#
# # iterate string
# # s1 ascending and s2 descending
# for i in range(length):
#     if i < s1_length:
#         print(i)
#         result = result + s1[i]
#         print(result)
#     if i < s2_length:
#         result = result + s2[i]
#         print(i)
#         print(result)
#
# print(result)

# str1 = "Abcdcd"
# str2 = "Xyz"
# str2 = str2[::-1]
# #
# for i in range(len(str1)):
#         if i < len(str1):
#             print(str1[i],end='')
#         if i <len(str2):
#             print(str2[i],end='')


#question 7

# s1 = "Ynf"
# s2 = "PYnative"
#
# flag = True
#
# for i in s1:
#     if i in s2:
#         continue
#     else:
#         flag = False
#
# print(flag)

#question 8
# str1 = "Welcome to USA. usa awesome , isn't it?"
# sub = "IT"
#
# temp = str1.lower()
# print(temp)
#
# count = temp.count(sub.lower())
# print(count)

#question 9
# str1 = "PYnative29@#8496"
# sum =0
# count =0
# for i in str1:
#     if i.isdigit():
#         sum += int(i)
#         count += 1
# avg = sum/count
# print(avg)

#question 10

# str1 = "Apple"
#
# char_dict = dict()
#
# for i in str1:
#     count = str1.count(i)
#
#     char_dict[i] = count
#
# print(char_dict)

#question 11

# str1 = "Pynative"
#
# str1 = str1[::-1]
#
# print(str1)


#question 12

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
#
# sub = input()
#
# res = str1.rfind(sub)
# print(res)


#question 13

# str1 = "Emma-is-a-data-scientist"
#
# str2 = str1.split("-")
#
# for i in str2:
#     print(i)


#question 14
#
# str_list = ["Emma", "John", "", "Kelly", None, "Eric",""]
# str1 = []
# for i in str_list:
#     if i:
#         str1.append(i)
#
# print(str1)

#question 15

# str1 = "/*Jon is @developer & musician"
# str2 = ""
# for i in str1:
#     if i.isalnum():
#         str2 += i
#     if i == ' ':
#         str2 += ' '
# str2 = str2.replace("  "," ")
#
# print(str2)

# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(mytable)
# print(txt.translate(mytable))

# import string
#
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
# x = str1.maketrans('', '',  string.punctuation)
# print(x)
# new_str = str1.translate(x)
#
# print("New string is ", new_str)

# import re
#
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
# x = re
# print(x)
# # replace special symbols with ''
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)


#question 16

# str1 = 'I am 25 years and 10 months old'
#
# for i in str1:
#     if i.isdigit():
#         print(i,end='')

#question 17

# str1 = "Emma25 is Data scientist50 and AI Expert"
#
# str2 = str1.split(" ")
# res = []
# for i in str2:
#     if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
#         print(i)


#question 18
str1 = "/*Jon is @developer & musician!!"
for i in str1:
    if i.isalnum() is False:
        if i != " ":
            str1 = str1.replace(i,"#")
print(str1)