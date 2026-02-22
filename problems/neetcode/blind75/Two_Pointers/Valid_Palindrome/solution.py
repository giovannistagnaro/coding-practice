class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(character.lower() for character in s if character.isalnum())
        a, b = 0, len(clean_s) - 1

        while b > a:
            if clean_s[a] != clean_s[b]:
                return False
            a += 1
            b -= 1
        return True