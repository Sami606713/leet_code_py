prices = [7,1,5,3,6,4]
left=0
right=1
max_profit=0

while(right<len(prices)):
    if(prices[left]>prices[right]):
        left=right
    else:
        diff=prices[right]-prices[left]
        # print(diff)
        if(diff>max_profit):
            max_profit=diff
        right+=1
print(max_profit)