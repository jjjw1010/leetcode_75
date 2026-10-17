class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        r = 0     # red starting pt
        b = len(nums) - 1 # blue starting pt

        while i <= b:
            if nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                # initially, r has been checked since r = 0 and i = 0
                r += 1
                i += 1 # no need to check swapped value since nums[i] is either 0 or 1

            elif nums[i] == 2:
                nums[b], nums[i] = nums[i], nums[b]
                b -= 1
                # need to check new nums[i] after swapped; nums[i] can be either 0 or 1
            else:
                i += 1