#question 1
# for i in range(1,11):
#     print(i)

#question 2
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print("\r")

#question 3
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


#question 4
# n = int(input())
# for i in range(1,11):
#     print(i*2)

#question 5
# list = [12,75,150,180,145,525,50]
# for i in list:
#    if i > 500:
#        break
#    elif i>150 :
#        continue
#    elif i%5 == 0:
#        print(i)

#question 6
# n = input()
# count=0
# for i in n:
#     count +=1
#
# print(count)

#question 7
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print("\r")

#question 8
# s = [10,20,30,40,50,60]
# for i in range(len(s),0,-1):
#     print(s[i-1])

#question 9
# for i in range(-10,0):
#     print(i)

#question 10
# for i in range(10):
#     print(i)
# print("Done!")


#question 11
# x = int(input())
# y = int(input())
# count = 0
# for i in range(x,y+1):
#     for j in range(1,i+1):
#       if i%j==0:
#           count  += 1
#     if count == 1 or count == 2:
#         print(i)
#         count = 0
#     else:
#         count = 0

#question 12
# n1 = 0
# n2 = 1
# n3 = 0
# n = int(input())
# if n==0:
#     print("Wrong Input")
# elif n==1:
#     print(n1)
# elif n == 2:
#     print(n1,n2)
# else:
#     for i in range(n):
#         print(n3)
#         n3 = n1+n2
#         n2 = n1
#         n1 = n3


#question 13
# fact = 1
# n = int(input())
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)

#question 14
# n = input()
# for i in range(len(n),0,-1):
#     print(i,end='')

# n = 12345
# x = n
# num = 0
# while x >0:
#     rem = x%10
#     num = num*10 +rem
#     x = x//10
#
# print(num)

#question 15
# l = [10,20,30,40,50,60,70,80,90,100]
# for i in range(len(l)):
#     if i%2 != 0:
#         print(l[i])


#question 16
# n = int(input())
# for i in range(1,n+1):
#     print(i*i*i)

#question 17
# n = int(input())
# x = 2
# sum = 0
# for i in range(n):
#     sum = sum+x
#
#     x = x*10 + 2
#
# print(sum)

#question 18
# for i in range(5):
#     for j in range(i+1):
#         print("*",end='')
#     print("\r")
# for i in range(5,0,-1):
#     for j in range(0,i-1):
#         print("*",end="")
#     print("\r")

for i in range(0,5*2-1):
    if i < 5:
        for j in range(5-i,5+1):
            print("*",end='')
        print("\r")
    else:
        for j in range(i-5+2,5+1):
            print("*",end="")
        print("\r")
