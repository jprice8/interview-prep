from typing import List


class Solution:

    def sortingByKeysApproach(self, logs):
        def get_key(log):
            _id, content = log.split(" ", 1)
            return (0, content, _id) if log[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


if __name__ == '__main__':
    logs = ["let1 art can", "dig1 8 5 1", "let2 art own"]
    s = Solution()
    print(s.sortingByKeysApproach(logs))