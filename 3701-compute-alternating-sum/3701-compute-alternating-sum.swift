class Solution {
    func alternatingSum(_ nums: [Int]) -> Int {
        var res = 0
        for (i, v) in nums.enumerated() {
            res += (i % 2 == 0) ? v : -v
        }
        return res
    }
}