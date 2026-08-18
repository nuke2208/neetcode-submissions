class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        start = intervals[0]
        count = 0
        for i in range(n-1):
            if intervals[i+1][0] >= start[1]:
                start = intervals[i+1]
            else:
                count = count + 1
                start[1] = min(intervals[i+1][1],start[1])

        return count
                

        