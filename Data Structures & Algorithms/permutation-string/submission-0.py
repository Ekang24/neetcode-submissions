class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1
        left = 0
        window = {} 
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if count == window:
                return True
        return False
            


            

        