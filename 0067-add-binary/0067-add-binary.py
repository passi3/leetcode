class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        initial = 0

        i, j = len(a)-1, len(b)-1

        while i>=0 or j>=0 or initial:
            num_a = int(a[i]) if i>=0 else 0
            num_b = int(b[j]) if j>=0 else 0

            total = num_a+num_b+initial
            initial = total//2
            result.append(str(total % 2))

            i -= 1
            j -= 1
        return ''.join(result[::-1])