import heapq
from typing import List


class Solution:
    # O(n^2*log(k)) time | O(k) space
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        n = len(matrix)
        for idx in range(n ** 2):        
            row = idx // n
            col = idx % n
            val = matrix[row][col]
            
            # Only poll if heap is at or past k
            if len(max_heap) >= k and val < -max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -val)
            
            # Always insert if heap not at k
            if len(max_heap) < k:
                heapq.heappush(max_heap, -val)
            
        return -max_heap[0]

    # O(X + klog(X)) time | O(X) space - where X is min(K, N)
    def lcHeap(self, matrix, k):
        # The size of the matrix
        N = len(matrix)

        # prepare the min-heap
        min_heap = []
        for r in range(min(k, N)):

            # add triplets of info for each cell
            min_heap.append((matrix[r][0], r, 0))

        # heapify the list
        heapq.heapify(min_heap)

        # until we find k elements
        while k:
            # Extract min
            element, r, c = heapq.heappop(min_heap)

            # if we have any new elements in the current row, add them
            if c < N - 1:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c + 1))

            # decrement k
            k -= 1

        return element


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    s = Solution()
    print(s.lcHeap(matrix, 8))