# I really couldn't figure this one out. Probably would have helped if I'd done #300, Longest Increasing Subsequence first.
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        answer = [1 for _ in obstacles]
        best = []

        for i, height in enumerate(obstacles):
            index = bisect.bisect_right(best, height)

            if index == len(best):
                best.append(height)
            else:
                best[index] = height
            answer[i] = index + 1
        
        return answer
