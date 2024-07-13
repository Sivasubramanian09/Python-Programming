#question 1:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10,20,30]
#
#
# res = dict(zip(keys,values))
#
# print(res)

#question 2:

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# dict3 = dict()
# # dict3 = dict1.copy()
# dict3.update(dict1)
# dict3.update(dict2)
# print(dict3)


#question 3:

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict['class']['student']['marks']['history'])


#question 4:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# res = dict.fromkeys(employees, defaults)
# print(res)
#
# # Individual data
# print(res["Kelly"])


#question 5:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# keys = ['name', 'salary']
#
# x = dict()
# for i in keys:
#     x.update({i : sample_dict[i]})
#
# print(x)


#question 6:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # Keys to remove
# keys = ["name", "salary"]
#
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)

#question 7:
#
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
#
# x = int(input())
#
# for i in sample_dict.values():
#     print(i)
#     if i == x:
#         print(f"{i} present in a dict")

#question 8:

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sample_dict.pop('city')
#
# sample_dict.update({'location': "New york"})
#
# print(sample_dict)


#question 9:
# sample_dict = {
#   'Physics ': 82,
#   'Maths' : 65,
#   'history' : 75
# }
#
# x = []
#
# for i in sample_dict.values():
#   # print(i)
#   x.append(i)
#   # print(x)
#
# x.sort()
# print(x)
#
# for i,j in sample_dict.items():
#   if j == x[0]:
#     print(i)


#question 10:

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)