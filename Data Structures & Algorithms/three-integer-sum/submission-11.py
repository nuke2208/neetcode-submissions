class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        n = len(nums)
        for i in range(n):
            seen = {}
            for j in range(i+1,n):
                needed = -(nums[i] + nums[j])
                if needed in seen:
                    triplets = sorted([nums[i], nums[j], needed])
                    answer.add(tuple(triplets))
                seen[nums[j]] = j
        return[list(triplets) for triplets in answer]
                     
        