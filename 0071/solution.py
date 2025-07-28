class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for cmd in path.split("/"):
            if cmd == "..":
                if stack:
                    stack.pop()
            elif cmd == "." or not cmd:
                continue
            else:
                stack.append(cmd)
        resp = "/" + "/".join(stack)
        return resp