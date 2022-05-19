from typing import List


class Solution:
    def problem1(self, password: str) -> int:
        result = 0
        vowel, consonant = False, False

        vowelSet = {'a', 'e', 'i', 'o', 'u'}

        for char in password:
            if char in vowelSet:
                vowel = True
            else:
                consonant = True 

            if vowel and consonant:
                result += 1
                vowel, consonant = False, False

        return result

            

if __name__ == '__main__':
    s = Solution()
    # print(s.problem1("thisisbeautiful"))
    # print(s.problem1('rhythm'))
    print(s.problem1('hackerrank'))