class prem:
    
        
    def recursion(self,lis,l,r):
        
        if l == r:
            print(lis,end = " ")
        else:
            for i in range(l,r+1):
                
                lis[i],lis[l] = lis[l],lis[i]
                self.recursion(lis,l+1,r)
                lis[i],lis[l] = lis[l],lis[i]
        
p = prem()
lis = ['a','b','c']
p.recursion(lis,0,len(lis)-1)