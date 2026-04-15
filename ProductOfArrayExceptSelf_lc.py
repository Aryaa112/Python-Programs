"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1]*n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(n-1,-1,-1):
            ans[i] *= sufix
            sufix *= nums[i]
        return ans
