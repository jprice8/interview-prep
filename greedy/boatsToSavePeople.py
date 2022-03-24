from typing import List


class Solution:
    def boatsToSave(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1

        ans = 0
        while l < r:
            ans += 1

            if people[l] + people[r] <= limit:
                l += 1
            r -= 1

        return ans


if __name__ == '__main__':
    people = [3, 2, 2, 1]
    limit = 3
    # people = [1, 2, 1, 2]
    # limit = 4
    s = Solution()
    print(s.boatsToSave(people, limit))