class Solution {
    func subsetXORSum(_ nums: [Int]) -> Int {
        var res = 0
        for i in nums.indices {
            res |= nums[i]
        }

        return res << (nums.count - 1)
    }
}