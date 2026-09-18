class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxright = -1
        n  = len(arr)
        for i in range(n-1,-1,-1):
            current = arr[i]
            arr[i] = maxright
            maxright = max(maxright,current)
        return arr



        