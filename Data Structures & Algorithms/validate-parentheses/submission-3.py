class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                res.append(c)
            elif c == ")":
                if len(res) > 0 and res.pop() == "(":
                    continue
                return False
            elif c == "}":
                if len(res) > 0 and res.pop() == "{":
                    continue
                return False
            elif c == "]":
                if len(res) > 0 and res.pop() == "[":
                    continue
                return False
        if len(res) > 0:
            return False
        return True
