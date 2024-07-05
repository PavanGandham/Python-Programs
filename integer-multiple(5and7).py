# Python Program to check whether the given integer is multiple of 5 and 7 

number = int(input("Enter the integer: "))
if((number%5==0 and number%7==0)):
    print("The nunber is multiple of both 5 and 7")
else:
    print("The number is not a multiple of both 5 and 7")
