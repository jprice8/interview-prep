class MySolution:
    def comboSum(self, candidates, target):
        return self.allSum(candidates, target)

    def allSum(self, candidates, target):
        if target == 0:
            return [[]]

        combos = []
        for num in candidates:
            remainder = target - num 
            if remainder >= 0:
                recursiveResult = self.allSum(candidates, remainder)
                for sub_list in recursiveResult:
                    sub_list.append(num)
                combos.extend(recursiveResult)

        return combos


    def recursiveHelper(self, candidates, target):
        if target == 0:
            return []
        elif target < 0:
            return None 

        for num in candidates:
            remainder = target - num 
            result = self.recursiveHelper(candidates, remainder)
            if result is not None:
                result.append(num)
                return result

        return None


class AMSolution:
    def comboSum(self, candidates, target):
        result = []
        self.allSum(candidates, target, result, [], 0)
        return result

    def allSum(self, candidates, target, result, path, start_idx):
        if target == 0:
            result.append(path[:])
            return 
        
        for idx in range(start_idx, len(candidates)):
            num = candidates[idx]
            remaining = target - num
            if remaining < 0:
                continue 
            self.allSum(candidates, remaining, result, path + [num], idx)


# O(n^t/m) time | O(t/m) - Where n is the length of candidates, t is the target value, m is the min value of candidates.
class LCSolution:
    def comboSum(self, candidates, target):
        result = []
        self.allSum(candidates, target, result, [], 0)
        return result 

    def allSum(self, candidates, target, result, path, start_idx):
        if target == 0:
            result.append(list(path))
            return 

        elif target < 0:
            return 

        for i in range(start_idx, len(candidates)):
            num = candidates[i]
            # Add the number into path to try
            path.append(num)
            remaining = target - num
            self.allSum(candidates, remaining, result, path, i)
            # Backtrack remove the number from path
            path.pop()

if __name__ =='__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    # s = MySolution()
    # print(s.comboSum(candidates, target))
    # am = AMSolution()
    # print(am.comboSum(candidates, target))
    lc = LCSolution()
    print(lc.comboSum(candidates, target))