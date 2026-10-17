class Solution:
    def isPalindrome(self, s: str) -> bool:
        # retain alnum characeters
        # lowercase the CAP letters
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

        # s = "".join(char.lower() for char in s if char.isalnum())
        # return s == s[::-1]

        