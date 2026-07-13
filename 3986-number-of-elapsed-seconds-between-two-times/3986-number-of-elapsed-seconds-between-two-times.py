class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def timeToSeconds(time: str) -> int:
            h, m, s = map( lambda x : int(x), time.split(":"))
            return 3600*h + 60*m + s

        s = timeToSeconds(startTime)
        e = timeToSeconds(endTime)
        
        return e-s