class Solution(object):

    """ 
        Use left & right pointer, ensuring that the characters at each pointer are the same.
        If at any point the pointers disagree, the string is not a palindrome.
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(char for char in s if char.isalnum()).lower()

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if not (s[left_pointer] == s[right_pointer]): return False
            left_pointer += 1
            right_pointer -= 1
        
        return True