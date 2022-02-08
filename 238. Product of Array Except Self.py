class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZero, prod, zeroidx = 0, 1, 0
        for i, num in enumerate(nums):
            if num == 0:
                numZero += 1
                zeroidx = i
            else:
                prod *= num
        if numZero >= 2:
            return [0] * len(nums)
        if numZero == 1:
            ret = [0] * len(nums)
            ret[zeroidx] = prod
            return ret
        
        # backward pass
        ret = [0] * len(nums)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            ret[i] = prod
        # forward pass
        prod = 1
        for i, num in enumerate(nums):
            prod *= num
            nums[i] = prod    
            
        ret[0] = ret[1]
        for i in range(1, len(nums)-1):
            ret[i] = nums[i-1] * ret[i+1]
        ret[-1] = nums[-2]
        return ret
        








# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         num_zeros = 0
#         all_product = 1
#         zero_idx = -1
        
#         for i, num in enumerate(nums):
#             if num == 0:
#                 num_zeros += 1
#                 zero_idx = i
#             else:
#                 all_product *= num
                
#         if num_zeros >= 2:
#             return [0] * len(nums)

#         if num_zeros == 1:
#             ret = [0] * len(nums)
#             ret[zero_idx] = all_product
#             return ret
        
#         ret = []
#         for num in nums:
#             temp = self.fast_subtractor(abs(all_product), abs(num))
#             if not((all_product > 0) ^ (num > 0)):
#                 ret.append(temp)
#             else:
#                 ret.append(-temp)
#         return ret
        
#     def fast_subtractor(self, num, denom):
#         if denom == 1:
#             return num
#         ret = 0
#         now_denom = denom
#         now_share = 1
#         while now_denom <= num:
#             while now_denom <= num:
#                 num -= now_denom
#                 ret += now_share
#                 now_denom *= 2
#                 now_share *= 2
#             now_denom = denom
#             now_share = 1
#         return ret
