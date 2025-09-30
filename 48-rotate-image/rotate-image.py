class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        matrix2 = [row[:] for row in matrix]
        
        b = 0
        
        for i in range(n):
            a = n - 1
            for j in range(n):
                matrix[i][j] = matrix2[a][b]
                a -= 1
            b += 1