# Given an array of integers, return indices of the two numbers such that they add up to specific target.
# You may assume that each input would be exactly one solution, and you may not use the same element twice.
# 
# Given nums [2,7,11,15], target = 9
# Because num(0) + num(1) = 2 + 7 = 9
# return = [0, 1] 

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()


# time o(n)
# meme 0(n)
