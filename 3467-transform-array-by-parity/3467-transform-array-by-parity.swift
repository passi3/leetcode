class Solution {
    func transformArray(_ nums: [Int]) -> [Int] {
        return nums.map { $0 % 2 }.sorted()
    }
}