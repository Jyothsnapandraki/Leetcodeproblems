class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {} 
        m = magazine

        for ch in ransomNote:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1

        for ch in m:
            if ch in dict:
                dict[ch] -= 1
                if dict[ch] == 0:
                    dict.pop(ch)
            else:
                continue

        if len(dict) == 0:
            return True
        else:
            return False