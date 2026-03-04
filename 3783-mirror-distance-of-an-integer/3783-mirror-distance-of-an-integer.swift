class Solution {
    func mirrorDistance(_ n: Int) -> Int {
        var x = n
        var reversed = 0

        while x > 0 {
            let digit = x % 10
            reversed = reversed * 10 + digit
            x /= 10
        }

        return abs(n - reversed)
    }
}