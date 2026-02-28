class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        var res = 0
        operations.forEach {
            if $0.first == "-" || $0.last == "-" {
                res -= 1
            } else {
                res += 1
            }
        }
        return res
    }
}