# Naive O(n^2)
def longest_substring_without_repeating(string):
    longest = 0

    for start in range(len(string)):
        for end in range(len(string)):
            sub = string[start : end + 1]
            if len(set(sub)) == len(sub):
                longest = max(longest, end + 1 - start)

    return longest




if __name__ == '__main__':
    string = 'abcdbea'
    print(longest_substring_without_repeating(string))