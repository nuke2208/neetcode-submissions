class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                c = b + a
                stack.append(c)
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                c = b*a
                stack.append(c)
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                c = int(b/a)
                stack.append(c)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        