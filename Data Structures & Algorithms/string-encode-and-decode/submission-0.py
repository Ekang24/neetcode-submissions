class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
    
        while i < len(s):
            j=i
            while s[i] != '#':
                i += 1
            length = int(s[j:i])
            i+= 1


            decoded_string.append(s[i:i+length])

            i += length

        return decoded_string


