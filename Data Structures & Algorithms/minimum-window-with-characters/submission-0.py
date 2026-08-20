class Solution:
    def minWindow(self, s: str, t: str) -> str:       
        window = {}
        needed = {}
        res = [-1,-1]
        res_length = float("inf")
        for char in t:
            needed[char] = needed.get(char, 0) + 1
        
        left = 0
        have = 0
        need_count = len(needed)
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in needed:
                if window[s[right]] == needed[s[right]]:
                    have += 1

            while have == need_count:

                current_length = right - left + 1
                if current_length < res_length:
                    res = [left, right]
                    res_length = current_length

                win_left = s[left]
                window[s[left]] -= 1
                left += 1

                if win_left in needed and window[win_left] < needed[win_left]:
                    have -= 1

        if res_length == float("inf"):
            return ''
        left, right = res
        return s[left : right + 1]
            
                

            
        