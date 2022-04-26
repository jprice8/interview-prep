class Solution:

    def daysBetween2(self, date1, date2):
        def isLeap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 1000 == 0)

        def countSince1971(date):
            year, month, day = date.split('-')
            year, month, day = int(year), int(month), int(day)

            days = 0
            for i in range(1971, year):
                days += 365
            daysPerMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if isLeap(year):
                daysPerMonth[2] = 29
            for i in range(1, month):
                days += daysPerMonth[i]
            days += (day - 1)
            return days

        return abs(countSince1971(date1) - countSince1971(date2))


if __name__ == '__main__':
    s = Solution()
    print(s.daysBetween2('1971-06-29', '2010-09-23'))