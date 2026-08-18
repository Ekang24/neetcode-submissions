class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        for char in magazine:
            a[char] = a.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in a:
                return False
            a[char] -= 1
            if a[char] == 0:
                del a[char]
        return True

        