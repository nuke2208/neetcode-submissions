class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        ans = set()
        for i in range(n):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] - 1
            else:
                count[nums[i]] = int(n/3) - 1
        for i in range(n):
            if count[nums[i]] < 0:
                ans.add(nums[i])
        return list(ans)
    
        
            

        
        