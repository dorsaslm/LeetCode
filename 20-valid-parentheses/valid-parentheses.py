class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            stack = []
            for element in s:
                if element in ('(','[','{'):
                    stack.append(element)
                elif element in (')',']','}') and (len(stack)!=0):
                    if ((element == ')' and stack[-1]=='(') or (element == ']' and stack[-1]=='[') or (element == '}' and stack[-1]=='{')):
                        stack.pop()
                    else: 
                        return False
                else:
                    return False
            if len(stack) == 0:
                return True
            else:
                return False


        