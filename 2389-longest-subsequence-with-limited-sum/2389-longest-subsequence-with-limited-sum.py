class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefixSum = 0
        sums = []
        
        for num in nums:
            prefixSum += num
            sums.append(prefixSum)

        answer = []

        for query in queries:
            start, end = 0, n

            while start < end:
                mid = (start + end) // 2
                if sums[mid] <= query:
                    start = mid + 1
                else:
                    end = mid
            
            answer.append(start)
        return answer