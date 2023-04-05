from operator import itemgetter

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        start = -1 
        end = 0
        i = 0
        result = 0
        candidate = None
        while end < time and i < len(clips):
            clip_start, clip_end = clips[i]
            if clip_start > end:
                if candidate:
                    result += 1
                    start, end = candidate
                    candidate = None
                else:
                    return -1
            if clip_start <= end:
                if clip_end > time:
                    candidate = clips[i]
                    break
                if clip_end > end:
                    candidate = clips[i]
            i += 1
        if end < time and candidate:
            result += 1
            start, end = candidate
        if end >= time:
            return result
        else:
            return -1
