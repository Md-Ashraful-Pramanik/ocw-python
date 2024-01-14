from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
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
        result = deepcopy(self)
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                result[row_idx][col_idx] /= other
        return result  

    # Matrix // scalar
    def __floordiv__(self, other):
        result = deepcopy(self)
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                result[row_idx][col_idx] //= other
        return result  
    
    def __getitem__(self, index):
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

m2 = Matrix(
    matrix=[
        [5, 2, 5],
        [1, 3, 2],
        [4, 3, 4]
    ]
)

print(m1[0][0])
print(m1 * m2)
