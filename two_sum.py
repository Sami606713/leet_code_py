numbers=[2,7,11,15]
target=9
dic={}
for index,value in enumerate(numbers):
    # find the complement
    complement=target-value
    if(value in dic):
        print([dic[value]+1,index+1])
    else:
        dic[complement]=index
