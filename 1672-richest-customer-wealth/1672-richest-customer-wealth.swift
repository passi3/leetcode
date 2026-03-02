class Solution {
    func maximumWealth(_ accounts: [[Int]]) -> Int {
        var res = 0
        accounts.forEach {
            res = max(res, $0.reduce(0, +))
        }
        return res
    }
}