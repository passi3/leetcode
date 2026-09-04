class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def dfs():
            cnt = 0

            for char in counter:
                if counter[char] == 0:
                    continue
                
                counter[char] -= 1
                cnt += 1
                cnt += dfs()
                counter[char] += 1
        
            return cnt
        
        return dfs()