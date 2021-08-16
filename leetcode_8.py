class Solution:
    def myAtoi(self, s: str) -> int:
        ans="" 
        for i in s:
            if(i==' '):
                if(len(ans)==0):
                    continue
                else:
                    break
            elif(48<=ord(i)<=67):
                ans+=i
            elif(i=='-'or i=='+'):
                if(len(ans)==0):
                    ans+=i
                else:
                    break
            else:
                if(len(ans)>0):
                    break
                else:
                    return 0
        if(len(ans)==0 or ans=='-' or ans=='+'):
            return 0
        ans=int(ans)
        if(ans<-1*pow(2,31)):
            return -1*pow(2,31)
        elif(ans>pow(2,31)-1):
            return pow(2,31)-1
        else:
            return ans