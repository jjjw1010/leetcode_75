class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1 # assume positivity if no sign is present
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # Ignore any leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # signedness
        if i < n and s[i] in "+-":
            sign = 1 if s[i] == "+" else -1
            i += 1
        
        # conversion
        ans = 0
        while i < n and ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9'):
            ans = ans * 10 + ord(s[i]) - ord('0')

            # round within 32-bit signed integer range [-2 ** 31, 2 ** 31 - 1]
            if ans * sign < INT_MIN:
                return INT_MIN
            if ans * sign > INT_MAX:
                return INT_MAX
            
            i += 1
        return ans * sign