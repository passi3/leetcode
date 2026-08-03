class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        res = []

        while i >= 0 or k > 0 or carry > 0:
            digit_num = num[i] if i >= 0 else 0
            digit_k = k % 10

            total = digit_num + digit_k + carry

            res.append(total % 10)
            carry = total // 10

            i -= 1
            k //= 10

        return res[::-1]