from typing import List

# 1) Cycle, visited, and output
# 2) Construct adj list
# 3) Run DFS for each node in graph
# 4a) Add crs to cycle
# 4b) DFS on all neighbors of node
# 4c) remove crs from cycle
# 5) Add node to visited after visiting neighbors
# 5) Add node to output after visiting neighbors
# 6) Return the node list

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 2
        adjList = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visited, cycle = set(), set()

        # 3
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for neighbor in adjList[crs]:
                if not dfs(neighbor): return False 
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return [] 
        return output


if __name__ == '__main__':
    # pre = [[5,0], [4,0], [0,1], [0,2], [1,3], [3,2]]
    s = Solution()
    # print(s.findOrder(6, pre))
    print(s.findOrder(2, [[1,0]]))