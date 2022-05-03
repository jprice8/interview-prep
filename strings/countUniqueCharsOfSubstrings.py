import collections


class Solution:
    def countChars(self, s: str) -> int:
        last_seen = [[-1, -1] for i in range(26)]
        res = 0
        current = 0

        for i, char in enumerate(s):
            char_idx = ord(char) - 65 

            second_to_last_occ, last_occ = last_seen[char_idx]

            # num of substrings where s[i] was unique in the substring, but no longer is
            num_removed = last_occ - second_to_last_occ
            # num of substrings where s[i] does not appear
            num_added = i - last_occ

            last_seen[char_idx] = [last_occ, i]

            current += num_added - num_removed
            res += current

        return res

    def alternate(self, s):
        last_position = collections.defaultdict(int)
        contribution = collections.defaultdict(int)
        res = 0

        for i, char in enumerate(s):
            max_possible_substrs_at_idx = i + 1
            contribution[char] = max_possible_substrs_at_idx - last_position[char]

            res += sum(contribution.values())
            last_position[char] = i + 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.countChars('ABC'))
    print(s.alternate('ABA'))