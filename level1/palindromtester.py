#My solution
def is_palindrome(input_string):

	stack = []
	if len(input_string) == 0:
		return True

	for i in range(len(input_string)):
		stack.append(input_string[i])

	for i in range(len(input_string)):
		if stack.pop() != input_string[i]:
			return False
		else:
			return True

#Discussion Solution
def is_palindrome(input_string):
	return input_string == input_string[::-1] #iterate over string backwards

#Firecode Solution
def is_palindrome(input_string):
	result = True
	str_len = len(input_string)
	for i in range(0, int(str_len/2)):
		if input_string[i] != input_string[str_len-i-1]
		result = False
		break
	return False
