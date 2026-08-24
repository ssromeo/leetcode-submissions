class Solution:

    def encode(self, strs: List[str]) -> str:
        output  = "" 
        for string in strs:
            sizeWord = len(string)
            output += str(sizeWord) + "#"+ string
        print(output)
        return output


    def decode(self, s: str) -> List[str]:
        
        liste = list(s)
        output = []
        pointeur = 0
        i=0
        j=i
        temp=""
        while i < len(liste):
            while liste[j] != "#": 
                temp += liste[j]
                j+=1
            
            pointeur = int(str(temp))
            print(pointeur)
            output.append("".join(liste[j+1:j+int(pointeur)+1]))
            i = j + int(pointeur) + 1
            j=i
            temp = ""
        if not output:
            return []
        return output





        return ["","r"]
