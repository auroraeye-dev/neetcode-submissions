class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n]= count.get(n,0)+1
        arr = []
        for n, cnt in count.items():
            arr.append([cnt,n])
            arr.sort(reverse = True)
            while len(arr) > k:
                del arr[-1]
        res= []
        for pair in arr:
            res.append(pair[1])
        return res