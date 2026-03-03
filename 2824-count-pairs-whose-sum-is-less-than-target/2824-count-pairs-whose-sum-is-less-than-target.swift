class Solution {
    func countPairs(_ nums: [Int], _ target: Int) -> Int {
        var counter = 0
        var nums = nums
        nums.sort()
        var left = 0
        var right = nums.count - 1
        while left < right {
            if (nums[left] + nums[right] < target) {
                counter += (right - left)
                left += 1
            } else {
                right -= 1
            }
        }
        return counter
    }
}