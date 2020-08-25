"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        index = []
        for i in range(len(nums)):
            index.append(i)
            sum = nums[i]
            for k in range(i + 1, len(nums)):
                if (sum+ nums[k]) == target:
                    index.append(k)
                    return index
            index.remove(i)

if __name__ == "__main__":
    sol = Solution()
    #index = sol.twoSum([2, 7, 11, 15],9)
    index = sol.twoSum([3,2,3],6)
    print(index)