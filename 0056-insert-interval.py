class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        result = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s <= end:
                end = max(e, end)
            else:
                result.append([start, end])
                start, end = s, e
        result.append([start, end])
        return result
