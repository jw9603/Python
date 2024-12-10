# 394. Decode String
# https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        # https://leetcode.com/problems/decode-string/submissions/1475248065
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_num = 0
                current_str = ""
            
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        return current_str
    
if __name__ == '__main__':
    solution = Solution()
    
    example1 = "3[a]2[bc]"
    example2 = "3[a2[c]]"
    example3 = "2[abc]3[cd]ef"
    
    print(f"Example1: {solution.decodeString(example1)}")
    print(f"Example2: {solution.decodeString(example2)}")
    print(f"Example3: {solution.decodeString(example3)}")
    