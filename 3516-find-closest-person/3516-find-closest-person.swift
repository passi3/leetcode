class Solution {
    func findClosest(_ x: Int, _ y: Int, _ z: Int) -> Int {
        let first = abs(x-z)
        let second = abs(y-z)
        if first == second { return 0 }
        return first < second ? 1 : 2
    }
}