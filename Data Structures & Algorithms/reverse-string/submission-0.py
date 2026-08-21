class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        arr = [0]*n
        for i in range(n):
            arr[i] = s[n-1-i]
        s[:] = arr
        
        