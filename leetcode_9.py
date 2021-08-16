class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        for i in range(int(len(s)/2)):
            if(s[i]!=s[-1-i]):
                return False
        return True
print(Solution.isPalindrome(1,131))