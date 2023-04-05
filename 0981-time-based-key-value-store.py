from sortedcontainers import SortedList

# Slow, but technically still O(log n) for all operations, I think
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, SortedList(key=lambda e: e[1])).add((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        stuff = self.store.get(key, SortedList())
        l = stuff.bisect_left((key, timestamp))
        r = stuff.bisect_right((key, timestamp))
        if l != r:
            return stuff[l][0]
        elif l > 0:
            return stuff[r-1][0]
        else:
            return ""
