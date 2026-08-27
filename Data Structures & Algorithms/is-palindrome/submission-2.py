class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        resultat = ""
        for c in s:
            if c.isalnum():
                resultat+=c
        compteur = 0
        for i in range(0,len(resultat)//2):
            if resultat[i] != resultat[len(resultat) -1 - compteur]:
                return False
            compteur +=1
        return True
        