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
# .insert() function inserts the specified value at the specified position.
list1.insert(0, 0)
print(list1)

#.remove() function removes the first occurrence of the element with the specified value.
list1.remove(0)
print(list1)

#.reverse() function reverses the order of the elements in the list.
list1.reverse()
print(list1)

#.sort() function sorts the list in ascending order
list1.sort()
print(list1)

#.sort(reverse=True) function sorts the list in descending order
list1.sort(reverse=True)  
print(list1 )

#.count() function returns the number of elements with the specified value.
print(list1.count(1))

#.index() function returns the index of the first element with the specified value.
print(list1.index(1))
#.copy() function returns a copy of the list

