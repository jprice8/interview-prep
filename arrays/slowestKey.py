def slowestKey(releaseTimes, keysPressed):
    previousKey = keysPressed[0]
    previousTime = releaseTimes[0]

    for idx in range(1, len(releaseTimes)):
        time = releaseTimes[idx]
        duration = time - previousTime
        if duration > previousTime or (duration == previousTime and keysPressed[idx] > previousKey):
            previousTime = duration 
            previousKey = keysPressed[idx]

    return previousKey


if __name__ == '__main__':
    # releaseTimes = [1, 2]
    # keysPressed = "ba"
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    print(slowestKey(releaseTimes, keysPressed))