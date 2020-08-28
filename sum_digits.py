
#4 Accept an integer & print the sum of its digits

val = int(input("Enter a number="))
print("The sum of digits of", val, end=" ")
sum = 0
while val != 0:
    rem = val % 10
    sum += rem
    val = val//10

print("is", sum)