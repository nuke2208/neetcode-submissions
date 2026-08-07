class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        stack.append(0)
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                result[a] = i - a
            
            stack.append(i)
        
        return result

            


        