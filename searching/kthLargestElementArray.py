# EPI solution using quick select
# The numbering starts from one, i.e. if A = [3, 1, -1, 2]
import random


def find_kth_largest_epi(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx.

        #Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left 
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    pass

# Two solutions from Leetcode
# 1) Heap -> Easy one line : heapq.nlargest(k, nums)[-1]
# 2) Quick select
# Time Complexity
# Average: O(n) time
# Worst Case: O(n^2) time
# O(1) space
def findKthLargestRecursive(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. Move all smaller elements to the left
        store_index = left 
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. Move pivot to its final place 
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def select(left, right, k_smallest):
        if left == right: # If list only has one element, return that element
            return nums[left]

        # Select a random pivot
        pivot_index = random.randint(left, right)

        # Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # The pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]

        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)

        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)


#### My Recursive Solution
# O(n) time average
# O(n^2) worst case
# O(1) if tail recursion, O(k) space if no tail recursion for the call stack.
class Solution:
    def findKthLargestRec(self, nums, k):
        k = len(nums) - k 

        def quickSelect(l, r):
            pivot, p = nums[r], l 
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:   return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)

#### My Iterative Solution
# O(n) time
# O(1) space
def findKthLargestIterative(nums, k):
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]

    def partition(left, right):
        ran = random.randint(left, right)
        pivot = right 
        swap(pivot, ran, nums)

        border = left 
        for i in range(left, right):
            if nums[i] >= nums[pivot]:
                swap(i, border, nums)
                border += 1

        swap(border, pivot, nums)
        return border

    def select(left, right, k_largest):
        result = None 
        while left <= right:
            p = partition(left, right)
            if p == k_largest:
                result = nums[k_largest]
                break
            elif p > k_largest:
                right = p - 1
            else:
                left = p + 1
        return result

    return select(0, len(nums) - 1, k - 1)




if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2 
    # print(find_kth_largest(k, nums))
    # print(findKthLargestIterative(nums, k))
    solution = Solution()
    print(solution.findKthLargestRec(nums, k))