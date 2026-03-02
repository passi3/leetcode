class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        var res = 0
        var dict: Dictionary<Character, Int> = [:]
        
        for i in 0..<t.count {
            let index = t.index(t.startIndex, offsetBy: i)
            let value = t[index]
            dict[value] = i
        }

        for i in 0..<s.count {
            let index = s.index(s.startIndex, offsetBy: i)
            let value = s[index]
            let diff = abs(i-(dict[value] ?? 0))
            res += diff
        }
        return res
    }
}