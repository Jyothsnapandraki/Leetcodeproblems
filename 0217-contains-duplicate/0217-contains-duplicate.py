class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sum=set()
        for i in nums:
            if i in sum:
                return True
            sum.add(i)
        return False
        
