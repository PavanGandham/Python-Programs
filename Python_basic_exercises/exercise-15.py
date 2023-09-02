#  Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")