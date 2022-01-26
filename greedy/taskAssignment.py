# O(nlog(n)) time | O(n) space - where n is the number of tasks.
def taskAssignment(k, tasks):
    tasks.sort()
    output = []
    idxA = 0
    idxB = len(tasks) - 1

    while idxA < idxB:
        optimalTasks = [idxA, idxB]
        output.append(optimalTasks)

        idxA += 1
        idxB -= 1

    return output


def aeSolution(k, tasks):
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationToIndices(tasks)

    sortedTasks = sorted(tasks)
    for idx in range(k):
        task1Duration = sortedTasks[idx]


def getTaskDurationToIndices(tasks):
    pass

if __name__ == '__main__':
    k = 3
    tasks = [1, 3, 5, 3, 1, 4] 
    # k = 1
    # tasks = [3, 5]
    print(taskAssignment(k, tasks))