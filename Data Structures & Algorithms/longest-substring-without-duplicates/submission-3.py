class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        max_count = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            else:
                seen.add(s[right])
            count = right - left + 1
            if count > max_count:
                max_count = count
        return max_count        