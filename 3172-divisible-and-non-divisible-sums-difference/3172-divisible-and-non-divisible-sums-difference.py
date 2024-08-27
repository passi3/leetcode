class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        list1 = [i for i in range(1, n+1) if i%m != 0]
        list2 = [i for i in range(1, n+1) if i%m == 0]

        return sum(list1)-sum(list2)