class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if(len(x)==0 or len(x)==1):
            return True
        else:
            if(x[0]!=x[-1]):
                return False
            else:
                return self.isPalindrome(x[1:-1])