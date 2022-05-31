from bisect import bisect_left


class Solution:
    def longestSub(self, arr):
        sub = []
        for num in arr:
            i = bisect_left(sub, num)

            # if num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num 

        return len(sub)


if __name__ == '__main__':
    s = Solution()
    print(s.longestSub([1, 2, 4, 3]))