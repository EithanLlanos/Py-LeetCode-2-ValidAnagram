# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

################################################################################################################################


#First Attempt:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1
        for i in t:
            dic2[i] = dic2.get(i,0) + 1
        if len(dic) != len(dic2): return False
        try:    
            for k in dic:
                if dic[k] != dic2[k]: return False
        except: return False    
        return True
    