import heapq
from typing import List


class Solution:
    def problem1(self, popularity: List[int], k: int) -> List[int]:
        output = [[]]

        for num in popularity:
            step = [curr + [num] for curr in output]
            # output += [curr + [num] for curr in output]
            output += step

        minHeap = []
        for subset in output:
            subsetSum = sum(subset)
            if len(minHeap) < k:
                heapq.heappush(minHeap, subsetSum)
            elif subsetSum > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, subsetSum)

        res = []
        for _ in range(len(minHeap)):
            res.append(heapq.heappop(minHeap))

        res.reverse()
        return res

    def recursion(self, popularity: List[int], k: int) -> List[int]:
        def dfs(path, used, minHeap, currSum):
            # base
            if len(path) == len(popularity):
                return

            for idx, num in enumerate(popularity):
                if used[idx]:
                    continue 

                currSum += num

                # if not k sums, add to heap anyway and continue
                if len(minHeap) < k:
                    heapq.heappush(minHeap, currSum)
                elif currSum > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, currSum)

                # recursion
                path.append(num)
                used[idx] = True 
                # check if 
                dfs(path, used, minHeap, currSum)
                path.pop()
                used[idx] = False
                currSum -= num

        minHeap = []
        dfs([], [False] * len(popularity), [], minHeap, 0)
        return minHeap[::-1]


if __name__ == '__main__':
    arr = [3, 5, -2]
    s = Solution()
    print(s.problem1(arr, 3))