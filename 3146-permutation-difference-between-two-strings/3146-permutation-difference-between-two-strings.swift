class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        var res = 0
        for (i, v) in s.enumerated() {
            let idx = t.firstIndex(of: v)!
            res += abs(i - t.distance(from: t.startIndex, to: idx))
        }
        return res
    }
}