from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        self.m, self.n = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        # Compute the prefix sum matrix
        for i in range(self.m):
            for j in range(self.n):
                self.prefixSum[i + 1][j + 1] = (
                    matrix[i][j] 
                    + self.prefixSum[i][j + 1] 
                    + self.prefixSum[i + 1][j] 
                    - self.prefixSum[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1] 
            - self.prefixSum[row1][col2 + 1] 
            - self.prefixSum[row2 + 1][col1] 
            + self.prefixSum[row1][col1]
        )
