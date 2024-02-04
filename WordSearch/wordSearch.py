class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        def f(b,w,i,j,k):
          if k==len(w):
              return True
          if i<0 or j<0 or i>=len(b) or j>=len(b[0]) or b[i][j]!=w[k] or b[i][j]=="0":
              return False
          temp=b[i][j]
          b[i][j]="0"
          t=f(b,w,i-1,j,k+1)
          d=f(b,w,i+1,j,k+1)
          l=f(b,w,i,j-1,k+1)
          r=f(b,w,i,j+1,k+1)
          b[i][j]=temp
          return t or d or l or r
        for i in range(len(b)):
            for j in range(len(b[0])):
                if f(b,w,i,j,0)==True:
                   return True
        return False