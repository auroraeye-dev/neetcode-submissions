class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}

        for i, n in enumerate(nums):
            dict1[n]=i
        for i,n in enumerate(nums):
            diff= target - n
            if diff in dict1 and dict1[diff]!= i:
                return [i, dict1[diff]]
        return []