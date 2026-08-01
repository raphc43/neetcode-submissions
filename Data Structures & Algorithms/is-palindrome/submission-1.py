import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        inv_s = s[::-1]

        if s == inv_s:
            return True
        else:
            return False

        