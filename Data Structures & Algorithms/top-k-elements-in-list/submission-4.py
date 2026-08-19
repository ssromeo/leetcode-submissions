class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap={}
        for num in nums:
            if num not in hashMap:
                hashMap[num]=0
            hashMap[num]+=1
        bucket=[[] for _ in range(len(nums)+1)]
       
        for key,value in hashMap.items():
            bucket[value].append(key)
        bucket = [bucket[x] for x in range(len(bucket)-1,0,-1) if  bucket[x]]
        bucket = [num for sublist in bucket for num in sublist]
        print(bucket)
        return bucket[:k]
