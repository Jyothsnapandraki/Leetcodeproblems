class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxv=max(nums)
        index=nums.index(maxv)
        for num in nums:
            if num!=maxv and maxv<2*num:
                return -1
        return index