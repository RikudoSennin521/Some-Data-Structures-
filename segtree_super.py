# Python3 Code Addition
class ST:
    def __init__(self,arr):
        self.N = len(arr)
        self.T = [0] * (2 * self.N)  
    # insert leaf nodes in tree 
        for i in range(self.N) : 
            self.T[self.N + i] = arr[i]; 
      
    # build the tree by calculating parents 
        for i in range(self.N - 1, 0, -1) : 
            self.T[i] = self.T[i << 1] + self.T[i << 1 | 1]; 
  
# function to update a tree node 
    def updateTreeNode(self,p, value) : 
      
    # set value at position p 
        self.T[p + self.N] = value; 
        p = p + self.N; 
      
    # move upward and update parents 
        i = p
      
        while i > 1 :
          
            self.T[i >> 1] = self.T[i] + self.T[i ^ 1]; 
            i >>= 1; 
  
    # function to get sum on interval [l, r) 
    def query(self,l, r) : 
  
        res = 0; 
      
        # loop to find the sum in the range 
        l += self.N
        r += self.N
      
        while l < r :
      
            if (l & 1) :
                res += self.T[l]; 
                l += 1
      
            if (r & 1) :
                r -= 1
                res += self.T[r]; 
              
            l >>= 1
            r >>= 1
      
        return res; 
  
# Driver Code
if __name__ == "__main__" : 
  
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
  
    t = ST(a)

      
    # print the sum in range(1,2) index-based 
    print(t.query(1, 3)); 
      
    # modify element at 2nd index 
    t.updateTreeNode(2, 1); 
      
    # print the sum in range(1,2) index-based 
    print(t.query(1, 3)); 
      