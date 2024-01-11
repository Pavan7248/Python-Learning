list1 = [1, 2, 3, 4, 5 ]
list2 = [6, 7, 8, 9, 10]
#.append() adds the element to the end of the list
list1.append(list2)
print(list1)
#Removing extra square brackets from the list i.e. [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
# .pop()function removes the last element from the list 

nested_list = list1.pop()
list1.extend(nested_list)
print(list1)

# .extend() function adds the elements of a list (or any iterable), to the end of the current list.
list1.extend(list2)
print(list1)
