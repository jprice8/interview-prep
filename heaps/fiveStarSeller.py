import heapq


# O(m*log(n) + n) time - where m is extra students and n is the number of classes
# O(n) space
def fiveStarSeller(classes, extraStudents):
    def profit(a, b):
        return (a + 1) / (b + 1) - a / b 

    maxHeap = []
    for a, b in classes:
        a, b = a * 1.0, b * 1.0 # Convert int to double
        maxHeap.append((-profit(a, b), a, b))
    heapq.heapify(maxHeap)

    for _ in range(extraStudents):
        d, a, b = heapq.heappop(maxHeap)
        heapq.heappush(maxHeap, (-profit(a + 1, b + 1), a + 1, b + 1))

    return sum(a / b for d, a, b in maxHeap) / len(classes)


if __name__ == '__main__':
    # classes = [[1, 2], [3, 9], [4, 5], [2, 10]]
    # extraStudents = 4
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    print(fiveStarSeller(classes, extraStudents))