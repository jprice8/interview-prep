from typing import List


# O(n) time | O(n) space - Where n is the length of points.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x, y = point 
            distance = self.findDistance(x, y)
            distances.append(distance)

        self.quickSelect(distances, k)
        return distances[-k:]

    def findDistance(self, x1, y1):
        x2, y2 = 0, 0
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def quickSelect(self, array, k):
        # Set k as len(array) - k
        k_index = len(array) - k 
        def qs(left, right):
            # Set p_index and pivot_number
            p_index, pivot_number = left, array[right]

            # Loop from left to right
            for i in range(left, right):
                if array[i] <= pivot_number:
                    array[i], array[p_index] = array[p_index], array[i]
                    p_index += 1

            array[right], array[p_index] = array[p_index], array[right]

            if k < p_index:
                return qs(left, p_index - 1)
            elif k > p_index:
                return qs(p_index + 1, right)
            else:
                return array[k]

        qs(0, len(array) - 1)


if __name__ == '__main__':
    points = [
        [1, 3],
        [-2, 2]
    ]
    k = 1

    s = Solution()
    print(s.kClosest(points, k))