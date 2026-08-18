class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set()
        res = 0
        for char in allowed:
            a.add(char)
        for word in words:
            valid = 1
            for char in word:
                if char not in a:
                    valid = 0
                    break
            if valid:
                res += 1    
        return res
