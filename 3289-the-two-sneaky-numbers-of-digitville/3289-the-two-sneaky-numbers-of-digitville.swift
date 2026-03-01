class Solution {
    func getSneakyNumbers(_ nums: [Int]) -> [Int] {
        var res: [Int] = []
        var dict: Dictionary<Int, Int> = [:]
        
        nums.forEach {
            dict[$0, default: 0] += 1
            if dict[$0] == 2 { res.append($0) }
        }

        return res
    }
}