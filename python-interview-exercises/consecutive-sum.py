# write a python program to find the sum of n cosecutive numbers in a series list and so on.

sum_list = []

def consecutive_sum(n,series_list):
    for i in range(0,len(series_list),n):
        group_sum = sum(series_list[i:i+n])
        sum_list.append(group_sum)
print(sum_list)

# Example lets take n=3 so we need to find the sum of 3 consecutive number in a series list and so, on

# series_list = [1,2,3,4,5,6,7,8,20]
# then sum_list = [6, 15, 35]