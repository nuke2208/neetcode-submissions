class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        current_min = nums[0]
        current_max = nums[0]
        answer = nums[0]
        for i in range(1,n):
            x = nums[i]
            new_max = max(x,x*current_max,x*current_min)
            new_min = min(x,x*current_max,x*current_min)
            current_max = new_max
            current_min = new_min
            answer = max(current_max,answer)
        return answer
        