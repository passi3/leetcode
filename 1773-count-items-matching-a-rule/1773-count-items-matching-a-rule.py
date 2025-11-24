class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                cnt += 1
                pass
            elif ruleKey == "color" and item[1] == ruleValue:
                cnt += 1
                pass
            elif ruleKey == "name" and item[2] == ruleValue:
                cnt += 1
                pass
        
        return cnt