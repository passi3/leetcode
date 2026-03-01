class Solution {
    func defangIPaddr(_ address: String) -> String {
        return address.map { $0 == "." ? "[.]" : String($0) }.joined()
    }
}