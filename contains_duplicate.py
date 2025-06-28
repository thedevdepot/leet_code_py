'''
217 leet code contains duplicate
Given and integer array nums, return true if any value appears at least twice in the array.
Return false if every element is distinct

Ex. input nums [1, 2, 4, 1]
return True
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Check if a list contains duplicate numbers."""
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


def main():
    solution = Solution()

    # Example 1: List with duplicates
    nums1 = [1, 2, 3, 1]
    print(f"List: {nums1} contains duplicates: {solution.containsDuplicate(nums1)}")

    # Example 2: List without duplicates
    nums2 = [1, 2, 3, 4]
    print(f"List: {nums2} contains duplicates: {solution.containsDuplicate(nums2)}")

    # Example 3: Empty list
    nums3 = []
    print(f"List: {nums3} contains duplicates: {solution.containsDuplicate(nums3)}")

    # Example 4: List with single element
    nums4 = [1]
    print(f"List: {nums4} contains duplicates: {solution.containsDuplicate(nums4)}")


if __name__ == "__main__":
    main()
        





