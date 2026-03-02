class Solution {
    func shuffle(_ nums: [Int], _ n: Int) -> [Int] {
        var res: [Int] = []

        for i in 0..<n {
            res.append(nums[i])
            res.append(nums[i+n])
        }
        return res
    }
}