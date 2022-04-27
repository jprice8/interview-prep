class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        #2) contains one of three required types
        missing_type = 3
        if any('a' <= c <= 'z' for c in password): missing_type -= 1
        if any('A' <= c <= 'Z' for c in password): missing_type -= 1
        if any(c.isdigit() for c in password): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < len(password):
            # 3 No three repeating chars
            if password[p] == password[p - 1] == password[p - 2]:
                length = 2
                while p < len(password) and password[p] == password[p - 1]:
                    length += 1
                    p += 1

                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1

        # 1 check required lengthA
        if len(password) < 6:
            # not enough chars
            return max(missing_type, 6 - len(password))
        elif len(password) <= 20:
            # enough chars, just changes and missing types
            return max(missing_type, change)
        else:
            # too many chars
            delete = len(password) - 20

            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3 

            return delete + max(missing_type, change)


if __name__ == '__main__':
    s = Solution()
    print(s.checkPassword('Febbbbbbyb007')) # 0
    print(s.checkPassword('aA1')) # 3