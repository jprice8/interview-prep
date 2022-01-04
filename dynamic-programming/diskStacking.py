def diskStacking(disks):
    disks = sorted(disks, key=lambda x: x[2])
    results = [0 for _ in disks]
    results[0] = disks[0][2]
    output = []

    for i in range(1, len(disks)):
        currentDisk = disks[i]
        previousDisk = disks[i - 1]
        # Check to see if width and depth are greater than previous element.
        if currentDisk[0] > previousDisk[0] and currentDisk[1] > previousDisk[1]:
            results[i] = results[i - 1] + currentDisk[2]
            output.append(currentDisk)
        # Else check if we'd be better off starting over with current
        else:
            if currentDisk[2] > results[i - 1]:
                results[i] = currentDisk[2]
                output.append(currentDisk)
            else:
                results[i] = results[i - 1]

    return output 


if __name__ == '__main__':
    disks = [[2, 1, 2], [3, 2, 3]]
    print(diskStacking(disks))