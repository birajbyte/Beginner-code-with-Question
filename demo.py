
#print from 1 to 100 using for and while loop
i=1
while i<=100:
    print(i,end=" ")
    i+=1
print("the numbers using for loop")
for i in range(1,101):
    print(i,end=" ")


print("Hello world")
#Second question to print number with user input
num=int(input("Enter the number"))
print(f"The required number to print is {num}")
#the third question using if elif statements
marks= float(input("Enter the marks received"))

if marks<0:
    print(f"Invalid mark {marks}")
elif 32<=marks and marks<100:
    print("student passed the exam")
elif marks>100:
    print("Marks is greater than 100")
else:
    print("Students has failed the exam")


