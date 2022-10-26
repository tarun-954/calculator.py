a = int(input("enter the number:"))
x =input("Enter the operater:")
b =int(input("enter the second number:"))

# this is the simple calulator caluculations
# print("addition is ",a+b)
# print("substration is ",a-b)
# print("multiplication is ", a*b)
# print("modulus is :",a%b )
# print("division is :",a/b)

if x=="+":
    print("the output is :",a+b)
elif x=="-":
    print("the output is :",a-b)
elif x=="%":
    print("the output is :",a%b)
elif x=="*":
    print("the output is :",a*b)
elif x=="**":
    print("the output is :",a**b)
elif x=="//":
    print("the output is :",a//b)
elif x!="+,*,-,**,//":
    print("Error 202!! ")
else:
    print("Invalid input!!??? ")
