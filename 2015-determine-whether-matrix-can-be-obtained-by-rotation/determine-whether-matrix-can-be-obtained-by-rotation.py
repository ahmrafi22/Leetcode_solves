class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        for rotation in range(4):
            if mat == target:
                return True
            

            mat2 = [row[:] for row in mat]
            b = 0
            for i in range(n):
                a = n - 1
                for j in range(n):
                    mat[i][j] = mat2[a][b]
                    a -= 1
                b += 1
        
        return False