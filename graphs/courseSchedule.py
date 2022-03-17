import collections
from typing import Dict, List


class Solution:
    def courseScheduleBfs(self, numCourses: int, prerequisites: List[int]) -> bool:
        pass

    def courseScheduleDfs(self, numCourses, prerequisites):
        preMap = { i: [] for i in range(numCourses) }
        for target, needed in prerequisites:
            preMap[target].append(needed)

        visit = set()

        def dfs(node):
            if node in visit:
                return False 

            if preMap[node] == []:
                return True 

            visit.add(node)

            for prereq in preMap[node]:
                if not dfs(prereq): return True

            visit.remove(node)
            preMap[node] = []
            return True

        for node in range(numCourses):
            if not dfs(node): return False 
        return True


    def courseScheduleTopo(self, numCourses, prerequisites):
        adj = [set() for i in range(numCourses)]
        
        indegree = {i:0 for i in range(numCourses)}
        for u,v in prerequisites:
            indegree[v] += 1
            adj[u].add(v)
        
        q = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        
        return max(indegree.values()) == 0


if __name__ == '__main__':
    numCourses =5 
    prerequisites = [
        [0, 1],
        [0, 2],
        [1, 3],
        [1, 4],
        [3, 4]
    ]
    s = Solution()
    # print(s.courseScheduleBfs(numCourses, prerequisites))
    print(s.courseScheduleTopo(numCourses, prerequisites))