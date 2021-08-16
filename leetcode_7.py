class Solution:
    def reverse(self, x: int) -> int:
                     
        ans=0
        m=1
        if (x < 0):
            m=-1
            x=x*-1
        while(x!=0):
            ans=ans*10+x%10
            x=int(x/10)
        
        if(ans*m>pow(2,31)-1 or ans*m<-1*pow(2,31)):
            return 0
        
        return ans*m