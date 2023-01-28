# addNum is O(log n) because that's the time for insertion into a priority queue
#   a different queue implementation would make that faster, I believe
# getIntervals is O(n log n) because it's doing an O(log n) removal for each item in the queue
#   I don't think a better queue implementation could help here, because they all have O(log n) min pop
# could be faster with sortedcollections.SortedList, which is available in leetcode
import heapq

class SummaryRanges:
    def __init__(self):
        self.heap = []

    def addNum(self, value: int) -> None:
        heapq.heappush(self.heap, value)

    def getIntervals(self) -> List[List[int]]:
        if not self.heap:
            return []
        dup = [*self.heap]
        result = [[heapq.heappop(dup)] * 2]
        while dup:
            interval = result[-1]
            value = heapq.heappop(dup)
            if value - interval[1] > 1:
                result.append([value] * 2)
            else:
                interval[1] = value
        return result

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
