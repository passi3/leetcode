class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square = students.count(1)
        circular = students.count(0)

        for s in sandwiches:
            if s == 1 and square == 0:
                break

            elif s == 0 and circular == 0:
                break

            elif s == 1 and square > 0:
                square -= 1

            elif s == 0 and circular > 0:
                circular -= 1

        return max(circular, square)
