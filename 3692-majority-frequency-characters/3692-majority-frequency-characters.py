class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        hash = {}
        maxk = []

        for char in set(s):
            k = s.count(char)
            if k in hash:
                hash[k].append(char)
            else:
                hash[k] = [char]
        
            if len(hash[k]) > len(maxk):
                maxk = hash[k]
                prevK = k
            if len(hash[k]) == len(maxk):
                if k >= prevK:
                    maxk = hash[k]
                    prevK = k

        return "".join(maxk)
