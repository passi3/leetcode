class Solution {
    func largestLocal(_ grid: [[Int]]) -> [[Int]] {
        let n = grid.count
        
        var res = Array(
            repeating: Array(
                repeating: 0,
                count: n - 2),
            count: n - 2
        )
        
        for i in 0..<(n - 2) {
            for j in 0..<(n - 2) {
                var maxV = 0

                for x in i...(i + 2) {
                    for y in j...(j + 2) {
                        maxV = max(maxV, grid[x][y])
                    }
                }

                res[i][j] = maxV
            }
        }
        return res
    }
}