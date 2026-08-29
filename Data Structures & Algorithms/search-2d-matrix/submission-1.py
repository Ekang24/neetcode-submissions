class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            row_mid = (top+bot) // 2
            if target < matrix[row_mid][0]:
                bot = row_mid - 1
            elif target > matrix[row_mid][-1]:
                top = row_mid + 1
            else:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target == matrix[row_mid][mid]:
                        return True
                    if target < matrix[row_mid][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
        return False