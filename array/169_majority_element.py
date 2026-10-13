class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # majority element appear more than n/2 times so it cannot be cancelled
        majority_num, majority_cnt = 0, 0

        for num in nums:
            if majority_cnt == 0:
                majority_num = num
            
            if num == majority_num:
                majority_cnt += 1
            else:
                majority_cnt -= 1
    
        return majority_num

        # Generic Solution
        # freq = {}
        # majority_num = nums[0]
        # majority_cnt = 1

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        #     if freq[num] > majority_cnt:
        #         majority_cnt = freq[num]
        #         majority_num = num
        # return majority_num
