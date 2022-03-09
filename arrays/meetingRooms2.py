import heapq


class Solution:
    def meetingRoomsII(self, intervals):
        start = [s[0] for s in intervals]
        start.sort()
        end = [e[1] for e in intervals]
        end.sort()
        rooms = 0
        roomsRequired = 0
        startIdx = 0
        endIdx = 0

        while startIdx < len(intervals) and endIdx < len(intervals):
            currentStart = start[startIdx]
            currentEnd = end[endIdx]

            if currentStart < currentEnd:
                rooms += 1
                startIdx += 1
            else:
                rooms -= 1
                endIdx += 1

            roomsRequired = max(roomsRequired, rooms)
        
        return roomsRequired

    def heapSolution(self, intervals):
        free_rooms = []

        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            # If the room at the top of min heap is due to end 
            # before this meeting begins, assign that room to this meeting.
            if free_rooms[0] <= current_interval[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, current_interval[1])

        return len(free_rooms)




if __name__ == '__main__':
    # intervals = [
    #     [0, 30],
    #     [5, 10],
    #     [15, 20]
    # ]
    intervals = [
        [13, 15],
        [1, 13],
        [6, 9]
    ]
    s = Solution()
    print(s.heapSolution(intervals))