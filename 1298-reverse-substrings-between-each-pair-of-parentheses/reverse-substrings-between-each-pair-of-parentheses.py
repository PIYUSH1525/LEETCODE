class Solution:
    def reverseParentheses(self, s: str) -> str:
        ind_stack: deque[int] = deque()
        res: list[str] = []
        for char in s:
            if char == "(":  
                ind_stack.append(len(res)) 
            elif char == ")":  
                start_ind: int = ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)
        return "".join(res)