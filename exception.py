"""num1= int(input("Enter the Number 1:"))
num2= int(input("Enter the Number 2:"))

try:
    z= num1/num2
except ZeroDivisionError as e:
    print("Exception Occured:",e)
    z= None
print("Division is: ",z)"""

a= input("Enter the input:")
b= input("Enter the input:")

try:
      z=x/(int)
      
except ZeroDivisionError as e:
    print("Division on Zero Error")
    z=None
except TypeError as e:
    print("Type Error Exception")
    z= None
print("Division is: ",z)
    