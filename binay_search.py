# set two pointer
    # i-low pointer set at index 0
    # ii high pointer set at 2 last index
# while loop when low<=high
    # find the mid point
    # if(given array mid is equal to target )
        # return 
    # if value greater to target :
        # set the high to mid- high
        # a
def binary_search(array, target):
   # set the two pointer high and low
    low=0
    high=len(nums)-1
        
        # itrate the while loop
    while(low<=high):
            # calculate the mid point
        mid=(low+high)//2

            # check the  mid value
        if(nums[mid]==target):
                return mid
        elif(nums[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1

# low=0 high=7
array = [1, 2, 3, 10, 4, 5, 6, 7, 18]
print(binary_search(array, 18))


# array=[1,2,3,4,5,6,7,8]
# print(binary_search(array,6))
# # [1,2,3,4] [5,6,7,8]