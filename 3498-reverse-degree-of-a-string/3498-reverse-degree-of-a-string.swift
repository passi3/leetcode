class Solution {
    func reverseDegree(_ s: String) -> Int {
        var res = 0
        for (i, v) in s.enumerated() {
            res += (i + 1) * (26 - (Int(v.asciiValue!) - 97))
        }
        return res
    }
}