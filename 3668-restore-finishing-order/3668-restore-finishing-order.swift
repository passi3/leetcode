class Solution {
    func recoverOrder(_ order: [Int], _ friends: [Int]) -> [Int] {
        return order.filter { friends.contains($0)}
    }
}