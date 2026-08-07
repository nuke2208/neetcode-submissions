class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)*len(matrix[0]) - 1
        while left <= right:
            mid = int((left + right)/2)
            if target > matrix[int(mid/len(matrix[0]))][mid%len(matrix[0])]:
                left = mid + 1
            elif target < matrix[int(mid/len(matrix[0]))][mid%len(matrix[0])]:
                right = mid - 1
            else:
                return True
        return False
                
