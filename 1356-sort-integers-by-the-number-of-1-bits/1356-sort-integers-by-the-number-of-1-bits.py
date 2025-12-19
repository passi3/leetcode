class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        hash = defaultdict(list)

        for num in arr:
            cnt = bin(num).count("1")
            hash[cnt].append(num)
        
        return [i for k in sorted(hash) for i in hash[k]]