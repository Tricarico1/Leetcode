# Write a function to return the length of the longest substring in a provided string s where all characters in the substring are distinct.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        max_ = 0
        for end in range(len(s)):
            dic[s[end]] = dic.get(s[end],0)+1

            while dic[s[end]] > 1:
                dic[s[start]] -=1
                start+=1
            max_ = max(max_, end-start+1)
        return max_
        
# Unit Tests using unittest
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)
    
    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)
    
    def test_no_repeated_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)
    
    def test_with_duplicates(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
    
    def test_all_same_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaaaa"), 1)
    
    def test_mixed_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

# Main block to run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()