class Solution {
    func minBitFlips(_ start: Int, _ goal: Int) -> Int {
        var res = 0
        var xor = start ^ goal

        while xor > 0 {
            res += xor & 1
            xor >>= 1
        }

        return res
    }
}