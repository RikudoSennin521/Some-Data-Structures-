def summation(a,b):
    return a + b
 
#to query (l,r) use (l,r + 1)
class STree:
    def __init__(self,arr,default = 0,func = summation):
        n = len(arr)
        self.default = default
        self.size = n
        self.func = func
        self.tree = [default]*(4*n)
        self.build(arr)
        
    
    def build(self,arr):
        n = len(arr)
 
        for i in range(n):
            self.tree[n + i] = arr[i]
 
        for i in range(n - 1, 0 , -1):
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])
 
    def updateTreeNode(self,p,value):
        n = self.size
        self.tree[p + n] = value
        p = p + n
 
        i = p
 
        while i > 1:
            self.tree[i >> 1] = self.func(self.tree[i],self.tree[i ^ 1])
            i >>= 1
 
 
    def query(self,l,r):
        n = self.size
        res = 0
 
        l += n
        r += n
        res_left = res_right = self.default
        while(l < r):
            #print(l,r)
            if l & 1:
                res_left =  self.func(res_left,self.tree[l])
                l += 1
 
            if r & 1:
                r -= 1
                res_right = self.func(res_right,self.tree[r])
 
            l >>= 1
            r >>= 1
 
        res = self.func(res_left,res_right)
 
        return res
