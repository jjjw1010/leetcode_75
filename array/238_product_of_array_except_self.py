class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        # O(n) runtime 
        # O(1) space time excluding output array
        product = [1 for _ in range(n)]

        for i in range(n):
            product[i] *= prefix            # Product of everything left of i
            prefix *= nums[i]               # Update prefix for next i
            product[n - i - 1] *= suffix    # Product of everything right of i
            suffix *= nums[n - i - 1]       # Update suffix for next i
        return product


        # O(n) Runtime
        # O(n) spacetime
        # n = len(nums)
        # l_product = [1 for _ in range(n)]
        # r_product = [1 for _ in range(n)]


        # # left product/ prefix product
        # for i in range(1, n):
        #     l_product[i] = nums[i - 1] * l_product[i - 1]
        #     r_product[n - i - 1] = nums[n - i] * r_product[n - i]

        # return [r_product[j] * l_product[j] for j in range(n)]