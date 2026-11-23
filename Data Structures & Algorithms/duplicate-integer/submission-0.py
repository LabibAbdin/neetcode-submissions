class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]=seen[num]+1
            else: seen[num]=1
            if seen[num]>1:
                return True
        return False