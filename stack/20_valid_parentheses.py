class Solution:
    def isValid(self, s: str) -> bool:

        # odd length string is not valid
        if len(s) % 2 != 0 : return False

        stack = []
        paren_dict = {"{" : "}", "[" : "]", "(" : ")"}
        for char in s:
            if char in paren_dict:
                stack.append(paren_dict[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack # stack is not empty