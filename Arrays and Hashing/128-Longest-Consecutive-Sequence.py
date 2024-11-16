class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not len(nums):
            return 0
        if len(nums) == 1:
            return 1
        hashmap = {}
        numset = set(nums)
        nums.sort()

        for num in nums:
            if (num-1) in numset:
                hashmap[num] = hashmap.get(num-1, 0) + 1
            else:
                hashmap[num] = 1

        return(max(list(hashmap.values())))