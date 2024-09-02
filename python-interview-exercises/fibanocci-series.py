'''
What is Fibonacci Series
It's a unique sequence where the next number is the sum of previous two numbers.

Where the first two terms are always 0 and 1
In mathematical terms :
Fn = Fn-1 + Fn-2

Where,
F0 : 0
F1 : 1
Example Series
The series Looks like : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 …
'''
# Find the Fibonacci Series up to Nth Term Using Python

#1. Using Simple loops either for or while
    #a.Using For loop

def fibanocci_series_using_while_loop(num):
    num1 = 0
    num2 = 1
    count = 2
    print(f'Fibanocci Series for given number {num} is : {num1} {num2}', end=" ")
    while count < num:
        count += 1
        next_num = num1 + num2
        num1, num2 = num2, next_num
        print(next_num, end=" ")

fibanocci_series_using_while_loop(20)

    #b.Using While loop
def fibanocci_series_using_while_loop(num):
    num1 = 0
    num2 = 1
    next_num = num2
    count = 1
    while count <= num:
        count += 1
        print(next_num, end=" ")
        num1, num2 = num2, next_num
        next_num = num1 + num2

fibanocci_series_using_while_loop(20)

#-------------------------------------------------------------------------------------

# 2. Using Recurvsive Functions

