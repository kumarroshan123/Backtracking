class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def p(n, s, e, t,res):
            if t != "" and len(t) == 2 * n:
                res.append(t)
                return
            if s < n:
                p(n, s + 1, e, t + '(',res)
            if s > e:
                p(n, s, e + 1, t + ')',res)
        res=[]
        p(n,0,0,"",res)
        return res
