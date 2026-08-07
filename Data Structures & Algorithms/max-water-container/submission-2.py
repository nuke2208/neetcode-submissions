class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights) - 1
        right = n
        max_area = 0
        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            current_area = width*height
            if current_area > max_area :
                max_area = current_area
            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return max_area
        