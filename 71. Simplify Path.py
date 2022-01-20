class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        for path in paths:
            if path:
                if path == '.':
                    continue
                elif path == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(path)
        ret = '/'
        for path in stack:
            ret += path + '/'
        if not stack:
            return ret
        return ret[:-1]
