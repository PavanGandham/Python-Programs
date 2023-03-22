# Find the product of set of real numbers

i = 0
product = 1
count = int(input("Enter the no.of real numbers: "))
for i in range(count):
    x =  float(input("Enter the real number: "))
    product = product * x
print("The Product of numbers is : ", product)

