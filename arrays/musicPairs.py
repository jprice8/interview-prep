from collections import Counter
import collections


def musicPairs(time):
    c = [0] * 60 
    result = 0
    for songLength in time:
        result += c[-songLength % 60]
        c[songLength % 60] += 1
    return result


def amSolution(time):
    complement = Counter()
    ans = 0
    for t in time:
        if (-t % 60) in complement:
            ans += complement[-t % 60]
        complement[t % 60] += 1
    return ans


def lcSolution(time):
    remainders = collections.defaultdict(int)
    # remainders = {}
    result = 0

    for songLength in time:
        if songLength % 60 == 0: # check if a % 60 == 0 and b % 60 == 0
            result += remainders[0]
        else: # check if a % 60 + b % 60 == 60
            result += remainders[60 - songLength % 60]
        remainders[songLength % 60] += 1
    return result


if __name__ == '__main__':
    time = [30, 20, 150, 100, 40]
    print(musicPairs(time))
    # print(amSolution(time))
    # print(lcSolution(time))