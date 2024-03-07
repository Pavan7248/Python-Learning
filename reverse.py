#Program to display the reverse of a given number.
num = int(input("Enter a number: "))

rev = 0
while num > 0:
  rem = num % 10
  rev = rev * 10 + rem
  num = num // 10

print("The reverse of the number is: ", rev)


num = int(input("Enter a number:  "))

rev = 0
while num > 0:
  rem = num % 10
  rev = rev *10 + rem 
  num = num // 10

print("The reverse of the number is: ", rev")

       rev = 0
      while num > 0:
  rem = num % 10
  rev = rev * 10 +rem
  num = num // 1
  