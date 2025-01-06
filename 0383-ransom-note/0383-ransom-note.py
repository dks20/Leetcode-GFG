class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in ransomNote:
            if i in hash1:
                hash1[i] +=1
            else:
                hash1[i] = 1

        for j in magazine:
            if j in hash2:
                hash2[j] += 1
            else:
                hash2[j] = 1
        
        for key,values in hash1.items():
            if key not in hash2 or hash2[key] < values:
                return False
        return True

        