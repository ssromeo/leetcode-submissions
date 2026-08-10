class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for char in s:
            if char in hashMap:
                hashMap[char]+=1
            else:
                hashMap[char]=1
        hashMapT={}
        for char in t:
            if char not in hashMap:
                return False
            if char in hashMapT:
                hashMapT[char]+=1
            else:
                hashMapT[char]=1
       

        for c in hashMap:
            if hashMap[c] != hashMapT[c]:
                print(hashMap[c])
                print(hashMapT[c])
                return False
        return True

        
        