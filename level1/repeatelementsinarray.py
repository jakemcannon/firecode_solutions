
list_numbers = [1, 3, 4, 2, 1, 2, 4]
# list_numbers = [4]

def duplicate_items(list_numbers):
	list_numbers.sort()
	result = []

	for i in range(len(list_numbers)):
		if len(list_numbers) == 1:
			continue

		if list_numbers[i] == list_numbers[i-1]:
			result.append(list_numbers[i])
	return result


'''
Notice that the second function allows you to remove the first if statement. That is
because there is an edge case when your array only has one element in it. The additional step
is to make the range from 1 - length instead of 0 - length. This is because in our comparison
code we have [i-1] and so if there is only one element in the array we will just look at the items
in reverse and they will in fact be == but the function will say != . My fix was to add 
an extra if statement but another solution is to also start at index 1 instead of 0. Then 1-0 = 1.
In otherwords we actually do a calculation instead of indexing the array backward.
'''

# def duplicate_items(list_numbers):
# 	list_numbers.sort()
# 	result = []

# 	for i in range(1, len(list_numbers)):
# 		if list_numbers[i] == list_numbers[i-1]:
# 			result.append(list_numbers[i])
# 	return result