class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in range(len(s) - 1, -1 ,-1):
            if s[char] == ' ' and length != 0:
                return length
            elif s[char] == ' ' and length == 0:
                continue
            length += 1
        
        return length
        