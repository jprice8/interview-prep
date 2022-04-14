from typing import List


class Solution:
    def transactionLogs(self, logs: List[str], threshold: int) -> List[str]:
        pass

if __name__ == '__main__':
    logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
    s = Solution()
    print(s.transactionLogs(logs, 2))