class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        buckets = [[] for _ in range(n+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        answer = []
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer

                       
        