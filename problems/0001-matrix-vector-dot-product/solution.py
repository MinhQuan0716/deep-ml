def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	RowA = len(a)
	ColA = len(a[0])
	RowB = len(b)
	if ColA != RowB:
		return -1
	result = [0 for _ in range(RowA)]
	for i in range(RowA):
			for k in range(ColA):
				result[i]+= a[i][k]*b[k]
	return result
	pass# If the number of columns in 'a' does not match the length of 'b', return -1.
	