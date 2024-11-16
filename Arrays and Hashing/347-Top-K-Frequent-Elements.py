class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        buckets = [[] for i in range(len(nums) +1)]
        for frute, price in hashmap.items():
            buckets[price].append(frute)
        
        ans = []
        for price in range(len(buckets) - 1, 0, -1):
            if buckets[price]:
                for frute in buckets[price]:
                    if frute != None:
                        ans.append(frute)
                        if len(ans) == k:
                            return ans