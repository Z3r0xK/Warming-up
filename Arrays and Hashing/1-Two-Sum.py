from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for index, value in enumerate(nums):
            if(target - value) in mapa:
                return [ mapa[(target - value)], index]
            mapa[value] = index
        return

