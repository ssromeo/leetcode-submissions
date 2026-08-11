class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hashMap = {}
        
        for anagram in strs:
            signature = [0] * 26
            for c in anagram:
                signature[ord(c) - ord('a')] += 1
            
            key = tuple(signature)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(anagram)
            

        for key in hashMap:
            output.append(hashMap[key])
        return output
            
        