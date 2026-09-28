class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        opening = ('[', '{', '(')
        for letter in s:
            if letter in opening:
                stack.append(letter)
            else:
                if stack:
                    if letter ==')':
                        if stack[-1] == "(":
                            stack.pop()
                            continue
                        return False
                    elif letter == ']':
                        print(stack)
                        if stack[-1] == "[":
                            stack.pop()
                            continue
                        else:
                            return False
                    elif letter == '}':
                        if stack[-1] == "{":
                            stack.pop()
                            continue
                        return False
                else:
                    return False
        if stack:
            return False
        
        return True 
            
        