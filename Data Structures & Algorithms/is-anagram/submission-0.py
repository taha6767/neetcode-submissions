class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count the number of letters and store them in a dictionary?
        #or maybe we can loop on one of the strings remove one letter
        hashS = {}
        hashT ={}
        for i in s:
            if (i in hashS) == False:
                hashS[i]=1
            else: hashS[i] +=1
        for x in t:
            if (x in hashT) == False:
                hashT[x]=1
            else: hashT[x] +=1
        if len(s) != len(t):
            return False
        else:
            for y in s:
                if (y in hashT) == False or hashS[y] != hashT[y]:
                    return False
            return True

           


        