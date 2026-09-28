from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        res = 0
        # Make adjList
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()

        def bfs(node):
            q = deque([node])  # Use deque for O(1) pop from front
            visited.add(node)
            while q:
                curr = q.popleft()
                for nei in adjList[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        
        return res

        