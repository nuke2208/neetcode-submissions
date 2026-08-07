class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        order = set(nums)
        longest = 0
        for num in order:
            if (num-1) not in order:
                current = 1
                next = num + 1
                while next in order:
                    current = current + 1
                    next = next + 1
                if current > longest:
                    longest = current
        return longest