# Python equivalent of above code 

# define a function to set the zeroes in the matrix
def setZeroes(matrix):
	# get the length of the matrix
	rows = len(matrix)
	cols = len(matrix[0])

	# Iterate through each element of the matrix
	for i in range(0, rows):
		for j in range(0, cols):

			# If the element is 1, mark its
			# corresponding row and column using -1
			if matrix[i][j] == 1:

				# Mark all elements in the same column
				# as -1, except for other 1's
				ind = i - 1
				while ind >= 0:
					if matrix[ind][j] != 1:
						matrix[ind][j] = -1
					ind -= 1

				ind = i + 1
				while ind < rows:
					if matrix[ind][j] != 1:
						matrix[ind][j] = -1
					ind += 1

				# Mark all elements in the same row as
				# -1, except for other 1's
				ind = j - 1
				while ind >= 0:
					if matrix[i][ind] != 1:
						matrix[i][ind] = -1
					ind -= 1

				ind = j + 1
				while ind < cols:
					if matrix[i][ind] != 1:
						matrix[i][ind] = -1
					ind += 1

	# Iterate through the matrix again, setting all
	# -1's to 0
	for i in range(0, rows):
		for j in range(0, cols):
			if matrix[i][j] < 0:
				matrix[i][j] = 1

# Test the setZeroes function with a sample input
if __name__ == "__main__":
	arr = [[1, 0, 2, 1],
		[3, 4, 5, 2],
		[0, 3, 0, 5]]
	setZeroes(arr)
	print("The Final Matrix is:")
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print(arr[i][j], end=" ")
		print()
