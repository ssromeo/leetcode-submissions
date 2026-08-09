class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        digitSeen=[]
        for num in nums:
            if num in digitSeen:
                return True
            digitSeen.append(num)
        return False
            


        