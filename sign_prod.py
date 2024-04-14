class Solution:
    def arraySign(self, nums: List[int]) -> int:
        import numpy as np
        
        prod=1

        for i in nums:
            prod=prod*i
        
        return np.sign(prod)