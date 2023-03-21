# Finding the given number is even or odd
number = input("Enter a Number: ")
x = int(number) % 2
if x == 0:
    print(f"The Given Number {number} is Even")
else:
    print(f"The Given Number {number} is Odd")