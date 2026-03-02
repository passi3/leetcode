class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        return words.filter { word in
            for char in word {
                if !allowed.contains(char) {
                    return false
                }
            }
            return true
        }.count
    }
}