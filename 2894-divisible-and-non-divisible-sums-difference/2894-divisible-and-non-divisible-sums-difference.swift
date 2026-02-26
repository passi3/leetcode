class Solution {
    func differenceOfSums(_ n: Int, _ m: Int) -> Int {
        var num1 = 0
        var num2 = 0
        Array(1...n).forEach {
            $0 % m != 0 ? (num1 += $0) : (num2 += $0)
        }
        return num1 - num2
    }
}