class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0

        for event in events:
            if counter >= 10:
                break
            elif event in ["WD", "NB"]:
                score += 1
            elif event == "W":
                counter += 1
            else:
                score += int(event)
        
        return [score, counter]