from matrix_errors import MatrixDefinitionError, MatrixOperationError

class Matrix:
	def __init__(self, content):
		# Check for emtpy matrix
		if not content:
			raise MatrixDefinitionError(details="A matrix cannot be empty.")
		
		# Check dimensions of the matrix
		cols = set([ len(row) for row in content ])
		if len(cols) != 1:
			matrix_dimension_error_deets = f"A matrix cannot have columns of varying lengths: {', '.join(map(str, cols))}"
			raise MatrixDefinitionError(details=matrix_dimension_error_deets)
		
		# Check for invalid matrix entries (non-int and non-float)
		invalid_entries = [ 
			(row_num, col_num, type(value).__name__, value)
				for row_num, row in enumerate(content)
					for col_num, value in enumerate(row)
						if not ( isinstance(value, float) or isinstance(value, int) )
		]
		if invalid_entries:
			invalid_entries_error_deets = '\n'.join( [ f"Element: { pos[3] } at position [{ pos[0] }][{ pos[1] }] is of type {pos[2]}" for pos in invalid_entries ] )
			raise MatrixDefinitionError(details=invalid_entries_error_deets)

		self.content = content

	def checkDimensionsMultiply(self, other):
		c1, r2 = len(self.content[0]), len(other.content)
		if c1 == r2:
			raise MatrixOperationError(details=f"Matrix 1 has {c1} columns and Matrix 2 has {r2} rows")
		
	def checkDimensionsAddSubtract(self, other):
		r1, c1, r2, c2 = len(self.content), len(self.content[0]), len(other.content), len(other.content[0])
		if c1 != c2 or r1 != r2:
			raise MatrixOperationError(details=f"Matrix 1 ({r1}x{c1}) columns is incompatible with matrix 2 ({r2}x{c2})")

	def add(self, matrix2, inplace=False):
		self.checkDimensionsAddSubtract(matrix2)
		
		pass

	def subtract(self, matrix2, inplace=False):
		self.checkDimensionsAddSubtract(matrix2)
		pass

	def leftMultiply(self, matrix2, side="r", inplace=False,):
		self.checkDimensionsMultiply(matrix2)

		pass

	def __str__(self):
		pass

myMatrix = Matrix( [[1, 2, 3], [3, 4, 5]] )
myMatrix2 = Matrix( [[4, 5, 6], [7, 8, 9]] )
print(myMatrix.dimensionsTest(myMatrix2))