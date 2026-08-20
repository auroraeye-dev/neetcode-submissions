class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}

        for i,n in enumerate(nums):
            diff= target - n
            if diff in dict1:
                return [dict1[diff],i]
            dict1[n]=i