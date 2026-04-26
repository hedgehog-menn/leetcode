class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""

        for c in path + "/":
            if c == "/":
                if current == "..":
                    if stack: # if not empty
                        stack.pop()
                elif current != "" and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += c

        return "/" + "/".join(stack)
        