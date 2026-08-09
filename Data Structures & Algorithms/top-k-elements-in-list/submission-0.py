class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            ans.append(freq[i][0])
        return ans
        


                
            
            
        