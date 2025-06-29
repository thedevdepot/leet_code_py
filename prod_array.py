#!/usr/bin/env python3

from typing import List

# Product of an Array except self
# leet code 238
# Given an integer array nums, return and array answer such that answer[i]
# is equal to the product of all elements of nums except nums[i]
#
# must fit 32 bit
# must run O(n) without division operator
#
# Example [1, 2, 3, 4]
# output [24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        # Calculate suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    print(result)
