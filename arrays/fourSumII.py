

def fourSumCount(nums1, nums2, nums3, nums4):
    count = 0
    hashMap = {}

    for i in nums1:
        for j in nums2:
            twoNumberSum = i + j
            if twoNumberSum in hashMap:
                hashMap[twoNumberSum] += 1
            else:
                hashMap[twoNumberSum] = 1

    for i in nums3:
        for j in nums4:
            twoNumberSum = i + j
            if twoNumberSum in hashMap:
                count += hashMap[-(i + j)]

    return count


fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])

