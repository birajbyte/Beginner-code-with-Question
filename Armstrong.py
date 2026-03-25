#check the given sunber as armstrong or not
num=int(input("Enter the number to check   "))
arm=0
digits=len(str(num))
num_2=num
while num>=1:   
    rem= num%10         
    arm= arm + rem**digits
    num= num//10  
if arm==num_2:
    print(f"The number given  {num_2} is Armstrong")
else:
    print(f"The number given {num_2} is not Armstrong")


