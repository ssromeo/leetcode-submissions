class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap={}
        for num in nums:
            if num not in hashMap:
                hashMap[num]=0
            hashMap[num]+=1

        output=[]
        result = sorted(hashMap.values(),reverse=True)[:k]
        for key,value in hashMap.items():
            if value in result:
                output.append(key)
        return output
            

        