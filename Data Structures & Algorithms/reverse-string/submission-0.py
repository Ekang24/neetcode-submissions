class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            l = s[left]
            r = s[right]
            s[right] = l
            s[left] = r
            left += 1
            right -= 1
        