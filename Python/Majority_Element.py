'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution(object):
    def majorityElement(self, nums):
        c=0
        k=len(nums)
        for a in set(nums[0:k/2+1]):
            for b in nums:
                if b==a: 
                    c=c+1
            if c>k/2:
                return a
            else: c=0