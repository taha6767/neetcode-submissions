class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s1 = ''.join(filter(str.isalnum, s))
        end= len(s1)-1
        start=0
        while (start <=end):
            if(s1[start] is not s1[end]):
                return False
            start +=1
            end -=1
        return True