class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output=[]

        prefix=[1] * (len(nums)+1)
        for i in range(0,len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
       

        suffix = [1] * (len(nums)+1)
        
        for i in range(len(nums),0,-1):
            suffix[i-1] = suffix[i] * nums[i-1]
        
        


        for i in range(0,len(nums)):
            if i == 0:
                output.append(suffix[i+1])
            elif i==len(nums)-1:
                output.append(prefix[i])
            else:
                output.append(prefix[i] * suffix[i+1])
        
        
        

        return output
                


        