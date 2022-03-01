class Solution:
    def optimalSolution(self, intervals):
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])

        return output


if __name__ == '__main__':
    intervals = [
        [1, 3],
        [2, 6],
        [8, 10],
        [15, 18],
    ]
    # intervals = [
    #     [1, 4],
    #     [2, 5],
    #     [3, 6],
    # ]
    # intervals = [
    #     [1, 4],
    #     [4, 5]
    # ]
    # intervals = [
    #     [1, 4],
    #     [2, 3]
    # ]
    s = Solution()
    print(s.optimalSolution(intervals))