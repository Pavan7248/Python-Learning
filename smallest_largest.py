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


#Finding max and min using for loop

l=eval(input("Enter a list of numbers"))

larg = l[0] 
small =l[0] 

for num in l:
    if num > larg:
        larg = num
    if num < small:
        smallest = num

print("Largest:", larg) 
print("Smallest:", small) 