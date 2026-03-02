class Solution {
    func numJewelsInStones(_ jewels: String, _ stones: String) -> Int {
        var res = 0
        var d: Dictionary<Character, Int> = [:]
        for s in stones {
            d[s, default: 0] += 1
        
        }
        for j in jewels {
            if let v = d[j] {
                res += v
            }
        }
        return res
    }
}