import numpy as nu
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst = nu.zeros(10**6 + 15)
        for i in range(len(nums)):
            lst[nums[i]] += 1
        for i in range(len(lst)):
            if lst[i] > 1:
                return True
        return False
        