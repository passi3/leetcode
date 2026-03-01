class Solution {
    func findWordsContaining(_ words: [String], _ x: Character) -> [Int] {
        var res: Array<Int> = []
        for (idx, word) in words.enumerated() {
            if word.contains(x) { res.append(idx)}
        }
        return res
    }
}