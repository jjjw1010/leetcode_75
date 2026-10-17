class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        
        odd_addon = 0
        total = 0
        for value in freq_s.values():
            if value % 2 != 0 : 
                odd_addon = 1
                total += value - 1
            else:
                total += value
        return total + odd_addon