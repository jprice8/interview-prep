class Solution:
    #O(min(n,m)) time | O(1) space - where n is the length of nums1 and m is the length of nums2
    def medianOfTwoSorted(self, nums1, nums2):
        A, B = nums1, nums2 
        total = len(nums1) + len(nums2)
        half = total // 2 

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                # Bleft is gt Aright
                l = i + 1


if __name__ == '__main__':
    # example 1
    # nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # nums2 = [1, 2, 3, 4, 5]

    # example 2
    nums1 = [1, 2, 8, 9, 15]
    nums2 = [7, 11, 18, 19, 21, 25]
    s = Solution()
    print(s.medianOfTwoSorted(nums1, nums2))