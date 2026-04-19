class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                result.append(prev)
                prev = intervals[i]
 
        result.append(prev)
        return result