# O(n) time | O(1) space
# def minRewards(array):
#     lowestScoreIdx = getLowestScoreIdx(array) 
#     totalRewards = 1

#     # If min is not first element
#     if lowestScoreIdx != 0:
#         cachedScore = 1
#         left = lowestScoreIdx - 1
#         while left >= 0:
#             if array[left] > array[left + 1]:
#                 cachedScore += 1
#                 totalRewards += cachedScore
#             else:
#                 cachedScore = 1
#                 totalRewards += cachedScore

#             left -= 1

#     # If min is not last element
#     if lowestScoreIdx != len(array) - 1:
#         cachedScore = 1
#         right = lowestScoreIdx + 1
#         while right < len(array):
#             if array[right] > array[right - 1]:
#                 cachedScore += 1
#                 totalRewards += cachedScore
#             else:
#                 cachedScore = 1
#                 totalRewards += cachedScore

#             right += 1

#     return totalRewards

# def getLowestScoreIdx(array):
#     lowestScoreIdx = 0
#     lowestScore = float("inf")
#     for idx, val in enumerate(array):
#         if val < lowestScore:
#             lowestScore = val
#             lowestScoreIdx = idx

#     return lowestScoreIdx


def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

if __name__ == '__main__':
    # print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])) # 25
    print(minRewards([0, 4, 2, 1, 3])) # 9