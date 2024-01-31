class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        if len(d)==0:
            return []
        def f(ar,d,i,res,temp):
            if i==len(d):
                res.add(temp)
                return
            k=int(d[i])-2
            for a in range(i,len(d)):
                for j in range(len(ar[k])):
                    f(ar,d,i+1,res,temp+ar[k][j])
        ar=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        res=set()
        f(ar,d,0,res,"")
        return res
