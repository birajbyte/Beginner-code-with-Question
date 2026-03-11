#1-Write a program to cout how many even or odd numbers are present in list
# arr=[2,5,7,8,10,13]
# count_even=0
# count_odd=0
# for i in arr:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(f"Required even count is {count_even}")
# print(f"Required odd count is  {count_odd}")
      
# 2#modified
# arr=[2,5,7,8,10,13]
# even_num=[]
# odd_num=[]
# for num in arr:
#     if num%2==0:
#         even_num.append(num)
#     else:
#         odd_num.append(num)
        
# print(f"Even numbers: {even_num}")
# print(f"Odd numbers: {odd_num}")

#3Write a program to find the largest number in a list without using max().
# arr=[1,23,3,45,67,3,4]
# max_num=-1111
# for num in arr:
#     if max_num<num:
#         max_num=num
# print(f"The largest number is {max_num}")

#4find the largest and the second largesgt form list or array
# arr=[12,45,7,23,56,89,34]

#Write a program to print numbers from 1 to 50 but skip numbers divisible by 5.
for num in range(1,51):
    if num%5==0:
        continue
    print(num)





