class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        frequencies = list(count.values())
        frequencies.sort(reverse=True)
        top = frequencies[:k]
        result = []
        for key, frequency in count.items():
            if frequency in top:
                result.append(key)  
        return result