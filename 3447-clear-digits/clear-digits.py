class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for each in s:
            if each.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(each)
        return "".join(stack)
        