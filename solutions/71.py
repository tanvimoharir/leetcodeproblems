# 71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == '/../':
            return '/'
        simplified = path.rstrip('/').replace('//', '/').replace('/./', '/').split('/')
        stack = []
        for idx, char in enumerate(simplified):
            if char == '' or char == '.':
                continue
            if simplified[idx] == '..' and stack:
                stack.pop()
            elif char != '..':
                stack.append(char)
        return '/' + '/'.join(stack)
