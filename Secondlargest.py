#find the second largest and largest
arr=[23,4,56,78,89,80]
largest=float("-inf")
second_largest=float("-inf")
second_largest=float("-inf")
for num in arr:
    if largest<num:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(f"largest number is {largest}")
print(f"Required second largest num is {second_largest}")



