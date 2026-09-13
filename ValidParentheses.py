class Solution:
    def isValid(self, s: str) -> bool:
        top = -1
        a = []
        for i in s:
            if i in ["(","[","{"]:
                a.append(i)
                top += 1
            elif i == ")":
                if top >= 0 and a[top] == "(":
                    a.pop(top)
                    top -= 1
                else: return False
            elif i == "]":
                if top >= 0 and a[top] == "[":
                    a.pop(top)
                    top -= 1
                else: return False
            elif i == "}":
                if top >= 0 and a[top] == "{":
                    a.pop(top)
                    top -= 1
                else: return False
        if top == -1:
            return True
        else: return False
