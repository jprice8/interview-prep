import collections
from typing import List


class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[int]) -> bool:
        graph = { i: [] for i in range(numCourses) }
        return graph


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    s = Solution()
    print(s.courseSchedule(numCourses, prerequisites))