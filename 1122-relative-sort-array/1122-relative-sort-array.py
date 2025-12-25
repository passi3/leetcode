class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash = {}
        notInArr2 = []

        for int2 in arr2:
            hash[int2] = arr1.count(int2)

        for int1 in arr1:
            if int1 not in arr2:
                notInArr2.append(int1)
        notInArr2.sort()

        return [k for k, v in hash.items() for _ in range(v)] + notInArr2