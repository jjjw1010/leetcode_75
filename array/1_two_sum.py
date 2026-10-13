class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        comp = {} # store complementary pairs index
        for i in range(n):
            # look for complementary pair
            if target - nums[i] in comp:
                # found complementary pair
                return [comp[target - nums[i]], i]
            # add num[i] as complementary
            comp[nums[i]] = i