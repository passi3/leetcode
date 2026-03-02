class Solution {
    func convertDateToBinary(_ date: String) -> String {
        return date.split(separator: "-").map { String(Int($0)!, radix: 2)}.joined(separator: "-")
    }
}