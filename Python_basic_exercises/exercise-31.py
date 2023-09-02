# Python program to find the Nth term in a Fibonacci series using recursion
def Fib(n):
    if n<0:
        print("The input is incorrect.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(7))