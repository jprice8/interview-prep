class Solution:
    def mergeIntervals(self, intervals):
        result = []
        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        while i < len(intervals):
            maxRight = intervals[i][1]
            newInterval = []
            j = i + 1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                maxRight = max(maxRight, intervals[j][1])
                newInterval = [intervals[i][0], maxRight]
                j += 1

            # Apply logic with j - 1
            result.append(newInterval)
            i = j - 1
            i += 1

        return result

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