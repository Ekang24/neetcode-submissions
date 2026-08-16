class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0
        score = 0
        for right in range(1, len(s)):
            a = abs(ord(s[left]) - ord(s[right]))
            score += a
            left += 1
        return score

        