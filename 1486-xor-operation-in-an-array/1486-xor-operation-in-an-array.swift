class Solution {
    func xorOperation(_ n: Int, _ start: Int) -> Int {
        var res = 0
        for i in 0..<n {
            res ^= (start + 2 * i)
        }
        return res
    }
}