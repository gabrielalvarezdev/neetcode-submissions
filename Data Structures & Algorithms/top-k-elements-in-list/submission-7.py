class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = set(nums)
        frequency = dict.fromkeys(numset, 0)
        for num in nums:
            frequency[num]+=1
        sorted_keys = sorted(frequency, key=frequency.get, reverse=True)
        return sorted_keys[:k]