# LeetCode 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        후위 표기법(tokens)이 주어졌을 때 이를 계산한 결과를 반환해라.
        """
        stack = []

        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))

        return stack[0] 