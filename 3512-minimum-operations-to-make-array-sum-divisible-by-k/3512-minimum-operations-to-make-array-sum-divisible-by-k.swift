class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let sum = nums.reduce(0, +)
        return sum % k
    }
}