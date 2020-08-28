#2 Accept a number and print the count of digit without using for loop
value=(input("Enter a number="))
print("The Count of",value,"is",len(value))

print("The count of",value ,end=" ")
count=0
while value != 0:
    value //= 10
    count+= 1
print("is",count)