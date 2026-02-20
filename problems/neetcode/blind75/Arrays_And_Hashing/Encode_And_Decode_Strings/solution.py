from typing import List

# somewhat hacky solution. If it wasn't specified in the problem that only 
# ASCII would be transmitted, there would be problems
class Solution_One:
    delimiter = '🦆'
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += self.delimiter
            encoded_str += str
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        decoded_str = s.split(self.delimiter)
        del decoded_str[0]  # get rid of unnecessary ''
        return decoded_str

# solution that would work beyond just ASCII
class Solution:
    def delimited_str(self, input: str) -> str:
        return f"{len(input) + 1}${input}"

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += self.delimited_str(str)
        
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        length_str = ''
        for c in s:
            if c != '$':
                length_str += c
                continue
            else:
                break
        length = int(length_str)

        next_word = ''
        for i in range(len(length_str) + 1, len(length_str) + length):
            next_word += s[i]
        return [next_word] + self.decode(s[(length + len(length_str)):])