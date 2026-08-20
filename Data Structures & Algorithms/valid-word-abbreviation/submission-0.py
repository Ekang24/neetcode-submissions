class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        
        while i < len(word) and j < len(abbr):
            number = ''
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                while j < len(abbr) and abbr[j].isdigit():
                    
                    number += abbr[j]
                    if number[0] == '0':
                        return False
                    j += 1
                forward = int(number)
                i += forward
        if i == len(word) and j == len(abbr):
            return True
        return False         


        