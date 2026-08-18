class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        result = []
        start = intervals[0]
        for i in range(n-1):
            if intervals[i+1][0] > start[1]:
                result.append(start)
                start = intervals[i+1]
            elif intervals[i+1][1]<start[0]:
                result.append(intervals[i+1])
            else:
                start[0] = min(start[0],intervals[i+1][0])
                start[1] = max(start[1],intervals[i+1][1])
        result.append(start)
        return result


        