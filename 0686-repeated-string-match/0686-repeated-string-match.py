class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep = a
        count =1

        while (len(rep) < len(b)):
            rep += a
            count+=1

        if b in rep:
            return count
        
        rep += a
        count +=1
        if b in rep:
            return count
        else:
            return -1



        