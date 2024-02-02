class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def f(k,n,res,ar,i):
            if 0==k and n==sum(ar):
                res.append(ar[:])
                return
            if k==0:
                return
            for a in range(i,10):
                ar.append(a)
                f(k-1,n,res,ar,a+1)
                ar.pop()
        ar=[]
        res=[]
        f(k,n,res,ar,1)
        return res