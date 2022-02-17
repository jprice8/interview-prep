def combinationSum(candidates, target):
    result = []
    dfs(candidates, 0, target, [], result)
    return result

def dfs(nums, start_index, remaining, path, result):
    # if state is a solution
    if remaining == 0:
        result.append(path[:]) # Add state to final result list
        return 

    # Iterate through children and make a recursive call
    for i in range(start_index, len(nums)):
        num = nums[i]
        # Is child not a potential match?
        if remaining - num < 0:
            continue 
        dfs(nums, i, remaining - num, path + [num], result)


class Solution:
    def combinationSum(self, candidates, target):
        results = []

        def backtrack(remaining, path, start_index):
            if remaining == 0:
                results.append(list(path))
                return 
            elif remaining < 0:
                return 

            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                # Add the number into the path
                path.append(candidate)
                # Give the current number another change, rather than moving on
                backtrack(remaining - candidate, path, i)
                # Backtrack, remove the number from the combination
                path.pop()

        backtrack(target, [], 0)

        return results

    


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    # print(combinationSum(candidates, target))
    solution = Solution()
    print(solution.combinationSum(candidates, target))