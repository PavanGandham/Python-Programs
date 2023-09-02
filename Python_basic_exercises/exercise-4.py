# Finding the average of set of integers

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter the integer: "))
    sum = sum + x
avg = sum / count
print("The Average is : ", avg)
