class Solution {
    func scoreOfString(_ s: String) -> Int {
        var res = 0
        let nums = s.map { Int($0.asciiValue!) }
        for i in 0..<nums.count - 1 {
            res += abs(nums[i] - nums[i + 1])
        }
        return res
    }
}