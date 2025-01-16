class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:
            if i == '(' or i == "[" or i== "{" :
                stack.append(i)
            else :
                
                    if len(stack) == 0:
                        return False
                    
                    if (stack[-1] == "(" and i != ")") or (stack[-1] == "{" and i != "}") or (stack[-1] == "[" and i != "]") :
                       return False
                    stack.pop()
        return not stack


        