
# Max Gain

'''
Given an list of integers, write a method max_gain that returns the maximum gain. Maximum Gain is defined as
the maximum difference between 2 elements in a list such that the larger element appears after the smaller element.
If no gain is possible return 0
'''

input_list = [1, 2, 5, 8, 16]

## My correct solution
def max_gain(input_list):

	diff = 0
	minimum = input_list[0]

	for val in input_list:
		if val < minimum:
			minimum = val
		if val - minimum > gain:
			gain = val - minimum
			
	if diff <= 0:
		return 0
	else:
		return gain


# Firecode solution
def max_gain(input_list):
	maximum = input_list[1] - input_list[0]
	minimum = input_list[0]
	i = 1
	while i < len(input_list):
		if (input_list[i] - minimum > maximum):
			maximum = input_list[i] - minimum
		if (input_list[i] < minimum):
			minimum = input_list[i]
		i = i + 1
	return 0 if maximum < 0 else maximum


# # More elegant solutions
def max_gain(input_list):
	min_val = input_list[0]
	diff = 0

	for val in input_list:
		if val < min_val:
			min_val = val
		else:
			diff = max(diff, val - min_val)

	return diff
