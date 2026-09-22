class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #loop over the array
    #maybe at every comparison also sort it
    #hash every element if you get a crash return false
    #if not return true in the end.
        hashMap ={}
        for i in nums:
            if hashMap.get(i) != None:
                return True
            else:
                hashMap[i]=i
        return False

    

