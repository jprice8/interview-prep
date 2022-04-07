from typing import List


class Solution:
    def freshPromo(self, codeList: List[List[str]], shoppingCart: List[str]) -> bool:
        codeIdx, cartIdx = 0, 0

        while codeIdx < len(codeList) and cartIdx < len(shoppingCart):
            currentCodeList = codeList[codeIdx]
            currentShoppingItem = shoppingCart[cartIdx]
            # check for match
            if currentCodeList[0] == 'anything' or currentCodeList[0] == currentShoppingItem:
                # potential match
                if self.checkForMatch(currentCodeList, cartIdx, shoppingCart):
                    cartIdx += 1
                    codeIdx += 1

                else:
                    cartIdx += 1

            cartIdx += 1

        return 1 if codeIdx == len(codeList) else 0

    def checkForMatch(self, currentCodeList, cartIdx, shoppingCart):
        tmpCartIdx = cartIdx
        for codeItem in currentCodeList:
            if codeItem == shoppingCart[tmpCartIdx] or codeItem == 'anything':
                tmpCartIdx += 1
            else:
                return False 
        return True


if __name__ == '__main__':
    codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
    shoppingCart = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange', 'banana', 'orange']
    s = Solution()
    print(s.freshPromo(codeList, shoppingCart)) 