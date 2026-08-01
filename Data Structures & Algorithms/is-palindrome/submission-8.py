import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        reverse_i = len(s) - 1


        while i <= reverse_i:   
            if s[i].isalnum() == False:
                i += 1
                continue

            if s[reverse_i].isalnum() == False:
                reverse_i -= 1
                continue

            # If either side mismatches then return False
            if s[i].lower() != s[reverse_i].lower():
                print("FALSE")
                return False

            i += 1
            reverse_i -= 1

        return True