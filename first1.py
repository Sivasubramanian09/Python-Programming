a=[]
res=0
n= int(input())
print("Enter the Numbers")
for i in range(n):
     num = int(input("Number"+str(i+1)))
     a.append(num)
     res = res+num
print("The first 7 Natural number is:",a)
print("The sum of the natural number is:",res)

    
