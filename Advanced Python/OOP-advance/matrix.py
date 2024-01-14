from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
        assert type(matrix) == list, "Matrix should be a 2D list"
        for row in matrix:
            assert type(row) == list, "Matrix should be a 2D list"

        self.data = matrix
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])
    
    # Matrix + Matrix
    # Matrix + scalar
    def __add__(self, other):
        result = deepcopy(self)
        result += other
        return result

    def __iadd__(self, other):
        result = self
        if type(other) == Matrix:
            assert self.num_rows == other.num_rows, "For Matrix Addition Dimension of two matrix should be equal."
            assert self.num_cols == other.num_cols, "For Matrix Addition Dimension of two matrix should be equal."

            for row_idx in range(self.num_rows):
                for col_idx in range(self.num_cols):
                    result[row_idx][col_idx] += other[row_idx][col_idx]
            return result  
        else:
            for row_idx in range(self.num_rows):
                for col_idx in range(self.num_cols):
                    result[row_idx][col_idx] += other
            return result  
    
    # scalar + matrix
    def __radd__(self, other):
        return self + other

    # Matrix - Matrix
    # Matrix - scalar
    def __sub__(self, other):
        result = deepcopy(self)

        if type(other) == Matrix:
            assert self.num_rows == other.num_rows, "For Matrix Subtraction Dimension of two matrix should be equal."
            assert self.num_cols == other.num_cols, "For Matrix Subtraction Dimension of two matrix should be equal."

            for row_idx in range(self.num_rows):
                for col_idx in range(self.num_cols):
                    result[row_idx][col_idx] -= other[row_idx][col_idx]
            return result  
        else:
            for row_idx in range(self.num_rows):
                for col_idx in range(self.num_cols):
                    result[row_idx][col_idx] -= other
            return result  
    
    # scalar + matrix
    def __rsub__(self, other):
        return -(self - other)
    
    def __neg__(self):
        result = deepcopy(self)
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                result[row_idx][col_idx] = -result[row_idx][col_idx]
        return result 
    
    # Matrix * Matrix
    # Matrix * scalar
    def __mul__(self, other):
        result = deepcopy(self)

        if type(other) == Matrix:
            assert self.num_cols == other.num_rows, "For Matrix Multiplication number cols of first matrix should be equal to number of rows of the second matrix."

            for row_idx in range(self.num_rows):
                for col_idx in range(other.num_cols):
                    sum = 0
                    for idx in range(self.num_cols):
                        sum += self[row_idx][idx] * other[idx][col_idx]
                    result[row_idx][col_idx] = sum
            return result
        else:
            for row_idx in range(self.num_rows):
                for col_idx in range(self.num_cols):
                    result[row_idx][col_idx] *= other
            return result  
    
    # scalar * matrix
    def __rmul__(self, other):
        return self * other

    # Matrix / scalar
    def __truediv__(self, other):
        assert type(other) != Matrix, "Matrix/Matrix is not possible"

        result = deepcopy(self)
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                result[row_idx][col_idx] /= other
        return result  

    # Matrix // scalar
    def __floordiv__(self, other):
        assert type(other) != Matrix, "Matrix/Matrix is not possible"

        result = deepcopy(self)
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                result[row_idx][col_idx] //= other
        return result  
    
    def __getitem__(self, index):
        assert type(index) == int, "Index should be an integer"

        return self.data[index]

    def __str__(self):
        matrix_string = ''
        for row in self.data:
            for cell in row:
                matrix_string += str(cell) + " "
            matrix_string += "\n"
        return matrix_string

m1 = Matrix(
    matrix=[
        [1, 2, 3],
        [5, 7, 1],
        [1, 5, 9]
    ]
)
#  3 x 3
m2 = Matrix(
    matrix=[
        [5, 2, 5],
        [1, 3, 2],
    ]
)
#  2 x 3 
print(m1[0][0])
print(m1 * m2)
