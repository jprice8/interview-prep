class Solution:
    def plusOne(self, digits):
        digits.reverse()
        carry, i = 1, 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0

            else:
                digits.append(1)
                carry = 0
    
            i += 1
        return digits[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3,9,9]))