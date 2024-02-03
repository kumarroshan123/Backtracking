class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def f(s,i,ar,res):
            if i==len(ar)+1:
                return 
            else:
                res.append(''.join(s))
            for a in range(i,len(ar)):
                s[ar[a]]=s[ar[a]].swapcase()
                f(s,a+1,ar,res)
                s[ar[a]]=s[ar[a]].swapcase()
                
        ar=[]
        res=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]<"0" or s[i]>"9":
                ar.append(i)
        f(s,0,ar,res)
        return res