class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored = defaultdict(int)
        colores = defaultdict(set)
        ret = []
        for i in range(len(queries)):
            ball, color = queries[i]
            
            if ball in colored:
                colores[colored[ball]].remove(ball)
                if len(colores[colored[ball]]) == 0:
                    del colores[colored[ball]]
            colored[ball] = color 
            colores[color].add(ball)
            ret.append(len(colores))
        
        return ret