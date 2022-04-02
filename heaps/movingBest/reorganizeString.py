from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        # count up chars in s
        str_count = Counter(s)
        # no of evens
        number_of_even_indices = (n + 1) // 2
        # prepare max heap of counts
        max_heap = []
        for char, char_count in str_count.items():
            heapq.heappush(max_heap, (-char_count, char))

        # is it possible to reorg string?
        if -max_heap[0][0] > number_of_even_indices:
            return ""

        # stores the resulting char array to be converted to string
        res = [None] * n
        """
        Pointer to the next item to be inserted.
        Increment by 2 until it reaches the end to fill out even positions,
        then it is reset to 1 to fill out odd positions.
        """
        pointer = 0
        # Insert chars into the char array by their multiplicity.
        while max_heap:
            (count, char) = heapq.heappop(max_heap)
            count = -count 
            for i in range(count):
                res[pointer] = char
                pointer += 2
                if pointer >= n:
                    pointer = 1
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("abcaa"))