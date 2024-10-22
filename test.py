def lengthOfLongestSubstring(s: str) -> int:
    last_occurrence = {}
    longest = 0
    last_unique = 0
    current = 0
    for i, c in enumerate(s):
        if c not in last_occurrence:
            current += 1
        else:
            longest = max(longest, current)
            current = i - last_occurrence[c]
        last_occurrence[c] = i
    longest = max(longest, len(s) - last_unique)
    return longest
