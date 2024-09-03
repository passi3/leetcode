class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i, element in enumerate(words):
            if x in element:
                output.append(i)

        return output