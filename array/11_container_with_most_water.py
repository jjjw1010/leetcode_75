class Solution:
    def maxArea(self, height: list[int]) -> int:

        # Two point solution O(n) run time O(1) space
        # Optimzed solution by computing less (new height must be greater to compute)
        left = 0
        right = len(height) - 1
        maxArea = 0
        h = 0

        while left < right:
            h = min(height[left], height[right])
            tmpArea = (right - left) * h
            maxArea = max(tmpArea, maxArea)

            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
            
        return maxArea

        # O(1) space time complexity
        # O(n) runtime complexity
        # n = len(height)
        # left = 0
        # right = n - 1
        # maxArea = 0

        # while left < right:
        #     tmpArea = (right - left) * min(height[left], height[right])

        #     maxArea = max(tmpArea, maxArea)
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return maxArea
