import heapq
import itertools
from typing import Iterator, List


def kLongest(k: int, stream: Iterator[str]) -> List[str]:
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]

    heapq.heapify(min_heap)
    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


if __name__ == '__main__':
    k = 2
    stream = []