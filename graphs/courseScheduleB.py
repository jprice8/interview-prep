import collections
from typing import List


# [[2,1], [3,2], [4,2]]

class Solution:
    def solutionDfs(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        # build adj list
        adj = { i: [] for i in range(numCourses) }
        for course, pre in prereqs:
            adj[course].append(pre)

        visited = set()

        def dfs(crs):
            # we've found a cycle
            if crs in visited:
                return False
            # if crs has no prereqs, pop off
            if len(adj[crs]) == 0:
                return True

            visited.add(crs)
            for neighbor in adj[crs]:
                if not dfs(neighbor): return False
            visited.remove(crs)
            adj[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



    def solutionBfs(self, numCourses, prereqs):
        adj = collections.defaultdict(list)


if __name__ == '__main__':
    s = Solution()
    print(s.solutionDfs(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))