'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        n= len(s)
        m= len(t)

        while(i<n and j<m):
            if s[i]==t[j]:
                i=i+1
                j=j+1
            else: j=j+1 
        
        if i==n: return True
        return False
