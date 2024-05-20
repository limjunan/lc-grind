class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = {}
        column = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in row: row[i] = 0
                    if j not in column: column[j] = 0

        for i in row:
            matrix[i] = [0 for _ in range(len(matrix[i]))]

        for i in column:
            for row in range(len(matrix)):
                matrix[row][i] = 0
        
        return matrix


        


        