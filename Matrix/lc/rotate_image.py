class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 
        if n == 1: return matrix
        store = deque([])
        start, end = 0, n - 1

        while 1:
            # start = 1, end = 2
            for i in range(start, end):
                store.appendleft(matrix[start][i])
                store.appendleft(matrix[i][end])
                matrix[i][end] = store.pop()
                store.appendleft(matrix[end][end - (i - start)])
                matrix[end][end - (i - start)] = store.pop()
                store.appendleft(matrix[end - (i - start)][start])
                matrix[end - (i - start)][start] = store.pop()
                matrix[start][i] = store.pop()
            
            start += 1
            end -= 1
            if start >= end: break