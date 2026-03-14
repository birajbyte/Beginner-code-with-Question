#Celsius to frahnite degreee
def celsius_to_frahnite(x):
    frahnite=x*9/5+32
    return frahnite
number=int(input("Enter the celsius degree to convert"))
result=celsius_to_frahnite(number)
print(f"The required celsius is {result}")


#print multiplication table of n numbers
i=1
mult=int(input("Enter the numbers to find table"))
while i<=10:
    print(f"{mult} * {i} = {mult*i}")
    i+=1

    