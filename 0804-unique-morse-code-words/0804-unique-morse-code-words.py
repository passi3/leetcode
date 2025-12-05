class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        hashmap = dict()
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i, code in enumerate(codes):
            hashmap[chr(97+i)] = code
        
        for word in words:
            encode = ''.join(hashmap[char] for char in word)
            res.add(encode)
        
        return len(res)