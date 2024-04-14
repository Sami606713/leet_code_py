class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # get the min length
        min_length=min(len(word1),len(word2))

        merge=""

        for i in range(min_length):
            merge+=word1[i]+word2[i]
        
        # get the remaining element
        merge+=word1[min_length:]+word2[min_length:]


        # return the merge string
        return merge