class Solution:
    def findMedian(self, nums1, nums2):

        def findKth(left, right, k):
            if not left:
                return right[k]
            if not right:
                return left[k]

            leftMid, rightMid = len(left) // 2, len(right) // 2
            leftMedian, rightMedian = left[leftMid], right[rightMid]

            if leftMid + rightMid < k:
                # if left's median is bigger than right's, right's first half doesnt include k
                if leftMedian > rightMedian:
                    return findKth(left, right[rightMid + 1:], k - rightMid - 1)
                else:
                    return findKth(left[leftMid + 1:], right, k - leftMid - 1)

            else:
                # if left's median is bigger than right's, left's second half doesn't include k
                if leftMedian > rightMedian:
                    return findKth(left[:leftMid], right, k)
                else:
                    return findKth(left, right[:rightMid], k)

        length = len(nums1) + len(nums2)
        mid = length // 2
        if length % 2:
            return findKth(nums1, nums2, mid)
        else:
            return (findKth(nums1, nums2, mid) + findKth(nums1, nums2, mid - 1)) / 2



if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 5]
    # 1, 2, 2, 3, 4, 5 -> 2.5
    s = Solution()
    print(s.findMedian(nums1, nums2))