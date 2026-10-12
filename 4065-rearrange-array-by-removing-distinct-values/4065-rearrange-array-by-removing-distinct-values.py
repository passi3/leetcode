class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        counter = Counter(nums)
        
        while counter:
            for key in sorted(counter.keys()):
                if counter[key] >0:
                    ans.append(key)
                    counter[key] -= 1

                    if counter[key] == 0:
                        del counter[key]
        
        return ans