#Replace duplicate occurance in string

str = input("Enter the string: ")

print("Printing the original string: ", str)
test_list = str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in res:
      