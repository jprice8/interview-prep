import collections


class Solution:
    def topKFrequent(self, nums, k):
        buckets = [[] for _ in range(len(nums) + 1)] 
        number_count = collections.defaultdict(int)
        for num in nums:
            number_count[num] += 1

        for num, freq in number_count.items():
            buckets[freq].append(num)

        flat_list = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    flat_list.append(num)
        return flat_list[:k]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k)) # [1, 2]