class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = ""
        plate = Counter(char for char in licensePlate.lower() if char.isalpha())

        for word in words:
            wordCounter = Counter(word)
            if all(wordCounter[char] >= plate[char] for char in plate):
                if res == "" or len(word) < len(res):
                    res = word
        return res