
n = 10

def dec_to_bin(n):
	if n < 2:
		return str(n)
	else:
		return dec_to_bin(n/2) + dec_to_bin(n%2)

print(dec_to_bin(n))