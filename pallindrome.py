#check the given sunber as pallidrome or not
num=int(input("Enter the number to check   "))
reverse=0
num_2=num
while num>=1:   
    reminder= num%10         
    reverse= reverse*10+reminder
    num= num//10  
if reverse==num_2:
    print(f"The number given  {num_2} is pallindrome")
else:
    print(f"The number given {num_2} is not pallindrome")


