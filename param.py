paran='{([])}{}([{}])'
# paran ="(]"
stack=[]

# make a paranthesis pair
dic={"}":"{",")":"(","]":"["}
# itrate loop and read each letter char by char
for i in paran:
   # check  the char in dic
   if i in dic:
      print(dic[i])
      # append in stack
      stack.append(i)
   else:
      # else remove the char in list 
      if i in dic.keys():
         if(len(stack)==0):
            print('false')
         else:
            re=stack.pop()
            if(dic[i]!=re):
               print('False')
print(len(stack)==0)

# ---leet code fuction
class Solution:
    def isValid(self, s: str) -> bool:
        # make a empty stack
        stack=[]
        # make a dic
        dic={"}":"{",")":"(","]":"["}
        for paran in s:
            if paran in dic.values():
                stack.append(paran)
            else:
                if not stack:
                    return False
                remove_element=stack.pop()
                if(dic[paran]!=remove_element):
                    return False
        return stack==None

      