# Write a function to find the length of the longest substring containing the same letter in a given string s, 
# after performing at most k operations in which you can choose any character of the string and change 
# it to any other uppercase English letter.

class Solution:
    def characterReplacement(self, s: str, k: int):
        state = {}# choose appropriate data structure
        start = 0
        max_ = 0
        freq_max = 0

        for end in range(len(s)):
            # extend window
            # add nums[end] to state in O(1) in time
            #A:2,B:1
            state[s[end]]= state.get(s[end],0)+1
            

            while k > 0 and len(state) < 2:
                state[s[start]] -= 1
                if state[s[start]]==0:
                    del state[s[start]]

            # repeatedly contract window until it is valid again
            # remove nums[start] from state in O(1) in time
            start += 1

            # INVARIANT: state of current window is valid here.
            max_ = max(max_, end - start + 1)

        return max_
import unittest

class TestCharacterReplacement(unittest.TestCase):
    
    def test_case_1(self):
        s = "AABABBA"
        k = 1
        expected_output = 4
        self.assertEqual(Solution().characterReplacement(s, k), expected_output)
        
    def test_case_2(self):
        s = "AABABBA"
        k = 0
        expected_output = 1
        self.assertEqual(Solution().characterReplacement(s, k), expected_output)

    def test_case_3(self):
        s = "AAAA"
        k = 0
        expected_output = 4
        self.assertEqual(Solution().characterReplacement(s, k), expected_output)
        
    def test_case_4(self):
        s = "ABBBCC"
        k = 2
        expected_output = 5
        self.assertEqual(Solution().characterReplacement(s, k), expected_output)

    def test_case_5(self):
        s = "AABCAAADA"
        k = 1
        expected_output = 7
        self.assertEqual(Solution().characterReplacement(s, k), expected_output)

if __name__ == '__main__':
    unittest.main()
