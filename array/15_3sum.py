class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # two point solution w/ more exits
        n = len(nums)
        ans = []
        nums = sorted(nums)

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue
            if nums[k] > 0: break

            left = k + 1
            right = n - 1

            while left < right:

                total = nums[left] + nums[right] + nums[k]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    # total == 0 
                    ans.append([nums[k], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ans

        # solution inspired by two sum
        # O(n^2) but with less exits

        # n = len(nums)
        # ans = []
        # nums.sort()
        # seen = set()
        # for k in range(n):
        #     target = -nums[k]
        #     comp = set()
        #     seen_j = set()
        #     if target in seen: continue
        #     for j in range(k + 1, n):
        #         if nums[j] in seen_j : continue
        #         if target - nums[j] not in comp:
        #             comp.add(nums[j])
        #         else:
        #             ans.append([-target, target - nums[j], nums[j]])
        #             seen_j.add(nums[j])
        #             seen_j.add(target - nums[j])
        #     seen.add(target)
        # return ans
