class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        a = {}
        for char in chars:
            a[char] = a.get(char, 0) + 1
        for word in words:
            n = {}
            for char in word:
                n[char] = n.get(char,0) + 1
            valid = 1
            for char in n:
                if char not in a or n[char] > a[char]:
                    valid = 0
                    break
            if valid:
                res += len(word)

        return res