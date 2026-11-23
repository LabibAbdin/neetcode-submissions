class Solution:
    def isAnagram(self, s: str, t: str):
        seen_s={}
        seen_t={}
        for chr in s:
            if chr in seen_s:
                seen_s[chr]=seen_s[chr]+1
            else:
                seen_s[chr]=1
        for chr in t:
            if chr in seen_t:
                seen_t[chr]=seen_t[chr]+1
            else:
                seen_t[chr]=1
        if seen_s==seen_t:
            return True
        return False 
        
    
    

    

        