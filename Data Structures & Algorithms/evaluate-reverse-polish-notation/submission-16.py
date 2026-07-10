class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        nums = []
        for x in tokens:
            if x not in operators:
                nums.append(int(x))
            if x in operators:
                num2 = nums.pop()
                num1 = nums.pop()
                if x == "+": nums.append(num1 + num2)
                if x == "-": nums.append(num1 - num2)
                if x == "*": nums.append(num1 * num2)
                if x == "/": nums.append(int(num1 / num2))
        return nums.pop()