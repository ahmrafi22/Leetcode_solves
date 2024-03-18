class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)    # Number of rows in the original matrix
        col = len(matrix[0]) # Number of columns in the original matrix
    
    # Initialize the transposed matrix with correct dimensions
        matrix2 = [[0] * row for _ in range(col)]
    
    # Transpose the matrix
        for i in range(row):
            for j in range(col):
                matrix2[j][i] = matrix[i][j]
    
        return matrix2
        