class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      count = {}
      for ch in s:
        if ch in count:
            count[ch] = count[ch] + 1
        else:
            count[ch] = 1
      for ch in t:
        if ch in count:
            count[ch] = count[ch] - 1
        else:
            return False
      for value in count.values():
        if value != 0:
            return False
      return True