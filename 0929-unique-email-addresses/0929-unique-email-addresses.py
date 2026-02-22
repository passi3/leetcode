class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            n, d = e.split('@') 
            l = n.split('+')[0].replace('.', '')
            s.add(l + '@' + d)
        return len(s)