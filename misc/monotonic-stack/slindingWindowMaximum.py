from typing import List
import collections


class Solution:
    def slidingWindowMax(self, arr: List[int], k: int) -> int:
        # init decreasing deque
        q = collections.deque([])
        res = []

        left = 0
        for idx, num in enumerate(arr):
            # handle queue
            while q and arr[q[-1]] < num:
                q.pop()
            q.append(idx)

            if left > q[0]:
                q.popleft()

            # check whether to add res
            if idx + 1 >= k:
                res.append(arr[q[0]])
                left += 1

        return res

            

if __name__ == '__main__':
    arr = [1, 6, 2, 5, 8, 7] # [3, 5, 8, 8]
    s = Solution()
    print(s.slidingWindowMax(arr, 3))