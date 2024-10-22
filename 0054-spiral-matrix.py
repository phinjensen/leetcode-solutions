# THERE'S GOT TO BE A BETTER WAY!
NEXT_DIRECTION = {
    'r': 'd',
    'd': 'l',
    'l': 'u',
    'u': 'r',
}

def next_step(r, c, d):
    return {
        'r': (r, c+1),
        'd': (r+1, c),
        'l': (r, c-1),
        'u': (r-1, c),
    }[d]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.matrix = matrix
        visited = set()
        r, c = 0, 0
        result = []
        direction = 'r'
        while self.valid((r, c)) and (r, c) not in visited:
            result.append(matrix[r][c])
            visited.add((r,c))
            n = next_step(r, c, direction)
            if not (self.valid(n) and n not in visited):
                direction = NEXT_DIRECTION[direction]
                n = next_step(r, c, direction)
            r, c = n
        return result

    def valid(self, coords):
        r, c = coords
        if 0 <= r < len(self.matrix) and 0 <= c < len(self.matrix[0]):
            return True
        return False


