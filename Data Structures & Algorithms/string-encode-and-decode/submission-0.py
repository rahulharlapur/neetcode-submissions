class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(str(len(st)))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return "".join(res)
            
    def decode(self, s: str) -> List[str]:
        i=0
        sizes = []
        res = []

        while s[i] != '#':
            j=i
            size = ''
            while s[j] != ',':
                j+=1
            sizes.append(int(s[i:j]))
            i=j+1
        i+=1
        
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        
        return res


