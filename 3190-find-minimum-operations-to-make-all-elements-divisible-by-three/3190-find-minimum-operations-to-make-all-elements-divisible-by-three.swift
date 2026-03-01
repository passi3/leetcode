class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var res = 0
        nums.forEach {
            if $0 % 3 != 0 {
                res += 1
            }
        }
        return res
    }
}