class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        nums.reduce(0, +) % k
    }
}