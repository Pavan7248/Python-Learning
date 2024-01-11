#finding the smallest and the largest element from the list.

#creating the empty list
list1 = []

#asking the user to enter the number of elements to the list
num = int(input("Enter the number of elements in the list: "))

#iterating till the range
for i in range(num):
  numbers = int(input("Enter the element: "))
  list1.append(numbers)

#printing the list
print("The list is: ", list1)
#printing the largest element
print("The largest element in the list is: ", max(list1))
#printing the smallest element
print("The smallest element in the list is: ", min(list1))
