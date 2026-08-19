class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        count1 = [0]*26
        for s in s1:
            count1[ord(s) - ord('a')] += 1
        count2 = [0]*26
        for i in range(n):
            count2[ord(s2[i]) - ord('a')] += 1
        left = 0
        right = n-1
        for i in range(m-n+1):
            if count1 == count2:
                return True
            else:

                count2[ord(s2[left]) - ord('a')] -= 1
                left = left + 1
                right = right + 1
                if right < m:
                    count2[ord(s2[right]) - ord('a')] += 1
        return False
                

        
        

        
            
                
        