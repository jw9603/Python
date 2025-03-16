# LeetCode 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

# 1. Two Pointer
# https://leetcode.com/problems/trapping-rain-water/submissions/1575509100
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        cnt = 0

        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                cnt += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                cnt += max(0, right_max - height[right])

        return cnt

# 2. Stack
# https://leetcode.com/problems/trapping-rain-water/submissions/1575513319
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        n = len(height)
        cnt = 0

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                current_spot = stack.pop()

                if not stack:
                    break
                
                left = stack[-1]
                width = i - left - 1
                height_diff = min(height[left], height[i]) - height[current_spot]
                
                cnt += height_diff * width
            stack.append(i)
        return cnt
    
if __name__ == '__main__':
    height1, height2 = [0,1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5]
    sol = Solution()

    print(f"Result1: {sol.trap(height=height1)}")
    print(f"Result2: {sol.trap(height=height2)}")