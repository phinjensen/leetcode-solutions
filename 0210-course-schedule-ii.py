# Faster: Keep track of the nodes with an indegree of 0:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adjacency = {}
        for course, prereq in prerequisites:
            indegree[course] += 1
            adjacency.setdefault(prereq, []).append(course)

        nodes_with_0_indegree = [i for i in range(numCourses) if indegree[i] == 0]
        sort = []

        while len(nodes_with_0_indegree) > 0:
            node = nodes_with_0_indegree.pop()
            sort.append(node)
            for course in adjacency.get(node, []):
                indegree[course] -= 1
                if indegree[course] == 0:
                    nodes_with_0_indegree.append(course)
        
        if len(sort) < numCourses:
            return []
        else:
            return sort

# Slower: Just keep iterating over all nodes.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adjacency = {}
        for course, prereq in prerequisites:
            indegree[course] += 1
            adjacency.setdefault(prereq, []).append(course)
        
        sort = []
        while len(sort) < numCourses:
            found = False
            for node in range(numCourses):
                if indegree[node] == 0:
                    indegree[node] = -1
                    found = True
                    sort.append(node)
                    for course in adjacency.get(node, []):
                        indegree[course] -= 1
            if not found:
                return []
        return sort
