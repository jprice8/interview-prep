def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1) 
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)


def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))


def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    return merged


def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursString = str(hours)
    minutesString = "0" + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minutesString


if __name__ == '__main__':
    calendar1 = [
        ['9:00', '10:30'],
        ['12:00', '13:00'],
        ['16:00', '18:00'],
    ]
    dailyBounds1 = ['9:00', '20:00']
    calendar2 = [
        ['10:00', '11:30'],
        ['12:30', '14:30'],
        ['14:30', '15:00'],
        ['16:00', '17:00'],
    ]
    dailyBounds2 = ['10:00', '18:30']
    meetingDuration = 30
    print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))