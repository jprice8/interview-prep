class Solution:
    def armstrongNumber(self, n: int) -> bool:
        n_string = str(n)
        n_list = [char for char in n_string]

        list_length = len(n_list)
        running_sum = 0
        for char in n_list:
            char_int = int(char)
            running_sum += char_int ** list_length

        return n == running_sum


if __name__ == '__main__':
    s = Solution()
    print(s.armstrongNumber(153))