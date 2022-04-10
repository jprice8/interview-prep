from typing import List


class Solution:
    def carPool(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        lastMile = max(trips, key=lambda x: x[2])[2]

        # 0 through last mile manifest cache
        manifest = [0] * (lastMile + 1)
        for trip in trips:
            numPassengers, fromMile, toMile = trip
            # fill in manifest with current trip
            for idx in range(fromMile, toMile):
                manifest[idx] += numPassengers

        # return whether we are under capacity throughout journey
        return all(seatsFilled <= capacity for seatsFilled in manifest)


if __name__ == '__main__':
    s = Solution()
    trips = [
        [2, 1, 5],
        [3, 3, 7],
    ]
    print(s.carPool(trips, 4)) # false
    # print(s.carPool(trips, 5)) # true