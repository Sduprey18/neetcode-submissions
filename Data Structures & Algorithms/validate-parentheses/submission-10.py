class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for letter in s:
            if letter == "}":
                if stack :
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif letter == "]":
                if stack :
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif letter == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            else:
                stack.append(letter)
        
        return len(stack) == 0
        