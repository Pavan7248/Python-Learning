#creating a list through user input
#creating empty list
list1 = []

#asking user to enter number of elements 
num = int(input("Enter the number of elements in the list: "))

#iterating till the range
for i in range(num):
  numbers = int(input("Enter the number: "))
  list1.append(numbers)

#printing the list
print('The list is:', list1 )
