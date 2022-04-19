import collections
from typing import List


class Solution:
    def shortestPath(self, graph: List[List[int]], a: int, b: int) -> int:
        q = collections.deque([a])
        edgeCount = 0
        visited = set([a])
        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node == b:
                    return edgeCount
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue 
                    q.append(neighbor)
                    visited.add(neighbor)

            edgeCount += 1



if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }
    s = Solution()
    print(s.shortestPath(graph, 0, 3)) # 2