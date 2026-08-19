class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        n = len(piles)
        answer = right
        while left <= right:
            mid = int((left+right)/2)
            hours = 0
            for i in range(n):
                if piles[i]%mid == 0:
                    hours = hours + piles[i]/mid
                else:
                    hours = hours + int(piles[i]/mid) + 1
            if hours > h:
                left = mid + 1
            else:
                answer = mid
                right = mid -1 
        return answer

                
        






        


        