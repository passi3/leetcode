class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        valid = defaultdict(list)
        validChar = set('abcdefghijklmnopqrstuvwxyz0123456789_')
        for i in range(len(code)):
            target = code[i].lower()
            if not isActive[i] or target == "" or set(target).difference(validChar) or businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue
            valid[businessLine[i]].append(code[i])
        print(valid)
        for order in ["electronics", "grocery", "pharmacy", "restaurant"]:
            if order not in valid:
                continue
            res += sorted(valid[order])
        
        return res