class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        for charS, charT in zip(s,t):
            if charS in mapping:
                if mapping[charS] != charT:
                    return False
            else:
                if charT in used:
                    return False
                mapping[charS] = charT
                used.add(charT)
        return True
        