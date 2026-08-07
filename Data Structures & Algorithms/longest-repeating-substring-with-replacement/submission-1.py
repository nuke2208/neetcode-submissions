class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maxlength = 0
        maxfreq = 0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            if freq[s[right]] > maxfreq:
                maxfreq = freq[s[right]]
            while (right - left) + 1 - maxfreq > k:
                freq[s[left]] -= 1
                left = left + 1
            if right - left + 1 > maxlength:
                maxlength = right - left + 1
        return maxlength
                        