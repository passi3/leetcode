class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        output = dict()
        for i, num in enumerate(arr):
            if num in output:
                output[num] +=1
            else:
                output[num] = 1

        result = []

        for key, value in output.items():
            if value not in result:
                result.append(value)
            else:
                return False
                
        return True