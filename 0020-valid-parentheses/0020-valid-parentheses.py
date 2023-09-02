class Solution:
    def isValid(self, s: str) -> bool:
        HashMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in HashMap:
                if stack and stack[-1] == HashMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
    