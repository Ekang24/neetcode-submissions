class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = right
            right = max(current, right)
        return arr

        