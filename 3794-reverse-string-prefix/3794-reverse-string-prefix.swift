class Solution {
    func reversePrefix(_ s: String, _ k: Int) -> String {
        let idx = s.index(s.startIndex, offsetBy: k)
        var prefix = String(s[..<idx].reversed())
        return prefix + String(s[idx...])
    }
}