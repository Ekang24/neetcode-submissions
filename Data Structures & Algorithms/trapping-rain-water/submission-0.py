class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_max = 0
        right_max = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                left_water = left_max - height[left]
                total += left_water
                left += 1

            else:
                right_water = right_max - height[right]
                total += right_water
                right -= 1

        return total
            

        