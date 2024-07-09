# Find the average of 10 numbers using while loop

count = 0
sum = 0.0
lst = []
while(count<10):
    number = float(input("Enter the real number: "))
    lst.append(number)
    count += 1
    sum += number
avg = sum/10
print(f"The Average of the following 10 numbers [{lst}] is : {avg}")
