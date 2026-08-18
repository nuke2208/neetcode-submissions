class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        for i in range(n):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
        result.append(newInterval)
        return result
            
        
        