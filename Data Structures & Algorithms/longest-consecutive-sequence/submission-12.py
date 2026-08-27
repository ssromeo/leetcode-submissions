class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sortedArray = list(sorted(set(nums)))
        print(sortedArray)
        
        output = 0
        temp = 0
        for i in range(0,len(sortedArray)-1):
            #faire le if pour pass le for si c le meme cas. 
            if sortedArray[i+1] == sortedArray[i] +1:
                temp += 1
            else:               
                temp = 0
            if temp > output:
                output = temp            
        
        if not nums:
            return 0
        return output+1
        