class Solution {
    func maxFreqSum(_ s: String) -> Int {
        var v: Dictionary<Character, Int> = [:]
        var c: Dictionary<Character, Int> = [:]
        var maxV = 0
        var maxC = 0
        let vowels = Set("aeiou")

        s.forEach {
            if vowels.contains($0) {
                v[$0, default: 0] += 1
            } else {
                c[$0, default: 0] += 1
            }
        }
        return (v.values.max() ?? 0) + (c.values.max() ?? 0)
    }
}