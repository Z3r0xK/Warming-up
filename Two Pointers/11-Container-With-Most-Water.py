class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 2:
            return min(height)
        
        else:
            maximum = 0
            left, right = 0, (len(height)-1)
            temp = 0
            
            while left < right:
                if height[left] < height[right]:
                    temp = height[left] * (right - left)
                    left += 1
                else:
                    temp = height[right] * (right - left)
                    right -= 1
                
                maximum = max(maximum, temp)
        return maximum