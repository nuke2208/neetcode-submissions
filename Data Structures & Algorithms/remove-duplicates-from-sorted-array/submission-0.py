class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        arr = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                arr.append(nums[i])
        nums[:] = arr
        return len(arr)       
            
