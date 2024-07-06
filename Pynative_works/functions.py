
#question 1
# def func(name,age):
#     print(f'Name:{name}\nAge:{age}')
#
# func("Siva",22)


#question 2
# def func(*args):
#     print("Printing values:")
#     # print(*args)
#     for i in args:
#         print(i)
#
# func(20,40,60)
#
# func(80,100)


#question 3
# def calculation(a,b):
#     add = a+b
#     sub = a-b
#
#     return add,sub
#
# x,y = calculation(40,10)
# print(x,y)


#question 4
# def show_employee(name,salary=9000):
#     print(f'Name: {name} Salary: {salary}')
#
# show_employee("Ben",12000)
# show_employee("Jessa")

#question 5
# def func(a,b):
#
#     def func1(a,b):
#         add = a+b
#         return add
#
#     sum = func1(a,b)+5
#
#     return sum
#
# x = func(5,6)
# print(x)


#question 6
# def recursive(n):
#     if n<=1:
#         return n
#     else:
#         return n + recursive(n-1)
#
# n = int(input())
#
# x = recursive(n)
#
# print(x)


#question 7
# def display_student(name,age):
#     print(name,age)
#
# show_student = display_student
#
# show_student("Siva",22)

#question 8
# def generate_list():
#     l = []
#     for i in range(4,30):
#         if i%2 == 0:
#             l.append(i)
#
#     print(l)
#
# generate_list()

# print(list(range(4,30,2)))

#question 9
# x = [4,6,8,24,12,2]
#
# x.sort()
# print(x[-1])

#question 10

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
print(Fibonacci(4))