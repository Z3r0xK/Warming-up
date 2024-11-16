class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        ans = [1] * size

        pre = 1
        for i in range(size):
            ans[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(size-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        
        return ans