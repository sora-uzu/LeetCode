class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack =[]

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False

                last_open = stack.pop()
                expected_close = brackets[last_open]

                if expected_close != char:
                    return False

        return not stack
