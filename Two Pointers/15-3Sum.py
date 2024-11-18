class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, value in enumerate(nums):

            # case 1 handle
            if value > 0:
                break

            # case 2 handle
            if index > 0 and value == nums[index - 1]:
                continue

            # we will apply solution of two sum II, here
            start, end = index + 1, len(nums) - 1

            while start < end:
                currSum = value + nums[start] + nums[end]
                if currSum > 0:
                    # mov rightPointer
                    end -= 1

                elif currSum < 0:
                    # mov leftPointer
                    start += 1

                else:
                    result.append([value, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

        return result