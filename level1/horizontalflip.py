
#Horizontal Flip

'''
You are given a m x n 2d image matrix where each integer represents a pixel. Flip it in-place along its horizonral axis.

input image:
11
00

output image:
00
11

'''

matrix =[[1,0,0], [0, 1, 0], [0, 0, 1]]

def flip_horizonral_axis(matrix):

	row = len(matrix) - 1
	col = len(matrix[0]) -1

	i = 0
	temp = 0
	while i <= row/2:
		j = 0
		while j <= col:
			temp = matrix[i][j]
			matrix[i][j] = matrix[row - i][j]
			matrix[row - i][j] = temp
			j = j + 1
		i = i + 1
	return matrix

print(matrix)
print(flip_horizonral_axis(matrix))






## My incorrect solution
def flip_horizontal_axis(matrix):
    
    m_length = len(matrix)
    pivot = (len(matrix)/2)
    
    for i in range(pivot):
        temp = m_length -i
        matrix[m_length -i] = matrix[i]
        matrix[i] = temp
