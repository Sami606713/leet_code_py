class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        new_nums=[]
        zero=[]
        for i in nums:
            if i is not 0:
                new_nums.append(i)
            else:
                zero.append(i)
            
        new_nums.extend(zero)

        nums[:]=new_nums   