class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b+a)
                elif token == '*':
                    stack.append(b*a)
                elif token == '/':
                    stack.append(int(b / a))
                else:
                    stack.append(b-a)
        return stack.pop()
           