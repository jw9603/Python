# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/description/

class Solution(object):
    def calculate(self, s):
        # https://leetcode.com/problems/basic-calculator-ii/submissions/1476667577
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        n = len(s)
        sign = '+'
        stack = []
        num = 0
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if char in '+/*-' or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / float(num)))
            
                sign = char
                num = 0
        
        return sum(stack)
    
if __name__ == '__main__':
    solution = Solution()
    example1 = "3+2*2"
    example2 = " 3/2 "
    example3 = " 3+5 / 2 "
    
    print(f"Result1: {solution.calculate(example1)}")
    print(f"Result2: {solution.calculate(example2)}")
    print(f"Result3: {solution.calculate(example3)}")
                
                