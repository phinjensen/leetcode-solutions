# Pretty slow, bottom 5.5%

from queue import PriorityQueue
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = PriorityQueue()
        counts = Counter(tasks)
        # tuple format: (wait, total, task)
        # Pop one off, remove 1 from total, put it back on with wait + n
        for key, count in counts.items():
            queue.put((0, count, key))
        
        result = 0
        while not queue.empty():
            wait, remaining, task = queue.get()
            #print(result, wait, remaining, task)
            if wait > result:
                result = wait
            result += 1
            if remaining > 1:
                queue.put((wait + n + 1, remaining - 1, task))
        return result
