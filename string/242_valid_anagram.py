class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Compare dictionary
        if len(s) != len(t): return False
        freq_s = {}
        freq_t = {}
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        return freq_s == freq_t

        # decrement from existing dictionary
        # assume s and t are lowercase english letters
        # if len(s) != len(t): return False
        # freq_s = [0 for _ in range(26)]

        # for char in s:
        #     freq_s[ord(char) - ord('a')] += 1
        
        # for char_t in t:
        #     if freq_s[ord(char_t) - ord('a')] == 0: 
        #         return False
        #     freq_s[ord(char_t)- ord('a')] -= 1

        # return True

        # s and t can be any unique characters
        # freq_s = {}
        # if len(s) != len(t): return False

        # for char in s:
        #     freq_s[char] = freq_s.get(char, 0) + 1
        
        # for char_t in t:
        #     if char_t not in freq_s or freq_s[char_t] == 0:
        #         return False
        #     freq_s[char_t] = freq_s.get(char_t, 0) - 1

        # return True


        # nlogn runtime
        # return sorted(s) == sorted(t)