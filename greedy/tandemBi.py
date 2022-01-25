# O(nlog(n)) time | O(1) space - where n is the number of cyclist.
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    blueShirtSpeeds.sort()
    if fastest:
        redShirtSpeeds.sort()
    else:
        redShirtSpeeds.sort(reverse=True)
    returnSpeed = 0

    for idx in range(len(redShirtSpeeds)):
        redSpeed = redShirtSpeeds[len(redShirtSpeeds) - idx - 1]
        blueSpeed = blueShirtSpeeds[idx]

        returnSpeed += max(redSpeed, blueSpeed)

    return returnSpeed


def aeSolution(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        totalSpeed += max(rider1, rider2)
    return totalSpeed


def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = True 
    print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)) # 25
    # print(aeSolution(redShirtSpeeds, blueShirtSpeeds, fastest))