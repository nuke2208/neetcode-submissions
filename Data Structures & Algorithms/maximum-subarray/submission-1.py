class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]
        current = nums[0]
        for i in range(1,n):
            current = max(nums[i],current + nums[i])
            maximum = max(current,maximum)
        return maximum

            
        