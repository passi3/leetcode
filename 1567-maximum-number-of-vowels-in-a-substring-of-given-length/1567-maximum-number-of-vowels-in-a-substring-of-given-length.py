class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cnt = sum(1 for c in s[:k] if c in vowels)
        max_cnt = cnt

        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i-k] in vowels:
                cnt -= 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt