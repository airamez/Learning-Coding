from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        # Matrix for memoization
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = list()
        # Filling memo with zeros
        for i in range(ROWS):
            memo.append(list())
            for j in range(COLS):
                memo[i].append(0)
                if matrix[i][j] == '1':
                    max_len = 1
        # Initializing the last row
        for j in range(COLS):
            memo[ROWS - 1][j] = int(matrix[ROWS - 1][j])
        # Initializing the last column
        for i in range(ROWS):
            memo[i][COLS - 1] = int(matrix[i][COLS - 1])
        # Starting from the bottow left, moving up and left building the memorization
        current_i = ROWS - 2
        current_j = COLS - 2
        while current_i >= 0 and current_j >= 0:
            # Updating row
            for j in range(current_j, -1, -1):
                if matrix[current_i][j] == '1':
                    right = memo[current_i][j + 1]
                    down = memo[current_i + 1][j]
                    diag = memo[current_i + 1][j + 1]
                    memo[current_i][j] = 1 + min(right, min(down, diag))
                    max_len = max(max_len, memo[current_i][j])
            # Updating Col
            for i in range(current_i, -1, -1):
                if matrix[i][current_j] == '1':
                    right = memo[i][current_j + 1]
                    down = memo[i + 1][current_j]
                    diag = memo[i + 1][current_j + 1]
                    memo[i][current_j] = 1 + min(right, min(down, diag))
                    max_len = max(max_len, memo[i][current_j])
            current_i -= 1
            current_j -= 1
                    
        # check if i or j ends first
        return max_len ** 2
        

app = Solution()
print(app.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))