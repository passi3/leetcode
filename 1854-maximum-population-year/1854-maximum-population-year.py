class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for i in logs:
            events.append([i[0], 1])
            events.append([i[1], -1])
        
        events.sort(key= lambda x:(x[0], x[1]))
        year = 0
        max_population =0
        t = 0
        for j in events:
            t += j[1]
            if t > max_population:
                max_population = t
                year = j[0]
        return year