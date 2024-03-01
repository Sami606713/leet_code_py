import time
curr=time.time()
s = "1A man, a plan, a canal: Panama1"
new=""
for i in s:
    if (i.isalnum()):
        new+=i.lower()
print(new)
# # s="amanaplanacanalpanama"
# s ="0P"
print(new[::-1]==new)
print('time consume is: ',time.time()-curr)
