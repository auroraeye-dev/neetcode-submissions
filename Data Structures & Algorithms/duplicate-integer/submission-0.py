class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new=set()
        for i in nums:
            if i in new:
                return True
            elif i not in new:
                new.add(i)
        else:
            return False