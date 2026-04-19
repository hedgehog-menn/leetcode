class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        result = []

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                result.append(prev)
                prev = interval
 
        result.append(prev)
        return result