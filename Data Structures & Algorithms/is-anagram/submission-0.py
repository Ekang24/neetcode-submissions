class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = 1+ count.get(char,0)
        
        for c in t:
            if c not in count:
                return False
            if c in count:
                count[c] -= 1
            if count[c] == 0:
                del count[c]
        
        
        if len(count) == 0:
            return True

        return False

    