# Solutio 1
low = 7
high = 9
count=0
for i in range(low,high+1):
    if(i%2 is not 0):
        count+=1
        print(i)
print(count)

# Solution 2
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if(low%2!=0):
            result=abs((low-high)//2) +  (high %2)
            return result
        else:
            result=abs((low-high)//2) +  (low %2)
            return result

