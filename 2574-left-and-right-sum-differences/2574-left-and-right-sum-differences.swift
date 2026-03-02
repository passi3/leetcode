class Solution {
    func leftRightDifference(_ nums: [Int]) -> [Int] {
        let prefix = nums.reduce(into: [Int]()) { res, n in
            let last = res.last ?? 0
            res.append(last + n)
        }
        
        let total = prefix.last!

        return nums.indices.map { i in
            let left = i == 0 ? 0 : prefix[i - 1]
            let right = total - prefix[i]
            return abs(left - right)
        }
    }
}