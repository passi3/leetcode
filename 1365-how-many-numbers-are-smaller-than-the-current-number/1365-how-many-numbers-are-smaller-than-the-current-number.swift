class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        let sortedNums = nums.sorted()
        var map: [Int: Int] = [:]
        
        for (i, num) in sortedNums.enumerated() {
            if map[num] == nil {
                map[num] = i
            }
        }
        return nums.map { map[$0]! }
    }
}