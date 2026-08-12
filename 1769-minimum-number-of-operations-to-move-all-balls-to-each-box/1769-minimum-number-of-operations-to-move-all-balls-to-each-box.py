class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        
        res[0] = sum(i for i, c in enumerate(boxes) if c == "1")

        right_count = boxes.count("1")
        left_count = 0

        if boxes[0] == "1":
            right_count -= 1
            left_count += 1

        for i in range(1, n):
            res[i] = res[i - 1] - right_count + left_count

            if boxes[i] == "1":
                right_count -= 1
                left_count += 1

        return res